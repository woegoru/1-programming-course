
#matrix([line][column])
#det = a11*A11+a12*A12+a13*A13...
#a11*(-1)^(1+1)M11+a12*(-1)^(1+2)M12+a13*(-1)^(1+3)M13...
#(-1)^(i+j)
#M11=a22*a33-a32*a23
#M12=a21*a33-a31*a23
#M13=a21*a32-a31*a2
# 2*2 det = M[0][0]*M[1][1] — M[0][1]*M[1][0]
#det big = det smal + det smal 2

from copy import deepcopy

def small_matrix(matrix1, line, column):
    matrix20 = deepcopy(matrix1)
    matrix20.remove(matrix1[line])
    for i in range(len(matrix20)):
        matrix20[i].remove(matrix20[i][column])
    return matrix20

def determinant(matrix):
    for line in matrix:
        if len(line) != len(matrix):
            #not square matrix
            return None
    if len(matrix) == 2:
        s_det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        return s_det
    else:
        c = 0
        for j in range(len(matrix)):
            cherezmin = (-1) ** (0+j) * (matrix[0][j]) * (determinant(small_matrix(matrix, 0, j)))
            c = c + cherezmin
        return c

