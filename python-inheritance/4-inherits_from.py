#!/usr/bin/python3
"doc"


def inherits_from(obj, a_class):
    "doc"
    try:
        if not obj and type(obj) is not object:
            return True
        if not obj and not issubclass(obj, a_class):
            return False
        if obj and type(obj) is not a_class and not issubclass(obj, a_class):
            return True
        if type(obj) is not a_class:
            return False
        else:
            return False
    except TypeError:
            return False
