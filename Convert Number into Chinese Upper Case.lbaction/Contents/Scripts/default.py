#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# LaunchBar Action Script
#
import sys
sys.dont_write_bytecode = True
import json
import os
my_env = os.environ.copy()
import subprocess as sp

from cnumber import cnumber

items = []

item = {}

pt = cnumber()
# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    item = {}
    try:
        arg = pt.cwchange(arg)
        item['title'] = arg
        item['icon']  = "yen-sign-solid-Template.png"
        title = "大写数字已复制"
        my_command = ["osascript", "./notification.applescript", title, arg]
    except:
        pass
        item['title'] = "请输入正确的阿拉伯数字！"
        item['icon']  = "font-awesome:fa-times"
        my_command = ["osascript", "./notification.applescript", item['title'], ""]

    items.append(item)

print json.dumps(items)

sp.check_output(my_command, env=my_env)