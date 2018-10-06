#!/usr/local/anaconda3/bin/python3
#
# LaunchBar Action Script
#
import sys
import json

from urllib.request import urlopen
from urllib.parse import quote
import re

def duden(arg, items):
    from bs4 import BeautifulSoup
    html = urlopen(
        "https://www.duden.de/rechtschreibung/"+ arg.lower()
        ).read().decode('utf-8')
    if len(html)!=0:
        html = re.findall(r'<h2>Bedeutungen, Beispiele und Wendungen</h2>(.+?)<h2>Blättern</h2>', html, flags=re.DOTALL)
        html = html[0]
        html = re.findall(r'<li id="Bedeut(.+?)</li>', html, flags=re.DOTALL)
        for x in html:
            index = re.findall(r'ung(.+?)"> ', x, flags=re.DOTALL)
            dfn = re.findall(r'"> (.+?)<section class="term-section">', x, flags=re.DOTALL)
            if len(dfn) != 0:
                item_dfn = {}
                item_dfn["title"] = BeautifulSoup(dfn[0],features="lxml").text.replace(";","\n")
                item_dfn["icon"] = "Duden@2x.png"
                item_dfn["subtitle"] = "Duden | Definition " + index[0]
                items.append(item_dfn)
                
            bsps = re.findall(r'<h3>Beispiele</h3><ul><li><span><span>(.+?)</span></span>', x, flags=re.DOTALL)
            if len(bsps) != 0:
                for bsp in bsps:
                    item_bsp = {}
                    item_bsp["title"] = BeautifulSoup(bsp, features="lxml").text
                    item_bsp["icon"] = "Duden@2x.png"
                    item_bsp["subtitle"] = "Duden | Beispiel " + index[0]
                    items.append(item_bsp)

def langenscheidt(arg,items):
    html = urlopen(
        "https://de.langenscheidt.com/deutsch-chinesisch/"+ quote(arg.lower())
        ).read().decode('utf-8')

    bedeutung = re.findall(r'<span class="ind">(.+?)</span>', html, flags=re.DOTALL)
    bedeut = []
    for i in range(len(bedeutung)):
        if i%2 == 0:
            bedeut = bedeut+[bedeutung[i]]
    #print(bedeut)
    #html = re.findall(r'<span class="ind-pieces"><span class="ind">(.+?)</span></span>', html, flags=re.DOTALL)
    #for html

    if len(html)!=0:
        #html = html[0]
        res = re.findall(r'<div class="text-to-speech" data-text="(.+?)" data-hash', html, flags=re.DOTALL)
        bedeutung = re.findall(r'<span class="ind">(.+?)</span>', html, flags=re.DOTALL)
        dict = {}
        for i in range(0,len(res),2):
            dict[res[i]] = res[i+1]
            item = {}
            item["title"] = res[i] + "\n" + res[i+1]
            item["subtitle"] = "Langenscheidt"
            item["icon"] = "langenscheidt.jpg"
            items.append(item)


items = []
# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    try:
        langenscheidt(arg,items)
    except:
        pass

    try:
        duden(arg, items)
    except:
        try:
            duden(arg.capitalize(),items)
        except:
            pass
    
    if len(items) == 0:
        item = {}
        item["title"] = "Nix gefunden."
        item["icon"] = "frown-Template.png"
        items.append(item)
print(json.dumps(items))



