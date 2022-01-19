import network
import json
import time
import uasyncio as a

class ESPConnector:

    def __init__ (self):
        f = open('../config.json')
        c = f.read()
        f.close()
        self.config = json.loads(c)
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        
    async def wifi_connect(self, attempts: int = 3):
        
        self.wlan.scan()
        if not self.wlan.isconnected():
            print('Connecting to network. Will try {} time(s)...'.format(attempts))

            count = 1
            while not self.wlan.isconnected() and count <= attempts:
                print("Attempt {}...".format(count))
                self.wlan.connect(self.config['SSID'], self.config['password'])
                await a.sleep_ms(1000)
                count += 1
        
        if self.wlan.isconnected():
            print('network config:', self.wlan.ifconfig())

    async def control_loop(self):
        await a.sleep_ms(1000)
        if self.wlan.isconnected():
            c = "c"
        else:
            c = "."
        print(c, end='')
    
    async def run(self):
        if not self.wlan.isconnected():
            await self.wifi_connect(attempts=1)

        await self.control_loop()