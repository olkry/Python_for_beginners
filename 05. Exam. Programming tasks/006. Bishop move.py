# Two different cells of a chessboard are given.
# Write a program that determines if an elephant can hit from the first square
# to the second in one go. The program receives as input four numbers from 1 to 8 each,
# specifying the column number and row number, first for the first cell, then for the second cell.
# The program should print "YES" if it is possible to get to the second from the first cell by the bishop's move
# or "NO" otherwise.
#
# Даны две различные клетки шахматной доски.
# Напишите программу, которая определяет, может ли слон попасть с первой клетки
# на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую
# или «NO» в противном случае.


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x1 - y1 == x2 - y2:
    print('YES')
elif x1 + y1 == x2 + y2:
    print('YES')
else:
    print("NO")