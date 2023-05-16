# Two integers m and n are given. Write a program that prints all numbers from m to n inclusive in ascending order,
# if m<n, or in descending order otherwise.
#
# Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания,
# если m<n, или в порядке убывания в противном случае.

m, n = int(input()), int(input())
if m < n:
    for i in range(m, n+1):
        print(i)
else:
    for i in range(m, n-1, -1):
        print(i)
