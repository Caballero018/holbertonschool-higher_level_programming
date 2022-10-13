#!/usr/bin/python3
"doc"


def inherits_from(obj, a_class):
    "doc"
    try:
        if issubclass(obj, a_class):
            return True
        elif isinstance(obj, a_class):
            return False
        else:
            return False
    except TypeError:
            return True
