# Given a natural number n. Write a program that prints the multiplication table for n.
#
# Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n.

n = int(input())

for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
