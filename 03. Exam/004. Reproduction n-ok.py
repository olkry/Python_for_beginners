# Write a program that reads a positive integer n, n[1,9], and outputs the value of n + nn + nnn.
#
# Напишите программу, которая считывает целое положительное число n, n[1,9], и выводит значение числа n + nn + nnn.

n = int(input())
print(n + n * 11 + n * 111)