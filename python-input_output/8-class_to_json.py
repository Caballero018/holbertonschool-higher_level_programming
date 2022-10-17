#!/usr/bin/python3
"""
Module tha have function that returns the dictionary description with simple data 
structure (list, dictionary, string, integer and boolean) for JSON serialization 
of an object:
"""
import json


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data structure (list, 
    dictionary, string, integer and boolean) for JSON serialization of an object:
    """
    return json.loads(obj)
