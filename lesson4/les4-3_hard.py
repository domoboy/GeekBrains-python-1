# lesson4-3, hard

def arrang_chess(matrix, *adresses):
    '''
    расставляет шахматы, возвращая новую матрицу
    :matrix: шахматная доска
    :adress: список из пары чисел (от 1-8)
    '''
    for adress in adresses:
        i = 8 - adress[1]
        j = adress[0] - 1
        matrix[i][j] = 1
    
    return matrix
        
'''
    1  2  3  4  5  6  7  8
8 [[0, 0, 0, 0, 0, 0, 0, 0],
7  [0, 0, 0, 0, 0, 0, 0, 0],
6  [0, 0, 0, 0, 0, 0, 0, 0],
5  [0, 0, 0, 0, 0, 0, 0, 0],
4  [0, 0, 0, 0, 0, 0, 0, 0],
3  [0, 0, 0, 0, 0, 0, 0, 0],
2  [0, 0, 0, 0, 0, 0, 0, 0],
1  [0, 0, 0, 0, 0, 0, 0, 0]]
'''
f1, f2, f3, f4, f5, f6, f7, f8 = ((4, 3), (5, 6), (2, 3), (7, 8),
                                  (6, 3), (5, 1), (3, 7), (8, 2))

chessboard = [[0]*8 for _ in range(8)]

chessboard = arrang_chess(chessboard, f1, f2, f3, f4, f5, f6, f7, f8)





