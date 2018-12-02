# ray test added
# from channels.consumer import AsyncConsumer

# class EchoConsumer(AsyncConsumer):

#     async def websocket_connect(self, event):
#         await self.send({
#             "type": "websocket.accept"
#         })

#     async def websocket_receive(self, event):
#         # Echo the received payload
#         await self.send({
#             "type": "websocket.send",
#             "text": event["text"]
#         })

import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class NoseyConsumer(AsyncJsonWebsocketConsumer):
    # ray: method when websocket is on
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)
        # ray: it output as times as opened browsers
        print(f"Added {self.channel_name} channel to gossip")
    # ray: method when websocket is off
    async def disconnect(self):
        await self.channel_layer.group_discard("gossip", self.channel_name)
        print(f"Removed {self.channel_name} channel from gossip")

    # ray: this is called when a new user is added on admin panel
    async def user_gossip(self, event):
        # ray: send a message down to the client
        await self.send_json(event) # ray: event passes to webSocketBridge.listen of home.html
        print(f"Got message {event} at {self.channel_name}")
