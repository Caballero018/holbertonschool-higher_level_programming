#!/usr/bin/python3
"Module that function that returns an object (Python data structure) \
represented by a JSON string"
import json


def from_json_string(my_str):
    "Function that returns an object (Python data structure) \
    represented by a JSON string"
    return json.dumps(my_str)
