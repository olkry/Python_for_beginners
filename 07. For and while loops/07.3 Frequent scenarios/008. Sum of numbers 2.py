# The input to the program is a natural number n. Write a program that calculates the sum of those numbers from 1 to
# n (inclusive) whose square ends in 2, 5, 8.
#
# На вход программе подается натуральное число n. Напишите программу, которая подсчитывает сумму тех чисел от 1 до
# n (включительно) квадрат которых оканчивается на 2, 5, 8.

total = 0
flag = True

for i in range(1, int(input()) + 1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
        total += i
        flag = False
if flag:
    print('0')
else:
    print(total)
