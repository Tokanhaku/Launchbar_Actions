#!/usr/local/anaconda3/bin/python3
#
# LaunchBar Action Script
#
import sys
import json
import os
from urllib.request import urlopen
from urllib.parse import quote
import re
from bs4 import BeautifulSoup


def search_youtube(arg):
    api = open("api", "r") 
    api = api.readline()
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q="+quote(arg)+"&key="+api+"&type=video"
    # try:
    content = json.loads(urlopen(url).read().decode('utf-8'))
    result = []
    for vid in content['items']:
        item = {}
        item["url"]   = "https://youtu.be/"+vid['id']['videoId']
        item["title"] = vid['snippet']['title']
        item["description"] = vid['snippet']['description']
        item["day"]   = vid['snippet']['publishedAt'][:10]
        item["pic"]   = vid['snippet']['thumbnails']['default']['url']
        item["picname"] = "../Resources/"+vid['id']['videoId']+'.jpg'
        f = urlopen(item["pic"])
        with open(item["picname"], "wb") as code:
            code.write(f.read())
        result.append(item)
    return result

if __name__ == '__main__':
    items = []
    for arg in sys.argv[1:]:
        try:
            vids = search_youtube(arg)
            for vid in vids:
                item = {}
                item["title"] = vid["title"]
                item["subtitle"] = vid["day"] + " | " + vid["url"]
                item["icon"] = vid["picname"][13:]
                item['action'] = "open.py"
                item['actionArgument'] = {"vid_url": "iina://weblink?url="+vid["url"]}
                item['actionRunsInBackground'] = True
                items.append(item)
        except:
            item = {}
            item["title"] = "Error!"
            item["icon"] = "font-awesome:fa-exclamation-triangle"
            items.append(item)
    print(json.dumps(items))