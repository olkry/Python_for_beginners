# Two different cells of a chessboard are given.
# Write a program that determines if the king can hit from the first square
# to the second in one go. The program receives as input four numbers from 1 to 8 each,
# specifying the column number and row number, first for the first cell, then for the second cell.
# The program should print "YES" if it is possible to get to the second one from the first cell by the king's move,
# or "NO" otherwise.
#
# Даны две различные клетки шахматной доски.
# Напишите программу,  которая определяет, может ли король попасть с первой клетки
# на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую,
# или «NO» в противном случае.

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if ((c == a + 1) or (c == a - 1) or c == a) and ((d == b + 1) or (d == b - 1) or d == b):
    print('YES')
else:
    print('NO')

