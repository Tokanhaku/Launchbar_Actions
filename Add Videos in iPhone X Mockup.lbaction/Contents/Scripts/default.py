#!/usr/bin/env python
#
# LaunchBar Action Script
#
# Required Software: ffmpeg
# method:
# ffmpeg -loop 1 -i Apple\ iPhone\ X\ Space\ Grey.png -i input.mp4 -filter_complex "overlay=110:142:shortest=1" -c:a copy -y output.mp4
# ffmpeg -i output.mp4 -framerate 1 -i Apple\ iPhone\ X\ Space\ Grey.png -filter_complex overlay -c:a copy -y output1.mp4

import sys
import subprocess as sp
import os

my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]

# Note: The first argument is the script's path
for arg in sys.argv[1:]:
# 0. set new gif name
	point_postion = arg.rfind(".")
	new_vid = arg[:point_postion]+"_mockup.mp4"#+arg[point_postion:]
# 1. Generate a palette:
# ffmpeg -loop 1 -i Apple\ iPhone\ X\ Space\ Grey.png -i input.mp4 -filter_complex "overlay=110:142:shortest=1" -c:a copy -y output.mp4
	my_command = ["ffmpeg", "-loop", "1", "-i", "Apple iPhone X Space Grey.png", "-i", arg, "-filter_complex", "overlay=110:142:shortest=1", "-c:a", "copy", "-y", "temp.mp4"]
	sp.check_output(my_command, env=my_env)
# ffmpeg -i output.mp4 -framerate 1 -i Apple\ iPhone\ X\ Space\ Grey.png -filter_complex overlay -c:a copy -y output1.mp4
	my_command = ["ffmpeg", "-i", "temp.mp4", "-framerate", "1", "-i", "Apple iPhone X Space Grey.png", "-filter_complex", "overlay", "-c:a", "copy", "-y", new_vid]
	sp.check_output(my_command, env=my_env)
# 4. notification
	my_command = ["osascript", "notification.scpt", new_vid]
	sp.check_output(my_command, env=my_env)
# 5. remove temp.mp4
    my_command = ["rm", "temp.mp4"]
    sp.check_output(my_command, env=my_env)

















