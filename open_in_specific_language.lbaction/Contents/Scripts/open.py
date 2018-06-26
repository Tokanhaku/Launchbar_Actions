import sys
import subprocess as sp
import os
import ast

my_env = os.environ.copy()
paras = ast.literal_eval(sys.argv[1])
paras["app"] = paras["app"].replace("\\", "")
my_command = ["open", paras["app"], "--args", "-AppleLanguages", "("+paras["language"]+")"]

#my_command = ["open", "/Applications/Downie.app"]
sp.check_output(my_command, env=my_env)