# Дано натуральное число n. Напишите программу, которая печатает численный треугольник
# с высотой равной n, в соответствии с примером:
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...


nuber = int(input())
num_print = 1

for i in range(1, nuber + 1):
    for j in range(i):
        print(num_print, end=' ')
        num_print += 1
    print()