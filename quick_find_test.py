import unittest
from quick_find import UnionFindQuickFind
class TestQuickFind(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_connected_1(self):
        testUnion = UnionFindQuickFind(10)
        testUnion.union(0,1)
        testUnion.union(0,2)
        testUnion.union(0,3)
        testUnion.union(4,1)
        testUnion.union(5,6)
        testUnion.union(8,7)
        testUnion.union(9,5)
        self.assertTrue(testUnion.find(0,1))
    
    def test_connected_2(self):
        testUnion = UnionFindQuickFind(10)
        testUnion.union(0,1)
        testUnion.union(0,1)
        testUnion.union(0,3)
        testUnion.union(4,1)
        testUnion.union(5,6)
        testUnion.union(8,7)
        testUnion.union(9,5)
        self.assertTrue(testUnion.find(4,3) == testUnion.find(3,4))
    
    def test_not_connected(self):
        testUnion = UnionFindQuickFind(10)
        testUnion.union(0,1)
        testUnion.union(0,2)
        testUnion.union(0,3)
        testUnion.union(4,1)
        testUnion.union(5,6)
        testUnion.union(8,7)
        testUnion.union(9,5)
        self.assertTrue(not testUnion.find(9,1))
    
if __name__ == '__main__':
    unittest.main()
    
