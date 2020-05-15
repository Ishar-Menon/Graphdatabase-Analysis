import csv

origin_path = 'D:\\College\\PES\\Semester-6\\Cloud - Computing\\Graphdatabase-Analysis\\postgres\\uprof_L3_After_Indexing\\'
File = open(origin_path +'pL34.txt',"r")
lines_ret_ins = File.readlines()
CSV_File = 'T4.csv'
Headers = ['CoreId','DTLB misses per 1000','L1 ITLB miss,L2 ITLB hit per 1000','L1 ITLB miss,L2 ITLB miss per 1000','Retired Instructions']
#print(len(lines_ret_ins),len(lines_ins))

row = []
rows = []
k = 0
for i in range(1,len(lines_ret_ins) - 1,4):
    #DTLB.append(lines_ret_ins[i].split()[3])
    #ITLB1.append(lines_ret_ins[i + 1].split()[3])
    #ITLB2.append(lines_ret_ins[i + 2].split()[3])
    #Retins.append(lines_ret_ins[i + 3].split()[3])
    DTLB = (int(lines_ret_ins[i].split()[3])/int(lines_ret_ins[i + 3].split()[3]))*1000
    ITLB1 = (int(lines_ret_ins[i + 1].split()[3])/int(lines_ret_ins[i + 3].split()[3]))*1000
    ITLB2 = (int(lines_ret_ins[i + 2].split()[3])/int(lines_ret_ins[i + 3].split()[3]))*1000
    rows.append([k,DTLB,ITLB1,ITLB2,lines_ret_ins[i + 3].split()[3]])
    k+=1

#print(rows)
#print(DTLB)
#print(ITLB1)
#print(ITLB2)
#print(Retins)


with open(CSV_File,'w',newline='\n') as csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerow(Headers)
    csvwriter.writerows(rows)


#print("HI")