import simplejson as json
import os 

class Configuration:
    path = ""

    def __init__(self):
        pass

    def detect_config_path(self):
        if not os.path.exists(self.path):
            file(self.path, "w").close()

    def Load(self):
        with open(self.path) as jsonData:
            data = json.load(jsonData)
            return data
