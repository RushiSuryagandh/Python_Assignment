import json
import logging


def load_config():
    """ loads the configuration file

    Returns:
        dictionary: Return the data present in config file if exists else return none
    """
    try:
        with open(f'./tasks_download/config.json', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        logging.error("Config file not found.")
        return None