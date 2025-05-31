"""
Ponto de entrada do servidor backend WebSocket.
Inicia o servidor e gerencia conexões.
"""

import asyncio
from websocket_server import start_server

if __name__ == "__main__":
    print("Iniciando servidor WebSocket Agrigest...")
    asyncio.run(start_server())
