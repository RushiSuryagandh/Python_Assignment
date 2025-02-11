import json
import logging

def load_config(filename="config.json"):
    """
    Loads configuration data from a JSON file.

    Args:
        filename (str): The path to the JSON file to load. Defaults to "config.json".

    Returns:
        dict: The configuration data loaded from the JSON file, or None if an error occurs.
    """
    try:
        with open(filename, 'r') as file:
            config = json.load(file)
        return config
    except Exception as e:
        logging.error(f"Error loading config file: {e}")
        return None
