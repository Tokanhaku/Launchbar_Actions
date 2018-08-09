#!/usr/local/anaconda3/bin/python
#
# LaunchBar Action Script
#
import sys
import subprocess as sp
import os
import new_file

my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]

for arg in sys.argv[1:]:    
    my_command = ["aria2c", arg]
    a = str(sp.check_output(my_command, env=my_env))
    jsp = a[(a.rfind("B/s|")+4):(a.rfind(".jsp")+4)]
    print(jsp)
    file = open(jsp)
    os.remove(jsp)
    
    for line in file:
        if "iframe src=" in line:
            anfang = line.find("https://")
            end = line.find(".pdf")
            pdf = line[anfang:end+4]
#   
    print(pdf)
    my_command = ["aria2c", pdf]
    a = str(sp.check_output(my_command, env=my_env))
    file = a[(a.rfind("B/s|")+4):(a.rfind(".pdf")+4)]
    new_file.lb_notification("New Document downloaded!",file)


