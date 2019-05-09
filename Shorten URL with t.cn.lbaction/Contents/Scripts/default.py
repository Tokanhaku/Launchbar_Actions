#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys, urllib2
import subprocess as sp
import os
import json

tcn_url = "http://api.weibo.com/2/short_url/shorten.json?source=2849184197&url_long="

items = []
item = {}

# Note: The first argument is the script's path
arg = sys.argv[1:][0]
if arg[:8] != "https://" or arg[:7] != "http://":
    arg = "https://"+arg
tcn_url += arg
req = urllib2.Request(tcn_url)
response = urllib2.urlopen(req)
the_page = response.read().replace("\n","").replace("true","True")
the_page = eval(the_page)
short_url = the_page["urls"][0]["url_short"].replace("http://","")

my_command = ["osascript", "./notification.applescript", short_url]
my_env = os.environ.copy()
sp.check_output(my_command, env=my_env)
#     item = {}
#     item['title'] = short_url
#     item['icon'] = "font-awesome:fa-link"
#     items.append(item)
# print json.dumps(items)