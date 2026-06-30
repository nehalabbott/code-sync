from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, room: str, websocket: WebSocket):
        await websocket.accept()

        if room not in self.active_connections:
            self.active_connections[room] = []

        self.active_connections[room].append(websocket)

    def disconnect(self, room: str, websocket: WebSocket):
        if room in self.active_connections:
            self.active_connections[room].remove(websocket)

            if len(self.active_connections[room]) == 0:
                del self.active_connections[room]

    async def broadcast(self, room: str, message: str):
        if room not in self.active_connections:
            return

        for connection in self.active_connections[room]:
            await connection.send_text(message)


manager = ConnectionManager()