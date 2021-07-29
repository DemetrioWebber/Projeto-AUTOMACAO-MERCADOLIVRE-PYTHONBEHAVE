import json
from os.path import dirname, realpath, isfile

class Json():

    def __init__(self, context):
        pass

    def retornarJson(self, arquivo):
        with open("features/fixtures/{}".format(arquivo)) as data_teste:
            data = json.load(data_teste)
            return data
    
    def transformarJson(self, context, string):
        objetoJson = json.loads(string)

        return objetoJson