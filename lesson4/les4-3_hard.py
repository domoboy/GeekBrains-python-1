# lesson4-3, hard


def arrang_chess(matrix, *adresses):
    '''
    Расставляет шахматы, возвращая новую матрицу

    :matrix: шахматная доска
    :adress: список из пары чисел (от 1-8)
    '''
    for adress in adresses:
        i = 8 - adress[1]
        j = adress[0] - 1
        matrix[i][j] = 1

    return matrix


def iscrossing(matrix):
    '''
    Возвращяет 'Yes', если в строчке и столбце
    по одному ферзю, иначе 'No'

    :matrix: шахматная доска
    '''
    res = 'No'
    for line in matrix:
        if line.count(1) != 1:
            return res
    for col in list(zip(*matrix)):
        if col .count(1) != 1:
            return res
    res = 'Yes'

    return res

'''
# Свободная расстановка
f1, f2, f3, f4, f5, f6, f7, f8 = ((4, 3), (5, 6), (2, 3), (7, 8),
                                  (6, 3), (5, 1), (3, 7), (8, 2))
'''
# Правильная расстановка
f1, f2, f3, f4, f5, f6, f7, f8 = ((1, 2), (2, 4), (3, 6), (4, 8),
                                  (5, 3), (6, 1), (7, 7), (8, 5))

# Формирование шахматной доски
chessboard = [[0]*8 for _ in range(8)]

# Раастановка шахмат
chessboard = arrang_chess(chessboard, f1, f2, f3, f4, f5, f6, f7, f8)

print('''
    1  2  3  4  5  6  7  8
8  {line1}
7  {line2}
6  {line3}
5  {line4}
4  {line5}
3  {line6}
2  {line7}
1  {line8}
'''.format(line1=chessboard[0],
           line2=chessboard[1],
           line3=chessboard[2],
           line4=chessboard[3],
           line5=chessboard[4],
           line6=chessboard[5],
           line7=chessboard[6],
           line8=chessboard[7]))

res = iscrossing(chessboard)
print(res)
