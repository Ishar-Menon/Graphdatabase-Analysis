
# Set affinity of all processes to cores 32 - 95

import os
# Retrieve all user's
os.system('cut -d: -f1 /etc/passwd > usr_file')
k = open("usr_file","r")
udata = k.read()
u_arr = udata.split()
print(u_arr)

# Retrieve pid's of processes run by all users and append them to upid_file
for i in u_arr:
        tmp = 'pgrep -u ' + i + '>>upid_file'
        os.system(tmp)
print("\n")
#print(get_root_pid)
f = open("upid_file","r")
data = f.read()
#print(type(data))
data_arr = data.split("\n")
#print(data_arr)

# Taskset to shift all processes
for i in data_arr:
        if (i == ''):
                break
        temp = 'sudo taskset -cp 32-95 ' + i
        print(temp)
        os.system(temp)