#!/usr/bin/python3
"doc"


def inherits_from(obj, a_class):
    "doc"
    try:
        if isinstance(obj, a_class):
            return False
        if issubclass(obj, a_class):
            return True
    except TypeError:
            return True
