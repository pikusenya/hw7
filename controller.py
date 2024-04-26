from model import model
from validator import validator
from my_exceptions import InvalidAction

class Controller:
    def get_json_data(self, operation):
        data = model.get_data_from_file('data.json')
        return data[operation]

    def validation(self, data):
        try:
            validator.validate_type(data, dict)
        except TypeError:
            return 'Неверный тип данных, передайте данные в словаре,' \
                   'для более детальной информации обратитесь к запросу "/help"'
        try:
            validator.validate_action(data["action"])
        except InvalidAction as error:
            return error.TEXT_EXCEPTION

    def sum(self, a, b):
        return a + b

    def diff(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def calculate(self, data):
        error = controller.validation(data)
        if error:
            return error

        a, b, action = data.values()

        if action == "+":
            return str(controller.sum(a, b))
        elif action == "-":
            return str(controller.diff(a, b))
        elif action == "*":
            return str(controller.mult(a, b))
        elif action == "/":
            return str(controller.div(a, b))

controller = Controller()
