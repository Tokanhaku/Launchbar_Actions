#!/usr/local/anaconda3/bin/python3
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
	screen = screen.resize((758,round(758/3*4)), Image.ANTIALIAS)
	screen_w, screen_h = screen.size

	kindle = Image.open("Amazon Kindle Paperwhite.png", 'r')
	img_w, img_h = kindle.size
	background = Image.new('RGBA', kindle.size)
	
	offset = (184,232)
	background.paste(kindle, (0,0))
	background.paste(screen, offset)


	background.save(new_image)
	my_command = ["osascript", "notification.scpt", new_image]
	sp.call(my_command, env=my_env)