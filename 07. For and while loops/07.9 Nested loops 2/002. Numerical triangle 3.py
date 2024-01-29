# Дано натуральное число n. Напишите программу, которая печатает численный треугольник
# с высотой равной n, в соответствии с примером:
#
# 1
# 121
# 12321
# 1234321
# 123454321
# ...

number = int(input())

for i in range(1, number + 1):
    num_print = 1
    num_print_retern = i - 1
    for j in range(i * 2 - 1):
        if num_print <= i:
            print(num_print, end='')
            num_print += 1
        else:
            print(num_print_retern, end='')
            num_print_retern -= 1
    print()

print('--------------------')
# any

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i):
        print(j, end="")

    print(i, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()
