from my_exceptions import InvalidAction


class Validator:
    def validate_type(self, data, type_data):
        if not isinstance(data, type_data):
            raise TypeError('Неверный тип данных')

    def validate_action(self, action):
        if action not in ('+', '-', '/', '*'):
            raise InvalidAction


validator = Validator()
