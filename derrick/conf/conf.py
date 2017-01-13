import simplejson as json


class Configuration:
    path = ""

    def __init__(self):
        pass

    def Load(self):
        with open(self.path) as jsonData:
            data = json.load(jsonData)
            return data
