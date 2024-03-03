# Напишите функцию generate_password(), которая принимает два аргумента:
#
# length: длину пароля;
# chars: алфавит из символов которого состоит пароль;
# и возвращает пароль.
#
# Используя цикл for, сгенерируйте необходимое количество паролей.
from random import *


def generate_password(chars, length):
    password = ''
    for i in range(length):
        password += choice(chars)
    return password



pass_char = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&*+-=?@^_.'
lenth = 8

for _ in range(int(input())):
    print(generate_password(pass_char, lenth))
