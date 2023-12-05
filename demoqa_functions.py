import requests
import json
# from user_funcs import User
# from bookstore_funcs import Bookstore


def extract_key_value(json_data, key):
    """Extracts a specific key-value pair from a JSON data"""
    data = json.loads(json_data)
    value = data.get(key)
    return value


