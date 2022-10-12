#!/usr/bin/python3
"Doc"


def lookup(obj):
    "Doc"
    object_methods = [method_name for method_name in dir(obj)
                  if callable(getattr(obj, method_name))]
    return object_methods