import os
import time
# Run Uprof on each of the four core complexes for each instruction

os.system('rm -rf Results')
os.system('mkdir Results')
NO_OF_CCX = 4
NO_OF_TESTS = 5
for _ in range(NO_OF_TESTS):
    fname = 'sudo mkdir uprof_results/Test_{}'.format(_)
    os.system(fname)
benchTime = 30

for _ in range(NO_OF_TESTS):
    # Benchmarks
    print("Test {} Results".format(_))
    for i in range(NO_OF_CCX):
        # No of tests
        print("CCX {}".format(i))
        uprof_cmd = '''sudo taskset -a -c 24-47,72-95 sudo AMDuProfPcm -m l3 -c ccx={} -d {} -o /home/user/Desktop/ycsbGraph/Graphdatabase-Analysis/neo4j/uprof_results/Test_{}/Trial_{}.csv'''.format(
            i, benchTime, _, i)
        client_cmd = 'sudo python client.py {}'.format(_ + 1)
        net_cmd = uprof_cmd + " && " + client_cmd
        print(net_cmd)

        os.system(net_cmd)
