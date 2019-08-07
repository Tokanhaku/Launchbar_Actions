#!/usr/local/anaconda3/bin/python3
#
# LaunchBar Action Script
#

from urllib.request import urlopen
from bs4 import BeautifulSoup
#from urllib.parse import quote
#import re

def GetURLTitle(url):

    html_contents = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html_contents,features="lxml")
    treffer = soup.find("title")
    title = treffer.renderContents().decode("utf-8").strip()
    return title

if __name__ == '__main__':
    url = "https://sspai.com"
    if url[:4] == "http":
        print(GetURLTitle(url))