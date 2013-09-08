#!/usr/bin/env python

# Dylan Shinzaki
# 9/7/13
# Test script to compare the implementation of the Union Find data structures
# Tests Quick find, Quick Union, and Quick Union with Path Compression
# Execution:
# python compareQF.py <arg1> <arg2> <arg3>
# <arg1>: Number of nodes in the UF structure (default 10)
# <arg2>: Name of file containing connections (default 10_10_UF.txt)
# <arg3>: Number of times to query the structure with random node pairs (default 10)

import sys
import random
import time
import timeit

from quick_find import UnionFindQuickFind
from quick_union import UnionFindQuickUnion
from quick_union_PC import UnionFindQuickUnionPC

if len(sys.argv) < 4:
    rep = 10
    print "Default to 10 random queries"
else:
    rep = int(sys.argv[3])

if len(sys.argv) < 3:
    rep = "10_10_UF.txt"
    print "Default to 10_10_UF.txt"
else:
    filename = sys.argv[2]

if len(sys.argv) < 2:
    totalNodes = 10
    print "Default to 10 nodes"
else:
    totalNodes = int(sys.argv[1])

quick_find = UnionFindQuickFind(totalNodes)
quick_union = UnionFindQuickUnion(totalNodes)
quick_union_PC = UnionFindQuickUnionPC(totalNodes)

x1 = [0] * rep
x2 = [0] * rep
for i in range(rep):
    x1[i] = random.randint(0, totalNodes-1)
    x2[i] = random.randint(0, totalNodes-1)

print "Quick find:"
start_time = time.time()
quick_find.load(filename)
end_time = time.time()
print("Elapsed time to load network is %g seconds" % (end_time - start_time))
start_time = time.time()
for i in range(rep):
    r1 = quick_find.find(x1[i],x2[i])
end_time = time.time()
print("Elapsed time for the queries is %g seconds" % (end_time - start_time))

print "Quick Union:"
start_time = time.time()
quick_union.load(filename)
end_time = time.time()
print("Elapsed time to load network is %g seconds" % (end_time - start_time))
start_time = time.time()
for i in range(rep):
    r2 = quick_union.find(x1[i],x2[i])
end_time = time.time()
print("Elapsed time for the queries is %g seconds" % (end_time - start_time))

print "Quick Union with path compression and tree weighting:"
start_time = time.time()
quick_union_PC.load(filename)
end_time = time.time()
print("Elapsed time for quick union PC to load network is %g seconds" % (end_time - start_time))
start_time = time.time()
for i in range(rep):
    r3 = quick_union_PC.find(x1[i],x2[i])
end_time = time.time()
print("Elapsed time for quick union PC is %g seconds" % (end_time - start_time))



