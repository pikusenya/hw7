from my_exceptions import InvalidAction


class Validator:
    def validate_type(self, data, type_data):
        if not isinstance(data, type_data):
            print("error type")
            raise TypeError('Неверный тип данных')

    def validate_action(self, action):
        if action not in ('+', '-', '/', '*'):
            print("error action")
            raise InvalidAction


validator = Validator()
