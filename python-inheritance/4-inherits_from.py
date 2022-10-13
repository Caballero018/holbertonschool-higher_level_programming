#!/usr/bin/python3
"doc"


def inherits_from(obj, a_class):
    "doc"
    try:
        if type(obj) is not a_class or issubclass(obj, a_class):
            return True
        else:
            return False
    except TypeError:
            return True
