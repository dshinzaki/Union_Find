Dylan Shinzaki
9/7/13

Implements several data structures for solving the union find problem
Each structure supports the following operations:

load(filename) : loads connects stored in filename
union(id1,id2) : connects nodes id1 and id2
find(id1, id2) : Returns true if nodes id1 and id2 are connected and false otherwise


Files:
***************************************************************
quick_find.py: Implements a quick find approach
***************************************************************
quick_union.py: Implements a quick union approach
***************************************************************
quick_union_PC.py: Implements a quick union approach with path compression and tree weighting
***************************************************************
generateConnections.py: Randomly generates a network
***************************************************************
X_X_UF.txt: Example random networks
***************************************************************
compareQF.py: Implements a testing script to compare the 3 structures.
 
Example execution and output for 10000 queries on a 1000 node random network:
python compareQF.py 1000 1000_100000_UF.txt 10000

Quick find:
Elapsed time to load network is 28.384 seconds
Elapsed time for the queries is 0.00999999 seconds
Quick Union:
Elapsed time to load network is 5.199 seconds
Elapsed time for the queries is 0.505 seconds
Quick Union with path compression and tree weighting:
Elapsed time for quick union PC to load network is 2.799 seconds
Elapsed time for quick union PC is 0.0220001 seconds


