"""
Módulo para comunicação com a API OpenWeatherMap.
Implementa padrão Facade para simplificar a interação.
"""

import aiohttp
import asyncio

API_KEY = "8308621c89d7d1f83e27b92133cd6a04"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class WeatherAPI:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WeatherAPI, cls).__new__(cls)
        return cls._instance

    async def fetch_weather(self, city: str) -> dict:
        """
        Obtém dados meteorológicos atuais da API para uma cidade.
        """
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "lang": "pt"
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(BASE_URL, params=params) as resp:
                data = await resp.json()
                return data

# Exemplo de uso:
# api = WeatherAPI()
# dados = asyncio.run(api.fetch_weather("Lisboa"))
