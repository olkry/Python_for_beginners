# Two cells of a chessboard are given.
# Write a program that determines whether the specified cells have the same color or not.
# If they are of the same color, then print the word "YES", and if they are of different colors, then print "NO".
#
# Заданы две клетки шахматной доски.
# Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет.
# Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if ((x1 + y1) % 2 == 0) and ((x2 + y2) % 2 == 0):
    print('YES')
elif ((x1 + y1) % 2 == 1) and ((x2 + y2) % 2 == 1):
    print('YES')
else:
    print('NO')