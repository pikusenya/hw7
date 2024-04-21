from model import model


class Controller:
    def get_json_data(self):
        data = model.get_data_from_file()
        return data["arg1"]

    def sum(self, a, b):
        return a+b


controller = Controller()


