import unittest
import asyncio
from weather_api import WeatherAPI

class TestWeatherAPI(unittest.IsolatedAsyncioTestCase):
    async def test_fetch_weather(self):
        api = WeatherAPI()
        data = await api.fetch_weather("Lisboa")
        self.assertIn("main", data)
        self.assertIn("temp", data["main"])

if __name__ == "__main__":
    unittest.main()
