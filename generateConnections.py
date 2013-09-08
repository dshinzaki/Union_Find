#!/usr/bin/env python

# Dylan Shinzaki
# 9/7/13
# Test script to create random UF connection and store in a text file
# Execution:
# python generateConnections.py <arg1> <arg2> <arg3>
# <arg1>: Number of nodes
# <arg2>: Number of connections
# Creates a text file of the form <arg3>.txt
#   By default this is <arg1>_<arg2>_UF.txt

import sys
import random

if len(sys.argv) < 2:
    totalNodes = 10
else:
    totalNodes = int(sys.argv[1])
    
if len(sys.argv) < 3:
    totalConnections = 10
else:
    totalConnections = int(sys.argv[2])

filename = "%d_%d_UF.txt" % (totalNodes, totalConnections)
if len(sys.argv) > 3:
    filename = sys.argv[3].concat(".txt")

f = open(filename, 'w+')

for x in range(0, totalConnections):
    f.write("%d %d\n" % (random.randint(0, totalNodes-1), random.randint(0, totalNodes-1)))
