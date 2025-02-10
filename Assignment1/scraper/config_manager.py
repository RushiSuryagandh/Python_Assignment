# Load config files
import json
def load_json():
    with open('./config.json', 'r') as file:
        data = json.load(file)
    return data