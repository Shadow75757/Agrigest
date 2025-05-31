import unittest
from suggestions import IrrigationStrategy

class TestSuggestions(unittest.TestCase):
    def test_irrigation_low_humidity(self):
        strategy = IrrigationStrategy()
        weather_data = {
            "main": {"humidity": 30},
            "rain": {},
            "weather": [{"main": "Clear"}]
        }
        result = strategy.suggest(weather_data)
        self.assertIn("Irrigação necessária", result)

    def test_irrigation_high_humidity(self):
        strategy = IrrigationStrategy()
        weather_data = {
            "main": {"humidity": 70},
            "rain": {},
            "weather": [{"main": "Clear"}]
        }
        result = strategy.suggest(weather_data)
        self.assertIn("não recomendada", result)

if __name__ == "__main__":
    unittest.main()
