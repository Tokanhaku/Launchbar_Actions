#!/usr/local/anaconda3/bin/python3
#
# LaunchBar Action Script
#
import sys
import subprocess as sp
import os
from urllib.parse import quote

my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]

n = 0
added_todos = ""
tags = ""
lists = ""
# Note: The first argument is the script's path
for arg in sys.argv[1:]:
	todos = arg.split('\n')
	for todo in todos:
		todo = todo.strip()
		if(todo[:4] == "http"):
			title = ""
			try:
				from GetURLTitle import GetURLTitle as GetTitle
				title = GetTitle(todo)
				if title != "":
					added_todos = (added_todos+ "\n" + title + "&notes="+ todo)
				n += 1
			except:
				pass
		else:
			todo_analyse = todo.split(' ')
			for item in todo_analyse:
				if item != "":
					if item[0] == "#":
						tags += "&tags="+item[1:]
						todo = todo.replace(" "+item, "")
					elif item[0] == "@":
						lists += "&list="+item[1:]
						todo = todo.replace(" "+item, "")
			if todo != "":
				added_todos = (added_todos+ "\n" + todo )
				n += 1

	added_todos = "things:///add?titles=" + added_todos + "&reveal=false&reveal=false" + tags + lists
	my_command=["open", added_todos]
	sp.check_output(my_command, env=my_env)

	my_command = ["osascript", "notifications.scpt", str(n), todo]
	sp.check_output(my_command, env=my_env)