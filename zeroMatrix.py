"""Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0. """

matrix = [[4,1,2,3],[4,5,6,0],[8,9,10,23]]

for i in range(3):
    for b in range(4):
        if matrix[i][b]==0:
            for c in range(3):
                for d in range(4):
                    matrix[c][d]=0
        else:
            continue
print(matrix)
