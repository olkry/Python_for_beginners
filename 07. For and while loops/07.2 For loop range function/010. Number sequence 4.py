# Given two natural numbers m and n (m<=n). Write a program that prints all numbers from m to n inclusive
# satisfying at least one of the following conditions:
# the number is a multiple of 17;
# the number ends in 9;
# the number is a multiple of 3 and 5 at the same time.
#
# Даны два натуральных числа m и n (m<=n). Напишите программу, которая выводит все числа от m до n включительно
# удовлетворяющие хотя бы одному из условий:
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.

num_m, num_n = int(input()), int(input())

for i in range(num_m, num_n + 1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)



