#!/usr/bin/python3
"doc"


def inherits_from(obj, a_class):
    "doc"
    if obj:
        return True
    try:
        if obj and type(obj) is not a_class and issubclass(obj, a_class):
            return True
        else:
            return False
    except TypeError:
            return True
