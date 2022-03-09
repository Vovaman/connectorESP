class Error:
    def __init__(self, id, mes):
        self.id: int = id
        self.mes: str = mes

class Errors:
    CN_NO_CONF: Error = Error(1, "Не указан файл конфигурации")
    CN_WRONG_CONFIG: Error = Error(2, "Ошибка файла конфигурации")
