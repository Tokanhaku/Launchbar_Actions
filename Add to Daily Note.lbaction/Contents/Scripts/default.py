#!/usr/bin/env python
# coding=utf-8
# LaunchBar Action Script
#
import sys
import os
import datetime


now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
notepath = "~/Desktop/Note@"+today+".md"
notepath = os.path.expanduser(notepath)
file = open(notepath, "a") 
for arg in sys.argv[1:]: 
    file.write(arg+"\n\n\n") 
file.close() 