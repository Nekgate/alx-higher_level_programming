#!/usr/bin/python3
"""
from_json_string(my_str) function
"""

import json


def from_json_string(my_str):
    """returns an object representation by JSON (string)"""
    return json.loads(my_str)
