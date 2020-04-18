import matplotlib.pyplot as plt

def convert(line):
    return list(map(lambda x: int(x.strip()), line.split(",")))

records = []
for i in range(0,9):
    records.append(i*50000+100000)

# record count vs Instruction Count
plt.figure()
plt.title("Instruction Count vs Record count")

plt.xlabel("Records")
plt.ylabel("Instructions")

fin = open("Instructions.txt", "r").readlines()
plt.plot(records, convert(fin[0]),'-ob', label='A')
plt.plot(records, convert(fin[1]), '-vg', label='B')
plt.plot(records, convert(fin[2]), '-xr', label='c')
plt.plot(records, convert(fin[3]), '-pc', label='D')
plt.plot(records, convert(fin[4]), '-sm', label='E')
plt.plot(records, convert(fin[5]), '-Dy', label='F')
plt.legend()
plt.show()