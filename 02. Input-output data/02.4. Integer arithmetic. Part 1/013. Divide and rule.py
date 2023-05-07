# Write a program that reads a positive integer x and displays a sequence of numbers x1,x2,x3,x4,x5
# separated by three dashes.
#
# Напишите программу, которая считывает целое положительное число x и выводит на экран
# последовательность чисел x1,x2,x3,x4,x5, разделённых тремя черточками.

num = int(input())
print(num, 2 * num, 3 * num, 4 * num, 5 * num, sep='---')