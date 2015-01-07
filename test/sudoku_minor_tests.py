'''
Created on Jan 6, 2015

@author: Ciprian Cosma
'''


import unittest
import sudoku


class sudoku_minor_test(unittest.TestCase):

    def test_find_first(self):
        matrix = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
        self.assertEqual(sudoku.find_first_eligible(matrix), (0, 2), "First"
                         " matched position is not correct")
        matrix[0][0] = 0
        self.assertEqual(sudoku.find_first_eligible(matrix), (0, 0), "0,0 "
                         " matched position is not correct")

    def test_full_find_first(self):
        size = 9
        matrix = []
        for i in range(size):
            matrix.append([])
            for j in range(size):
                matrix[i].append(1)
        self.assertEqual(sudoku.find_first_eligible(matrix), (-1, -1), "Error"
                         " value is not detected")

    def test_find_values(self):
        pass
if __name__ == '__main__':
    unittest.main()
