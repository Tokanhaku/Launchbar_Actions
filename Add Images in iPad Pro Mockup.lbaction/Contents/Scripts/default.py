#!/usr/local/bin/python3
#
# LaunchBar Action Script
#
# Required Software: Pillow(Python)
# method:

from PIL import Image
import sys
import subprocess as sp
import os

my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]
for arg in sys.argv[1:]:
# 0. set new image name
	point_postion = arg.rfind(".")
	new_image = arg[:point_postion]+"_mockup.png"#+arg[point_postion:]
	screen = Image.open(arg, "r")
	screen_w, screen_h = screen.size
	if screen_w == 2732 and screen_h == 2048:
		ipad = Image.open("Apple iPad Pro Gold H.png", 'r')
		offset = (350,200)
	elif screen_h == 2732 and screen_w == 2048:
		ipad = Image.open("Apple iPad Pro Gold V.png", 'r')
		offset = (200,350)
	else:
		my_command = ["osascript", "warning.scpt", arg]
		sp.call(my_command, env=my_env)
		break
	img_w, img_h = ipad.size
	background = Image.new('RGBA', ipad.size)
	background.paste(screen, offset)
	background.paste(ipad, (0,0), ipad)
	background.save(new_image)
	my_command = ["osascript", "notification.scpt", "New iPad Mockup Image!",new_image]
	sp.call(my_command, env=my_env)