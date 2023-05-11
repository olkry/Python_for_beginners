# We will consider an email address to be valid if it contains the dog symbol (@) and dots.
# Write a program that checks the correctness of an email address.
# Input data format
# The input to the program is one string - an email address.
#
# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки.
# Напишите программу проверяющую корректность email адреса.
# Формат входных данных
# На вход программе подаётся одна строка – email адрес.

# email = input()
# if '@' in email and '.' in email:
#     print('YES')
# else:
#     print('NO')


print('YES' if '@' in (email := input()) and '.' in email else 'NO')
