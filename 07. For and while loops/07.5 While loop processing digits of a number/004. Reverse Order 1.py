# Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.

num = int(input())

while num != 0:
    print(num % 10)
    num //= 10
