import unittest
import os
import json
from storage import save_record, get_history, DB_FILE

class TestStorage(unittest.TestCase):
    def setUp(self):
        # Backup original DB if exists
        if os.path.exists(DB_FILE):
            os.rename(DB_FILE, DB_FILE + ".bak")

    def tearDown(self):
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)
        if os.path.exists(DB_FILE + ".bak"):
            os.rename(DB_FILE + ".bak", DB_FILE)

    def test_save_and_get(self):
        record = {"city": "TestCity", "datetime": "2025-01-01T00:00:00Z"}
        save_record(record)
        history = get_history()
        self.assertTrue(any(r["city"] == "TestCity" for r in history))

if __name__ == "__main__":
    unittest.main()
