# Write a program to determine if a given year is a leap year.
# If the year is a leap year, then print "YES", otherwise print "NO".
# A year is a leap year if its number is a multiple of 4 but not a multiple of 100, or if it is a multiple of 400.
#
# Напишите программу, которая определяет, является ли год с данным номером високосным.
# Если год является високосным, то выведите «YES», иначе выведите «NO».
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.

x = int(input())
if (x % 4 == 0 and not x % 100 == 0) or x % 400 == 0:
    print('YES')
else:
    print('NO')
