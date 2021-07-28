import json


json_file = './config.json'


class Config:
    def __init__(self):
        with open(json_file, encoding='utf-8') as f:
            self.__json = json.loads(f.read())

    @property
    def xpaths(self):
        return self.__json['xpaths']

    @property
    def chromedriver_path(self):
        return self.__json['chromedriver_path']

    @property
    def data_output_path(self):
        return self.__json['data_output_path']

    @property
    def browser_path(self):
        return self.__json['browser_path']
