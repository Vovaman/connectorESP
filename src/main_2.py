# abstract websocket class for BaseConnector
# it has to implement some methods, described below...

import asyncio as a
from websocket import WebSocket

class TstWebSocket(WebSocket):

    def __init__(self):
        self.ws = WebSocket()

    async def handshake(self, uri, headers=[]):
        '''
        Method is used to set connection with server.
        '''
        try:
            self.ws.connect(uri, headers=headers)
        except:
            return False

        return True

    async def open(self, new_val: bool = None):
        '''
        Method returns the state of connection
        '''
        if new_val == False:
            self.ws.close()
            return False

        return self.ws.connected

    async def recv(self):
        '''
        Method read data from socket. All special packets are not returned.
        '''
        return self.ws.recv()

    async def send(self, buf):
        '''
        Method send data to server.
        '''
        return self.ws.send(buf)

#from websocket import create_connection

async def main():
    ws = TstWebSocket()
    await ws.handshake("ws://localhost:8002/5217670e-33e8-103c-9709-b9d40b7e922e")
    data = await ws.recv()
    print(data)
    await ws.open(False)

a.run(main())
