#!/usr/bin/env python

import yaml
import json
from pprint import pprint as pp

l = [
    1,
    "two",
    {"key1": "value1", 
     "key2": "value2"}
    ]

"""
YAML/JSON
6. Write a Python program that creates a list. One of the elements of the list should be a i
dictionary with at least two keys. Write this list out to a file using both YAML and JSON formats.
The YAML file should be in the expanded form.
"""

with open("yaml_file.txt", "w") as f:
    f.write(yaml.dump(l, default_flow_style=False))

with open("json_file.txt", "w") as f:
    json.dump(l, f)

"""
7. Write a Python program that reads both the YAML file and the JSON file created in exercise6 
and pretty prints the data structure that is returned.
"""

# Read back yaml file
print "Pretty-print yaml output"
print "------------------------"
with open("yaml_file.txt", "r") as f:
    new_list =  yaml.load(f)
    pp(new_list)


# Read back json file
print "\nPretty-print json output"
print "------------------------"
with open("json_file.txt", "r") as f:
    new_list =  json.load(f)
    pp(new_list)


