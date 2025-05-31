"""
Implementação de padrões de design usados no sistema.
"""

# Singleton já implementado em weather_api.py (WeatherAPI)

# Strategy implementado em suggestions.py (SuggestionStrategy)

# Facade implementado em weather_api.py (WeatherAPI classe)

# Exemplo genérico de Singleton para reutilização futura:

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
