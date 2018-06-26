#!/usr/local/anaconda3/bin/python
#
# LaunchBar Action Script
#
import sys
import json
import os
import lproj_name
import subprocess as sp

def open(app):
    my_env = os.environ.copy()
    my_command = ["open", app]
    sp.check_output(my_command, env=my_env)

items = []

# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    resource_path = arg + "/Contents/Resources"
    files = os.listdir(resource_path)
    for file in files:
        if file[-6:] == ".lproj":
            point_postion = file.rfind("/")
            file_name = file[point_postion+1:-6]
            item = {}
            if file_name in lproj_name.name:
                item['title'] = lproj_name.name[file_name]["language"]
                item['icon']  = lproj_name.name[file_name]["flag"]
            elif file_name == "Base":
                item['title'] = "Default"
                item['icon']  = "font-awesome:fa-flag"
            else:
                item['title'] = file_name
                item['icon']  = "font-awesome:fa-flag"
            item['action'] = "open.py"
            item['actionArgument'] = {"app":arg,"language":file_name}
            item['actionRunsInBackground'] = True
            items.append(item)
print(json.dumps(items))
