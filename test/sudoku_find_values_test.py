'''
Created on Jan 6, 2015

@author: Ciprian Cosma
'''
import unittest
import sudoku


class sudoku_find_values_test(unittest.TestCase):


    def setUp(self):
        self.matrix = [
          [5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


    def tearDown(self):
        pass


    def test_find_values(self):
        
        self.assertEqual(sudoku.find_values(0, 2, self.matrix), [1,2,4], "The"
                         " list is wrong")
        self.assertEqual(sudoku.find_values(8, 0, self.matrix), [1,2,3], "The"
                         " list is wrong")
        self.assertEqual(sudoku.find_values(8, 8, self.matrix), [4], "The"
                         " list is wrong")
        self.assertEqual(sudoku.find_values(3, 8, self.matrix), [2,4,7], "The"
                         " list is wrong")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()