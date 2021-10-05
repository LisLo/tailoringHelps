import json
import os
import sys


class ReadJson():
    def read_json_parameters(root_path):
        json_path = os.path.join(root_path, "Input", "config.json")
        if os.path.isfile(json_path):
            # Sonderzeichen koennen eingelesen werden
            with open(json_path, encoding = "utf-8") as json_path:
                inputs = json.load(json_path)
                return inputs
        else:
            sys.exit("No Config.json found")
