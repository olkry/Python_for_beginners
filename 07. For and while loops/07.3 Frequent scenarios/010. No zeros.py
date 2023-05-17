# Write a program that reads 10 numbers and prints the product of the non-zero numbers.
#
# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

total = 1

for i in range(10):
    n = int(input())
    if n != 0:
        total *= n
print(total)
