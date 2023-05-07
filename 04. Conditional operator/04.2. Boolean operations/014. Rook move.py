# Two different cells of a chessboard are given. Write a program that determines
# can the rook move from the first cell to the second in one move.
# The program receives as input four numbers from 1 to 8 each, specifying the column number and
# line number first for the first cell, then for the second cell.
# The program should print "YES" if it is possible to hit from the first square with the rook's move
# to the second, or "NO" otherwise.
#
# Даны две различные клетки шахматной доски. Напишите программу, которая определяет,
# может ли ладья попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и
# номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES», если из первой клетки ходом ладьи можно попасть
# во вторую, или «NO» в противном случае.

xstart, ystart, xend, yend =  int(input()), int(input()), int(input()), int(input())
if (xstart == xend and ystart != yend) or (ystart == yend and xstart != xend):
    print('YES')
else:
    print('NO')
