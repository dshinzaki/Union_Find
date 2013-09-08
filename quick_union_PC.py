#!/usr/bin/env python

# Dylan Shinzaki
# 9/7/13
# Implements the Quick Find w/ tree weighting and path compression
# 
# UnionFindQuickUnionPC(n): Generates a quick find object with n nodes
# load(filename): Loads connections in filename
# union(id1, id2): Unites node id1 and id2. If id1 or id2 are not valid
#   nodes, then the command does nothing
# find(id1, id2): Returns true if there is a connection between id1 and id2
#   Returns false if id1 or id2 are not valid nodes
# showId(): Prints the id array

# Execution:
# python UnionFindQuickUnionPC
# Executes a test script

class UnionFindQuickUnionPC(object):
    def __init__(self, size=0):
        # Creates an empty UF structure
        self.id = [x for x in range(size)]
        self.sz = [1 for x in range(size)]
        self.size = size
        
    def __root(self, id):
        while(id != self.id[id]):
            self.id[id] = self.id[self.id[id]]
            id = self.id[id]
        return id
        
    def load(self, filename):
        f = open(filename, 'r')
        for line in f:
            str = line.split() 
            self.union(int(str[0]), int(str[1]))
            
    def union(self, id1, id2):
        if (not self.__isValid(id1, id2)):
            print "Out of bounds, not added"
            return
        start1 = id1
        start2 = id2
        
        id1 = self.__root(id1)
        id2 = self.__root(id2)

        # set so id2 is the larger tree
        if self.sz[id1] > self.sz[id2]:
            tmp = id1
            id1 = id2
            id2 = tmp
            
            tmp = start1
            id1 = start2
            start2 = tmp
        
        self.id[id1] = id2
        self.sz[id2] += self.sz[id1]
        
    def find(self, id1, id2):
        if (not self.__isValid(id1, id2)):
            print "Out of bounds, not connected"
            return false
        return self.__root(id1) == self.__root(id2)
    
    def showId(self):
        for i in range(len(self.id)):
            print "%d : %d" % (i, self.id[i]) 
            
    def __isValid(self, id1, id2):
        return (id1 >= 0) and (id1 < self.size) and \
            (id2 >= 0) and (id2 < self.size)            

if __name__=="__main__":
    testUnion = UnionFindQuickUnionPC(10)
    testUnion.union(0,1)
    testUnion.union(0,2)
    testUnion.union(0,3)
    testUnion.union(4,1)
    testUnion.union(5,6)
    testUnion.union(8,7)
    testUnion.union(9,5) 
    testUnion.showId()
    
    print "Test queries. Should all be true"
    print "0,1 are connected: ", testUnion.find(0,1)
    print "5,7 are not connected: ", not testUnion.find(5,7)
    print "9,1 are not connected: ", not testUnion.find(9,1)
    
    