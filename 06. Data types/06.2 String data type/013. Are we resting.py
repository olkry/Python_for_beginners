# Write a program that reads one line and then prints "YES"
# if the input string contains the substring "Saturday" or "Sunday", and "NO" otherwise.
# Input data format
# The input to the program is one line.
#
# Напишите программу, которая считывает одну строку, после чего выводит «YES»,
# если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
# Формат входных данных
# На вход программе подается одна строка.


# lenth = input()
# if 'суббота' in lenth:
#     print('YES')
# elif 'воскресенье' in lenth:
#     print('YES')
# else:
#     print('NO')

print('YES' if 'суббота' in (lenth := input()) or 'воскресенье' in lenth else 'NO')
