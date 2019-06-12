#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import json
import subprocess as sp
import os

my_env = os.environ.copy()

items = []

# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    my_command = ["mdfind", arg]
    files = sp.check_output(my_command, env=my_env)
    files = str(files).split("\n")
    if files[0] == "":
        item = {}
        item['title'] = "No result!"
        item['icon']  = "grin-beam-sweat-Template"
        items.append(item)
    else:
        for file in files:
            item = {}
            item['path'] = file
            items.append(item)

print json.dumps(items)