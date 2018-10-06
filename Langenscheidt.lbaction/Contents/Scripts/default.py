#!/usr/local/anaconda3/bin/python
#
# LaunchBar Action Script
#
import sys
import json

from urllib.request import urlopen
import re

items = []

# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    html = urlopen(
        "https://de.langenscheidt.com/deutsch-chinesisch/"+arg
        ).read().decode('utf-8')
    html = re.findall(r'Beispielsätze für(.+?)Synonyme für',html)
    if len(html)!=0:
        html = html[0]
        res = re.findall(r'<div class="text-to-speech" data-text="(.+?)" data-hash', html, flags=re.DOTALL)
        dict = {}
        for i in range(0,len(res),2):
            dict[res[i]] = res[i+1]
            item = {}
            item["title"] = res[i] + "\n" + res[i+1]
            item["icon"] = "comment-dots-Template.png"
            items.append(item)
    else:
        item = {}
        item["title"] = "Keinen Beispielsatz gefunden."
        item["icon"] = "frown-Template.png"
        items.append(item)
print(json.dumps(items))

    # resource_path = arg + "/Contents/Resources"
    # files = os.listdir(resource_path)
    # for file in files:
    #     if file[-6:] == ".lproj":
    #         point_postion = file.rfind("/")
    #         file_name = file[point_postion+1:-6]
    #         item = {}
    #         if file_name in lproj_name.name:
    #             item['title'] = lproj_name.name[file_name]["language"]
    #             item['icon']  = lproj_name.name[file_name]["flag"]
    #         elif file_name == "Base":
    #             item['title'] = "Default"
    #             item['icon']  = "font-awesome:fa-flag"
    #         else:
    #             item['title'] = file_name
    #             item['icon']  = "font-awesome:fa-flag"
    #         item['action'] = "open.py"
    #         item['actionArgument'] = {"app":arg,"language":file_name}
    #         item['actionRunsInBackground'] = True
    #         items.append(item)
