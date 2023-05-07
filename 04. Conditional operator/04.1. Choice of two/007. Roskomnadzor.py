# Write a program that determines whether a user is allowed to access an Internet resource or not.
#
# Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.

age = int(input())
if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')
