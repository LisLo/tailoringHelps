import os
from Source.Config.read_json import ReadJson


class GetInput():
    def __init__(self, main_code_path):
        self.main_code_path = main_code_path
        self.__read_input_parameters()

    def __read_input_parameters(self):
        root_path = os.path.dirname(self.main_code_path)
        inputs = ReadJson.read_json_parameters(root_path)
        for key, value in inputs.items():
            setattr(self, key, value)
