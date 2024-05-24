from my_exceptions import InvalidAction, InvalidKey, InvalidType


class Validator:
    def validate_type(self, data: dict, type_data: type):
        """
        Метод проверяет соответствие данных передаваемому типу данных
        Args:
            словарь с данными, тип данных
        Raise:
            ошибка, если тип переданных данных не совпадает с переданным типом данных
        """
        if not isinstance(data, type_data):
            raise InvalidType

    def validate_action(self, action: str, action_list: tuple):
        """
        Метод проверяет соответствие операции передаваемому списку операций
        Args:
            значение словаря в виде строки (выбранная операция), кортеж операций
        Raise:
            ошибка, если переданная операция не находится в списке
        """
        if action not in action_list:
            raise InvalidAction

    def validate_keys(self, data: dict, keys: list):
        """
        Метод проверяет соответствие ключа передаваемому списку ключей
        Args:
            словарь с данными, список ключей к словарю
        Raise:
            ошибка, если ключи в переданном словаре не совпадают со списком ключей
        """
        for key in data.keys():
            if key not in keys:
                raise InvalidKey

    def val_calculate(self, data: dict) -> str:
        """
        Метод проверяет соответствие данных для выполнения математических операций
        Args:
            словарь с данными
        Raise:
            описание найденной ошибки
        """
        try:
            self.validate_type(data, dict)
            self.validate_type(data["a"], (int, float))
            self.validate_type(data["b"], (int, float))
            self.validate_action(data["action"], ('+', '-', '/', '*'))
            self.validate_keys(data, ["a", "b", "action"])
        except (InvalidType, InvalidAction, InvalidKey) as error:
            return error.TEXT_EXCEPTION

    def val_text_editor(self, data: dict) -> str:
        """
        Метод проверяет соответствие данных для выполнения преобразований текста
        Args:
            словарь с данными
        Raise:
            описание найденной ошибки
        """
        try:
            self.validate_type(data, dict)
            self.validate_action(data["action"], ("upper", "lower", "trim", "alter"))
            self.validate_keys(data, ["text", "action"])
        except (InvalidType, InvalidAction, InvalidKey) as error:
            return error.TEXT_EXCEPTION

    def val_parser(self, data: dict) -> str:
        """
        Метод проверяет соответствие данных для парсинга текста
        Args:
            словарь с данными
        Raise:
           описание найденной ошибки
        """
        try:
            self.validate_type(data, dict)
            self.validate_action(data["action"], ("email", "number"))
            self.validate_keys(data, ["text", "action"])
        except (InvalidType, InvalidAction, InvalidKey) as error:
            return error.TEXT_EXCEPTION


validator = Validator()
