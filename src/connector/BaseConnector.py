# базовый коннектор для платформы Пересвет
# реализует логику, общую для всех коннекторов
import json
from .consts import Errors

'''
async def read_loop():
    global config
    global lock
    global data_from_ws

    # may be, it
    wifi = await wifi_connect(config["wifi"]["SSID"], config["wifi"]["password"])
    while True:
        gc.collect()
        if not wifi.isconnected():
            wifi = await wifi_connect(config["wifi"]["SSID"], config["wifi"]["password"])
            if not wifi.isconnected():
                continue
        try:
            # connect to test socket server with random client number
            if not await ws.handshake("{}{}".format(config["server"], randint(1, 100))):
                raise Exception('Handshake error.')
            while await ws.open():
                data = await ws.recv()
                if data is not None:
                    await lock.acquire()
                    data_from_ws.append(data)
                    lock.release()
                await a.sleep_ms(50)
        except Exception as ex:
            print("Exception: {}".format(ex))
            await a.sleep(1)
# ------------------------------------------------------
'''

class BaseConnector:

    def __init__(self):
        '''
        Constructor can't be awaitable.
        Thus it is necessary to call `init` method after BaseConnector instantiating.
        '''
        self._connected = False

    async def _connect(self) -> bool:
        '''
        Method connects to platform using websocket.
        '''
        if not self._ws.handshake(
            "{}{}".format(self._conf["server"], self._conf["id"])):
            return False

        data = self._ws.recv()
        print("{}".format(data))


    async def init(self, config: str='config.json', ws=None) -> bool:
        if config is None:
            await self.send_error(Errors.CN_NO_CONFIG)
            return False

        try:
            f = open(config)
            self._conf = json.load(f)
        except:
            await self.send_error(Errors.CN_WRONG_CONFIG)

            return False
        f.close()

        self._ws = ws

        self._connected = self._connect()
        #self._parse_config(config)

    async def send_error(error: dict):
        '''
        Метод вывода данных об ошибке.
        В обычном коннекторе - лог, на контроллере, скорее всего - вывод в консоль и моргание LED'ом.
        '''
        pass
