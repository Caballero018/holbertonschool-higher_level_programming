#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then save them to a file.
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
lo = load_from_json_file(filename)
ls = []
for i in range(1, len(sys.argv)):
    ls.append(sys.argv[i])
for re in lo:
    ls.append(re)
save_to_json_file(ls, filename)
