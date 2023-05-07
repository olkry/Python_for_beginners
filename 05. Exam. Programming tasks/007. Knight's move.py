# Two different cells of a chessboard are given. Write a program
# which determines whether the knight can get from the first cell to the second in one move.
# The program receives as input four numbers from 1 to 8 each, specifying the column number
# and the line number first for the first cell, then for the second cell.
# The program should print "YES" if it is possible to get to the second from the first cell by the knight's move
# or "NO" otherwise.
#
# Даны две различные клетки шахматной доски. Напишите программу,
# которая определяет, может ли конь попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца
# и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую
# или «NO» в противном случае.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x2 == x1 + 1 or x2 == x1 - 1) and (y2 == y1 + 2 or y2 == y1 - 2):
    print('YES')
elif (x2 == x1 + 2 or x2 == x1 - 2) and (y2 == y1 + 1 or y2 == y1 - 1):
    print('YES')
else:
    print('NO')