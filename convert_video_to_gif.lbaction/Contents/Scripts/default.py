#!/usr/bin/env python
#
# LaunchBar Action Script
#
# Quell: bit.ly/2nMtZ16
# Required Software: ffmpeg, gifsicle
# 1. Generate a palette:
# ffmpeg -i vid.mp4 -vf fps=10,scale=960:-1:flags=lanczos,palettegen -y palette.png
# 2. Output the GIF using the palette:
# ffmpeg -i vid.mp4 -i palette.png -filter_complex "fps=10,scale=960:-1:flags=lanczos[x];[x][1:v]paletteuse" -y output.gif
# 3. Compress:
# gifsicle -i output.gif -O3 -o a.gif

import sys
import subprocess as sp
import os

my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]
vid_width = 960
vid_width = str(vid_width)

# Note: The first argument is the script's path
for arg in sys.argv[1:]:
# 0. set new gif name
	point_postion = arg.rfind(".")
	gif_name = arg[:point_postion]+".gif"#+arg[point_postion:]
# 1. Generate a palette:
	my_command = ["ffmpeg", "-i", arg, "-vf", "fps=10,scale=" + vid_width + ":-1:flags=lanczos,palettegen", "-y", "palette.png"]
	sp.check_output(my_command, env=my_env)
# 2. Output the GIF using the palette:
	my_command = ["ffmpeg", "-i", arg, "-i", "palette.png", "-filter_complex", "fps=10,scale=" + vid_width + ":-1:flags=lanczos[x];[x][1:v]paletteuse", "-y", gif_name]
	sp.check_output(my_command, env=my_env)
# 3. Compress
	my_command = ["gifsicle", "-i", gif_name, "-O3", "-o", gif_name]
	sp.check_output(my_command, env=my_env)
# 4. notification
	my_command = ["osascript", "notifications.scpt", gif_name]
	sp.check_output(my_command, env=my_env)

















