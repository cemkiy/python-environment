import os

class env:
    def __init__(self):
        self.enviroment_dict = {}
        content = [line.rstrip('\n') for line in open('.env')]
        for variable_line in content:
            try:
                self.enviroment_dict[variable_line.split('=')[0]] = variable_line.split('=')[1]
            except Exception as e:
                raise ValueError("environment variable format error")

    def set_dict_to_env(self, enviroment_dict=None):
        to_be_set_dict = enviroment_dict
        if to_be_set_dict==None:
            to_be_set_dict = self.enviroment_dict
        for key,value in to_be_set_dict.items():
            try:
                os.environ[key] = str(value)
                self.enviroment_dict[key] = value
            except:
                raise TypeError("dictionary values must be string or convertable string")

    def set_variables_to_env(self, variables_dict):
        for key,value in variables_dict.items():
            try:
                os.environ[key] = str(value)
                self.enviroment_dict[key] = value
            except:
                raise TypeError("dictionary values must be string or convertable string")

    def set_variable_to_env(self, key, value):
        try:
            os.environ[key] = str(value)
            self.enviroment_dict[key] = value
        except:
            raise TypeError("dictionary values must be string or convertable string")
