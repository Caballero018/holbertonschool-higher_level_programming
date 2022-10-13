#!/usr/bin/python3
"doc"


def inherits_from(obj, a_class):
    "doc"
    try:
        if issubclass(obj, a_class):
            return True
        if isinstance(obj, a_class):
            return False
        return False
    except TypeError:
            return True
