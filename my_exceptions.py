class InvalidAction(Exception):
    TEXT_EXCEPTION = 'Не удалось определить тип операции. Ознакомиться с доступными операциями можно по запросу "/help"'

class InvalidType(Exception):
    TEXT_EXCEPTION = 'Неверный тип данных. Ознакомиться с доступными типами данных можно по запросу "/help"'

class InvalidKey(Exception):
    TEXT_EXCEPTION = 'Неверный ключ в словаре. Ознакомиться с доступным форматом данных можно по запросу "/help"'