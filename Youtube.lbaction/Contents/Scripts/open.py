import sys
import subprocess as sp
import os
import ast

folder = '../Resources/'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path) and file_path[-4:]==".jpg":
            os.remove(file_path)
    except:
        pass
my_env = os.environ.copy()
paras = ast.literal_eval(sys.argv[1])
my_command = ["open", paras["vid_url"].replace("\\/","/")]
sp.check_output(my_command, env=my_env)