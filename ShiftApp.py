#!/usr/bin/env python3
import os
import sys

pid = sys.argv[1]

#0-11,48-59 -> Initial 2 Core Complexes
#shift all processes of the application as well as spawned pid's to cores 0-11,48-59
os.system('sudo rm app.txt')
os.system('sudo taskset -a -cp 0-11,48-59 {} > app.txt'.format(pid))

app = open('app.txt','r')
#print(app.read())
app_data = app.readlines()
#print(len(app_data))
res = ""
c = 0
for i in range(0,len(app_data),2):
    res+= app_data[i].split()[1][:-2] + ","
    c+=1

print(c)
#print(res)
pids = open('app_pid','w+')
pids.write(res[:-1])
