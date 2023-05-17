# The input to the program is a natural number n. Write a program that calculates n!.
#
# На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.

total = 1

for i in range(1, int(input()) + 1):
    total *= i
print(total)
