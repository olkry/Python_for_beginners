# Подключите модуль random;
# Создайте строковые константы:
# digits: 0123456789;
# lowercase_letters: abcdefghijklmnopqrstuvwxyz;
# uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
# punctuation: !#$%&*+-=?@^_.
# Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле.

from random import *


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''
