from bin import bot
import json


class Data(bot):
    def __init__(self, DataPath):
        self.DataPath = DataPath
        self.load()
        self.__sep = ','

    DataPath = "data.json"
    DataMSG = []

    def load(self):
        with open(str(self.DataPath), "r") as file:
            for i in json.loads(file):
                self.DataMSG.append(i['Data'] + self.__sep.rstrip())






