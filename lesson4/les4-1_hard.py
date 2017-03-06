# lesson 4-1, hard

matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

matrix_rotate = [list(x) for x in list(zip(*matrix))]

print(matrix_rotate)
