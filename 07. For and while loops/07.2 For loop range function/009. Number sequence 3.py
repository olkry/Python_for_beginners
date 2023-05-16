# Two integers m and n (m>n) are given. Write a program that prints all odd numbers from m to n inclusive in descending order.
#
# Даны два целых числа m и n (m>n). Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.

m, n = int(input()), int(input())

if m % 2 != 0:
    for i in range(m, n, -2):
        print(i)
else:
    for i in range(m - 1, n - 1, -2):
        print(i)
