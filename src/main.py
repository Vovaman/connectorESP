from machine import Pin
import uasyncio as a
#import uwebsockets
import json
import network
import time

from connector.ESPConnector import ESPConnector

LED_pin = Pin(2, Pin.OUT)

def flash_sos(str_to_print: str = None):
    def flash(on_ms: int, off_ms: int):
        LED_pin.on()
        time.sleep_ms(on_ms)
        LED_pin.off()
        time.sleep_ms(off_ms)
        
    flash(200, 100)
    flash(200, 100)
    flash(200, 100)
    flash(500, 100)
    flash(500, 100)
    flash(500, 100)
    
    if str_to_print is not None:
        print(str_to_print)


async def main():
    try:
        app = ESPConnector()
    except Exception as ex:
        print("Error while app initialization: {}.".format(ex))
        while True:
            flash_sos()
    
    count = 0

    try:
        await app.wifi_connect()
    except Exception as ex:
        print("Error while connecting to wi-fi: {}".format(ex))
        flash_sos()

    LED_pin.off()
    while True:
        try:
            await app.run()
        except Exception as ex:
            flash_sos(ex)
        
a.run(main())