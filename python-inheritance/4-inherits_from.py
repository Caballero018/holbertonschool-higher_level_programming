#!/usr/bin/python3
"doc"


def inherits_from(obj, a_class):
    "doc"
    try:
        if not obj and issubclass(obj, a_class):
            return True
        if not obj:
            return False
        if obj and type(obj) is not a_class and issubclass(obj, a_class):
            return True
        if type(obj) is not a_class:
            return False
        else:
            return False
    except TypeError:
            return True
