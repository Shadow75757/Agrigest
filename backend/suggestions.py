"""
Implementa o padrão Strategy para sugestões agrícolas
baseadas nos dados meteorológicos obtidos.
"""

from abc import ABC, abstractmethod

class SuggestionStrategy(ABC):
    @abstractmethod
    def suggest(self, weather_data: dict) -> str:
        pass

class IrrigationStrategy(SuggestionStrategy):
    def suggest(self, weather_data: dict) -> str:
        humidity = weather_data.get("main", {}).get("humidity", 100)
        rain = weather_data.get("rain", {}).get("1h", 0)
        rain_forecast = weather_data.get("weather", [{}])[0].get("main", "").lower()

        if humidity < 40 and rain == 0 and rain_forecast not in ["rain", "drizzle"]:
            return "Sugerido: Irrigação necessária devido à baixa humidade e ausência de chuva."
        return "Irrigação não recomendada."

class FertilizationStrategy(SuggestionStrategy):
    def suggest(self, weather_data: dict) -> str:
        rain_forecast = weather_data.get("weather", [{}])[0].get("main", "").lower()
        if rain_forecast not in ["rain", "drizzle"]:
            return "Sugerido: Condições favoráveis para fertilização."
        return "Fertilização adiada devido à previsão de chuva."

class CoverageStrategy(SuggestionStrategy):
    def suggest(self, weather_data: dict) -> str:
        wind_speed = weather_data.get("wind", {}).get("speed", 0)
        rain = weather_data.get("rain", {}).get("1h", 0)
        if rain > 10 or wind_speed > 15:
            return "Sugerido: Utilizar cobertura devido à chuva forte ou vento intenso."
        return "Cobertura não necessária."

class SuggestionContext:
    def __init__(self):
        self.strategies = [
            IrrigationStrategy(),
            FertilizationStrategy(),
            CoverageStrategy()
        ]

    def get_suggestions(self, weather_data: dict) -> list[str]:
        return [strategy.suggest(weather_data) for strategy in self.strategies]
