#!/usr/bin/python3
"doc"


def inherits_from(obj, a_class):
    "doc"
    try:
        if (obj or type(obj) is not a_class) and (not obj or issubclass(obj, a_class)):
            return True
        else:
            return False
    except TypeError:
            return True
