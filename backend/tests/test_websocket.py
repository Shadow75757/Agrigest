import unittest
import asyncio
import websockets
import json
from threading import Thread
from websocket_server import start_server

class WebSocketTest(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_thread = Thread(target=lambda: asyncio.run(start_server()), daemon=True)
        cls.server_thread.start()
        asyncio.sleep(1)

    async def test_websocket_response(self):
        uri = "ws://localhost:8765"
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({"city": "Lisboa", "user": "test"}))
            response = await websocket.recv()
            data = json.loads(response)
            self.assertIn("weather", data)
            self.assertIn("suggestions", data)

if __name__ == "__main__":
    unittest.main()
