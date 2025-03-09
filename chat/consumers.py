import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("✅ WebSocket Connected!")  # Debugging
        await self.accept()

    async def disconnect(self, close_code):
        print(f"❌ WebSocket Disconnected! Close code: {close_code}")  
        # Do NOT call close() here, let the client handle reconnection

    async def receive(self, text_data):
        print(f"📩 Received message: {text_data}")  # Debugging
        data = json.loads(text_data)
        message = data['message']
        user = data['user']

        # Send message back to client
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user
        }))