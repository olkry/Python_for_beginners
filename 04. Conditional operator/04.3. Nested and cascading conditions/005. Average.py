# Three distinct integers are given. Write a program that finds the average of a number.
#
# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

a, b, c = int(input()), int(input()), int(input())
if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)
