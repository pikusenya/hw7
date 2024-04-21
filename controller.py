from model import model

class Controller:
    def get_json_data(self):
        data = model.get_data_from_file("data.json")
        return data

controller = Controller()
