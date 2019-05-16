#!/usr/bin/env python
##########################################################
#Copyright (c) 2019 Volodymyr Len <vladymyrlen@gmail.com>#
##########################################################
import sys
import psutil

def cpu_metrics():
    cpu_name = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'guest']
    for name, value in zip(cpu_name, psutil.cpu_times()):
        print(name, value)

def mem_metrics():
    mem_name = ['total', 'available', 'percent', 'used', 'free', 'active', 'inactive', 'buffers', 'cached', 'shared', 'slab']
    for name, value in zip(mem_name, psutil.virtual_memory()):
        print(name, value)

if __name__ == "__main__":
     if sys.argv[1] == 'cpu':
         cpu_metrics()
     elif sys.argv[1] == 'mem':
         mem_metrics()
     elif sys.argv[1] in ['-h', '--help']:
         print('cpu arg is for displaying CPU metrics' + '\n' + 'mem arg is for displaying MEM metrics')
     else:
         print('Please add arguments cpu or mem or -h for helping')
