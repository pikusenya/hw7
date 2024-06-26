class InvalidAction(Exception):
    TEXT_EXCEPTION = 'Не удалось определить тип операции. Ознакомиться с доступными операциями можно по запросу "/helpme"'

class InvalidType(Exception):
    TEXT_EXCEPTION = 'Неверный тип данных. Ознакомиться с доступными типами данных можно по запросу "/helpme"'

class InvalidKey(Exception):
    TEXT_EXCEPTION = 'Неверный ключ в словаре. Ознакомиться с доступным форматом данных можно по запросу "/helpme"'