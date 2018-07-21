#!/usr/local/anaconda3/bin/python
#
# LaunchBar Action Script
#
# Required Software: /Applications/calibre.app

import sys
import subprocess as sp
import os
from new_file import lb_notification

my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]


# Note: The first argument is the script's path
for arg in sys.argv[1:]:
# 0. set new file name
    point_postion = arg.rfind("/")
    path = arg[:point_postion+1]
    #
    my_command = ["exiftool", arg, "-BookName"]
    title = sp.check_output(my_command, env=my_env)
    title = str(title, "utf-8")
    point_postion = title.find(":")
    title = title[point_postion+1:].strip()
    
    my_command = ["exiftool", arg, "-Author"]
    author = sp.check_output(my_command, env=my_env)
    author = str(author, "utf-8")
    point_postion = author.find(":")
    author = author[point_postion+1:].strip()
    
    new_file = path + title + " (" + author + ").azw3"
# 1. /Applications/calibre.app/Contents/MacOS/ebook-convert /path/to/input.azw3 temp.htmlz --extra-css KindleFonts.css
    my_command = ["/Applications/calibre.app/Contents/MacOS/ebook-convert", \
                  arg, \
                  "temp.htmlz", \
                  "--extra-css", "KindleFonts.css"]
    sp.check_output(my_command, env=my_env)
# 2. zip -urj0 ~/Desktop/temp.htmlz /Users/Huanbo/Downloads/KindleFonts
    my_command = ["zip", "-urj0", "temp.htmlz", "Fonts"]
    sp.check_output(my_command, env=my_env)
# 3. /Applications/calibre.app/Contents/MacOS/ebook-convert temp.htmlz /path/to/output.azw3 --language zh-Hans
    my_command = ["/Applications/calibre.app/Contents/MacOS/ebook-convert", \
                  "temp.htmlz", new_file, \
                  "--language", "zh-Hans"]
    sp.check_output(my_command, env=my_env)
# 4. rm temp.htmlz
    my_command = ["rm", "temp.htmlz"]
    sp.check_output(my_command, env=my_env)
# z. notification
    lb_notification("📕 New Book with Embedded Fonts!", new_file)