import json
def load_json():
    """
    load json file which is present in following path

    Returns:
        data: data present in json file
    """
    with open('./config.json','r') as file:
        data= json.load(file)
        return data