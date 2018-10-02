#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import json
import subprocess as sp
import os
from time import time


zeit = time()
my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]

items = []
languages = ["zh", "en", "de"]
# Note: The first argument is the script's path
for arg in sys.argv[1:]:
	#counter = arg.count("\n")
	for language in languages:
		my_command = ["trans", "-brief","-e", "google", ":"+language, arg]
		content = sp.check_output(my_command, env=my_env)
		content = content.decode("utf-8")
		item = {}
		item["title"] = content[:-1]
		item["icon"] = language+"_flag.png"
		items.append(item)
zeit = time()-zeit
item1 = {}
item1["title"] = str(zeit) + "s"
item1["icon"] = "font-awesome:fa-hourglass-2"
items.append(item1)
print(json.dumps(items))