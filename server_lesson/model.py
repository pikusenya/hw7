import json


class Model:
    def get_data_from_file(self):
        with open("test.json", "r") as file:
            return json.loads(file.read())


model = Model()
