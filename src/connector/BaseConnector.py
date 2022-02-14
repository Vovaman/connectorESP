# базовый коннектор для платформы Пересвет
# реализует логику, общую для всех коннекторов
class BaseConnector:

    def __init__(self, config: dict = None):
        self._connected = False
        if config is None:
            return

        self._connected = self._connect(config["id"], config["server"])
        self._parse_config(config)

    def _connect(id, )


        
