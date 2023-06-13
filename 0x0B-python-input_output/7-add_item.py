#!/usr/bin/python3
"""This module adds all arguments to a Python list,
and then save them to a file
"""


import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

argues = sys.argv

if not os.path.exists('add_item.json'):
    with open('add_item.json', 'w', encoding='utf-8') as fls:
        fls.write('[]')

obj = load_from_json_file('add_item.json')
for argue in argues[1:]:
    obj.append(argue)
save_to_json_file(obj, 'add_item.json')
