#!/usr/bin/python3
"Module that have a function that creates an Object from a “JSON file”"
import json


def load_from_json_file(filename):
    "Function that creates an Object from a “JSON file”"
    with open(filename, mode="r") as f:
        data = json.load(f)
