"""
Servidor WebSocket para comunicação com clientes React.
Recebe cidade, responde com dados + sugestões.
"""

import asyncio
import websockets
import json
from weather_api import WeatherAPI
from suggestions import SuggestionContext
from storage import save_record
from datetime import datetime

connected_clients = set()

async def handle_client(websocket, path):
    connected_clients.add(websocket)
    api = WeatherAPI()
    sugg_ctx = SuggestionContext()

    try:
        async for message in websocket:
            data = json.loads(message)
            city = data.get("city")
            user = data.get("user", "Guest")

            if not city:
                await websocket.send(json.dumps({"error": "Cidade não fornecida"}))
                continue

            weather_data = await api.fetch_weather(city)
            suggestions = sugg_ctx.get_suggestions(weather_data)

            record = {
                "city": city,
                "datetime": datetime.utcnow().isoformat() + "Z",
                "weather": weather_data,
                "suggestions": suggestions,
                "user": user
            }
            save_record(record)

            response = {
                "weather": weather_data,
                "suggestions": suggestions
            }
            await websocket.send(json.dumps(response))
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

async def start_server():
    print("Servidor WebSocket iniciado na porta 8765")
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()  # executa indefinidamente
