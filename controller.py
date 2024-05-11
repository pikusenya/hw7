from validator import validator

class Controller:
    def calc_sum(self, a, b):
        return a + b
    def calc_diff(self, a, b):
        return a - b
    def calc_mult(self, a, b):
        return a * b
    def calc_div(self, a, b):
        return a / b

    def calculate(self, data):
        error = validator.val_calculate(data)
        if error:
            return error

        a, b, action = data.values()

        if action == "+":
            return str(controller.calc_sum(a, b))
        elif action == "-":
            return str(controller.calc_diff(a, b))
        elif action == "*":
            return str(controller.calc_mult(a, b))
        elif action == "/":
            return str(controller.calc_div(a, b))

    def text_upper(self, text):
        return text.upper()
    def text_lower(self, text):
        return text.lower()
    def text_trim(self, text):
        return text.strip()
    def text_alter(self, text):
        return text[::-1]

    def text_editor(self, data):
        error = validator.val_text_editor(data)
        if error:
            return error

        text, action = data.values()

        if action == "upper":
            return controller.text_upper(str(text))
        elif action == "lower":
            return controller.text_lower(str(text))
        elif action == "trim":
            return controller.text_trim(str(text))
        elif action == "alter":
            return controller.text_alter(str(text))

    def text_email(self, text):
        pass
    def text_number(self, text):
        pass
    def parser(self, data):
        error = validator.val_parser(data)
        if error:
            return error

        text, action = data.values()

        if action == "email":
            return controller.text_email(str(text))
        if action == "number":
            return controller.text_number(str(text))


controller = Controller()
