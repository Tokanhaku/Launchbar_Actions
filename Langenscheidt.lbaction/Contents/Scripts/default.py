#!/usr/local/anaconda3/bin/python3
#
# LaunchBar Action Script
#
import sys
import json

from urllib.request import urlopen
from urllib.parse import quote
import re
from bs4 import BeautifulSoup

def langenscheidt(arg,items):
    arg = quote(arg)
    arg = arg.replace("%C3%B6","oe")
    arg = arg.replace("%C3%A4","ae")
    arg = arg.replace("%C3%BC","ue")
    arg = arg.replace("%C3%9F","ss")
    url = "https://de.langenscheidt.com/deutsch-chinesisch/"+ arg
    # print(url)
    html = urlopen(url).read().decode('utf-8')
    # print("https://de.langenscheidt.com/deutsch-chinesisch/"+ quote(arg.replace("ö","oe").replace("ä","ae").replace("ü","ue").replace("ß","ss")))
    html = BeautifulSoup(html,features="lxml")
    try:
        for bedeutung in html.find_all(attrs={"class":"lemma-entry translation"}):
            left  = bedeutung.find(attrs={"class":"col1"})
            left  = left.find(attrs={"class":"trans"})
            left  = left.span.string

            right = bedeutung.find(attrs={"class":"col2"})
            right1 = right.find(attrs={"class":"lemma-pieces"})
            right1 = right1.string
            try: 
                right2 = right.find(attrs={"class":"ind-pieces"})
                right2 = right2.string
                right = right1 + " (" + right2 + ")"
            except:
                right = right1
            item = {}
            item["title"] = right
            item["subtitle"] = "释义："+left
            item["icon"] = "langenscheidt.jpg"
            items.append(item)
    except:
        pass

    try:
        for bsp in html.find_all(attrs={"class":"lemma-example"}):
            left  = bsp.find(attrs={"class":"col1"})
            left  = left.find(attrs={"class":"trans"})
            left  = left.span.string
            right = bsp.find_all(attrs={"class":"col2"})[0]
            right = right.span.strings
            y = ""
            for x in right:
                y += x
            right = y

            item = {}
            item["title"] = right
            item["subtitle"] = "示例："+left
            item["icon"] = "langenscheidt.jpg"
            items.append(item)

    except:
        pass

    try:
        more_example = html.find(attrs={"class":"more example"})
        for bsp in more_example.find_all(attrs={"class":"additional-entry"}):
            left  = bsp.find(attrs={"class":"col1"})
            left  = left.find(attrs={"class":"trans"})
            left  = left.span.string

            right = bsp.find_all(attrs={"class":"col2"})[0]
            right = right.span.strings
            y = ""
            for x in right:
                y += x
            right = y

            item = {}
            item["title"] = right
            item["subtitle"] = "示例："+left
            item["icon"] = "langenscheidt.jpg"
            items.append(item)
    except:
        pass
    # url = html.find(attrs={"rel":"alternate","hreflang":"de"})
    # url = "https:"+re.findall(r'<link href="(.+?)"', str(url), flags=re.DOTALL)[0]
    # return url



items = []
# langenscheidt("ä ü ß",items)

# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    try:
        langenscheidt(arg,items)
    except:
        pass
if len(items) == 0:
    item = {}
    item["title"] = "Nix gefunden."
    item["icon"] = "frown-Template.png"
    items.append(item)
# else:
#     item = {}
#     item["title"] = url
#     # <link rel="alternate" hreflang="de" href="//de.langenscheidt.com/deutsch-chinesisch/aufnehmen" />

#     item["subtitle"] = "打开网页"
#     item["icon"] = "langenscheidt.jpg"
#     items.append(item)
print(json.dumps(items))



