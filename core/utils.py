# Utility/helper functions

import json

def read_json(file_path):
    
    with open(file_path) as file:
        return json.load(file)
