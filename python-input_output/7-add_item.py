#!/usr/bin/python3
"Script that adds all arguments to a Python list, and then save them to a file"


from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

ls = []
filename = "add_item.json"
for i in range(1, len(argv)):
    ls.append(argv[i])

for re in load_from_json_file(filename):
    ls.append(re)
save_to_json_file(ls, filename)
