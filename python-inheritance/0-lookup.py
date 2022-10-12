#!/usr/bin/python3
def lookup(obj):
    object_methods = [method_name for method_name in dir(obj)
                  if callable(getattr(obj, method_name))]
    return object_methods