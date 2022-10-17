#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then save them to a file.
"""
import os
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
ls = []
for i in range(1, len(sys.argv)):
    ls.append(sys.argv[i])
if os.path.isfile(filename) and not os.stat(filename).st_size == 0:
    lis = load_from_json_file(filename) + ls
    save_to_json_file(lis, filename)
else:
    save_to_json_file(ls, filename)
