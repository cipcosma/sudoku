'''
Created on Jan 6, 2015

@author: Ciprian Cosma
'''


def find_first_eligible(matrix):
    ''' return the first empty location of the matrix

    it searches by row/column
    if all the matrix has values, it returns -1, -1
    '''
    size = len(matrix)
    for x in range(size):
        for y in range(size):
            if matrix[x][y] == 0:
                return (x, y)
    return (-1, -1)


def find_values(x, y, matrix):
    ''' returns a list of legal values for a cell in a sudoku matrix

    matrix is an array of an incomplete sudoku game
    x and y are the coordinates of the cell
    '''
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(matrix)):
        if matrix[i][y] in values:
            values.remove(matrix[i][y])
        if matrix[x][i] in values:
            values.remove(matrix[x][i])
    for i in range(x/3*3, x/3*3+3, 1):
        for j in range(y/3*3, y/3*3+3, 1):
            if matrix[i][j] in values:
                values.remove(matrix[i][j])
    return values


def sudoku(matrix):
    ''' wrapper for the recursive function

    '''
    matrix, done = sudoku_rec(matrix, False)
    return matrix

def sudoku_rec(matrix, done):
    ''' recursive function that solves a sudoku game

    - receives a partially solved sudoku and returns
    the completely solved game
    '''
    (x, y) = find_first_eligible(matrix)
    if (x, y) == (-1, -1):
        done = True
        return (matrix, True)
    for value in find_values(x,y,matrix):
        matrix[x][y] = value
        (matrix, done) = sudoku_rec(matrix, False)
        if done:
            return(matrix, True)
    if not done:
        matrix[x][y] = 0
        return (matrix, False)

if __name__ == '__main__':
    calls = 0
    matrix_in = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
    #matrix_in = [
    #      [5,3,7,7,7,7,7,7,2],
    #      [6,7,7,1,9,5,7,7,4],
    #      [7,9,8,7,7,7,7,7,5],
    #      [8,7,7,7,7,7,7,7,3],
    #      [4,7,7,8,7,3,7,7,7],
    #      [7,7,7,7,2,7,7,7,6],
    #      [7,6,7,7,7,7,2,3,1],
    #      [7,7,7,4,1,9,4,5,8],
    #      [1,2,3,4,8,5,7,0,0]]

    matrix_out = sudoku(matrix_in)
    print calls
    print matrix_out
