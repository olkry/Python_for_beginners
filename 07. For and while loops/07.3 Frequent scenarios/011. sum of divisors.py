# The input to the program is a natural number n. Write a program that calculates the sum of all its divisors.
#
# На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.

number = int(input())
total = 0

for i in range(1, number + 1):
    if number % i == 0:
        total += i
print(total)
