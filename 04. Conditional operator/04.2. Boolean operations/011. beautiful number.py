# We call a number beautiful if it has four digits and is evenly divisible by 7 or 17.
# Write a program to determine if an input number is beautiful.
# The program should output "YES" if the number is pretty, or "NO" otherwise.
#
# Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
# Напишите программу, определяющую, является ли введённое число красивым.
# Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.

x = int(input())
if 999 < x < 10000 and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')