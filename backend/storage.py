"""
Módulo para armazenamento local dos dados em JSON.
Permite salvar e ler histórico.
"""

import json
import os
from datetime import datetime
from threading import Lock

DB_FILE = "backend/weather_history.json"
_lock = Lock()

def save_record(record: dict):
    """
    Guarda uma nova consulta no ficheiro JSON de histórico.
    """
    _lock.acquire()
    try:
        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = []

        data.append(record)

        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    finally:
        _lock.release()

def get_history() -> list:
    """
    Retorna todo o histórico armazenado.
    """
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
