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
	screen_w, screen_h = screen.size
# iPhone X
	if screen_w == 1125 and screen_h == 2436:
		iphone = Image.open("Apple iPhone X Space Grey.png", 'r')
		img_w, img_h = iphone.size
		background = Image.new('RGBA', iphone.size)
		
		offset = (140,180)
		background.paste(screen, offset)
		background.paste(iphone, (0,0), iphone)
# iPhone 8
	elif screen_w == 750 and screen_h == 1334:
		iphone = Image.open("Apple iPhone 8 Silver.png", 'r')
		img_w, img_h = iphone.size
		background = Image.new('RGBA', iphone.size)
		screen = Image.open(arg, "r")
		offset = (100,280)
		background.paste(iphone)
		background.paste(screen, offset)
# iPhone 8 Plus
	elif screen_w == 1080 and screen_h == 1920:
		iphone = Image.open("Apple iPhone 8 Silver.png", 'r')
		img_w, img_h = iphone.size
		background = Image.new('RGBA', iphone.size)
		screen = Image.open(arg, "r")
		offset = (100,280)
		background.paste(iphone)
		background.paste(screen, offset)
	else:
		my_command = ["osascript", "warning.scpt", arg]
		sp.call(my_command, env=my_env)
		break
	background.save(new_image)
	my_command = ["osascript", "notification.scpt", new_image]
	sp.call(my_command, env=my_env)