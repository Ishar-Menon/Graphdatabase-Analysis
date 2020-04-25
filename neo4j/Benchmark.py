#!/usr/bin/env python
import os
import sys
# run perf 5 times on each client file

os.system('rm -rf {}'.format(sys.argv[1]))
os.system('mkdir {}'.format(sys.argv[1]))
NO_OF_TESTS_EACH = 1
NO_OF_TESTS = 5
app_pid_file = open('app_pid','r')
pid_list = app_pid_file.read()

for _ in range(NO_OF_TESTS):
    fname = 'sudo mkdir {}/Test_{}'.format(sys.argv[1],_)
    os.system(fname)
time = 30

for _ in range(NO_OF_TESTS):
    # Benchmarks
    print("Test {} Results".format(_))
    for i in range(NO_OF_TESTS_EACH):
        # No of tests
        print("Trial {}".format(i))
        #perf_cmd = 'sudo taskset -c 24-47,72-95 sudo perf stat -e task-clock,context-switches,cpu-migrations,page-faults,cycles,instructions,cache-references,cache-misses,branches,branch-misses,L1-dcache-loads,L1-dcache-load-misses,L1-dcache-stores,L1-dcache-store-misses,L1-dcache-prefetches,L1-dcache-prefetch-misses,L1-icache-loads,L1-icache-load-misses,L1-icache-prefetches,L1-icache-prefetch-misses -p {} -- sleep {} 2>{}/Test_{}/Trial_{}.txt'.format(pid_list,
        #    time,sys.argv[1],_, i)
        perf_cores_cmd = 'sudo taskset -c 24-47,72-95 sudo perf stat -e task-clock,context-switches,cpu-migrations,page-faults,cycles,instructions,cache-references,cache-misses,branches,branch-misses,dTLB-loads,dTLB-load-misses,dTLB-prefetch-misses,L1-dcache-loads,L1-dcache-load-misses,L1-dcache-stores,L1-dcache-store-misses,L1-dcache-prefetches,L1-dcache-prefetch-misses,L1-icache-loads,L1-icache-load-misses,L1-icache-prefetches,L1-icache-prefetch-misses -C 0-11,48-59 -- sleep {} 2>{}/Test_{}/Trial_{}.txt'.format(time,sys.argv[1],_, i)
        client_cmd = 'sudo taskset -c 24-47,72-95 python3 client.py {}'.format(_ + 1)
        net_cmd = perf_cores_cmd + ' && ' + client_cmd
        # perf && client for simultaneous execution
        print(net_cmd)
        os.system(net_cmd)
