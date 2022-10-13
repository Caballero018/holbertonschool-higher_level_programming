#!/usr/bin/python3
"doc"


def inherits_from(obj, a_class):
    "doc"
    try:
        if not obj and ((issubclass(obj, a_class) or isinstance(obj, a_class)) or (not issubclass(obj, a_class) or not isinstance(obj, a_class))):
            return False
        if obj and type(obj) is a_class and not issubclass(obj, a_class):
            return False
        else:
            return True
    except TypeError:
            return True
