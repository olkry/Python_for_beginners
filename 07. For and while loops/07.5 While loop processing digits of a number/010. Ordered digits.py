# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр
# при просмотре справа налево упорядоченной по неубыванию.

num = int(input())
control = 'YES'

while num > 9:
    last_dig = num % 10
    pre_last = (num // 10) % 10
    if pre_last < last_dig:
        control = 'NO'
    num //= 10
print(control)
