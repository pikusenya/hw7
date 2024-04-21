import json


class Model:
    def get_data_from_file(self, data):
        with open(data, 'r') as file:
            return json.loads(file.read())

model = Model()
