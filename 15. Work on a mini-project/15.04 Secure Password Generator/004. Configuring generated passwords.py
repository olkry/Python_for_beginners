# На основании введенной пользователем информации, сформируйте переменную chars, содержащую все символы, которые могут быть в генерируемом пароле.

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''

pass_count = input('Сколько сгенерировать паролей: ')
while not pass_count.isdigit():
    pass_count = input('Неверно! Введите число, сколько сгенерировать паролей: ')
else:
    pass_count = int(pass_count)

print('В пароле нужны числа? 1 - да, 0 - нет')
digits_on = input()
while not digits_on.isdigit():
    print('не число')
    digits_on = input('Введите корректные данные! 1 - да, 0 - нет: ')
else:
    while True:
        if int(digits_on) == 1 or int(digits_on) == 0:
            digits_on = int(digits_on)
            break
        else:
            digits_on = input('Введите корректные данные! 1 - да, 0 - нет: ')

print('В пароле нужны большие буквы? 1 - да, 0 - нет')
upper_on = input()
while not upper_on.isdigit():
    print('не число')
    upper_on = input('Введите корректные данные! 1 - да, 0 - нет: ')
else:
    while True:
        if int(upper_on) == 1 or int(upper_on) == 0:
            upper_on = int(upper_on)
            break
        else:
            upper_on = input('Введите корректные данные! 1 - да, 0 - нет: ')


print('В пароле нужны маленькие буквы? 1 - да, 0 - нет')
lower_on = input()
while not lower_on.isdigit():
    print('не число')
    lower_on = input('Введите корректные данные! 1 - да, 0 - нет: ')
else:
    while True:
        if int(lower_on) == 1 or int(lower_on) == 0:
            lower_on = int(lower_on)
            break
        else:
            lower_on = input('Введите корректные данные! 1 - да, 0 - нет: ')

print('В пароле нужны символы "!#$%&*+-=?@^_?"? 1 - да, 0 - нет')
punctuation_on = input()
while not punctuation_on.isdigit():
    print('не число')
    punctuation_on = input('Введите корректные данные! 1 - да, 0 - нет: ')
else:
    while True:
        if int(punctuation_on) == 1 or int(punctuation_on) == 0:
            punctuation_on = int(punctuation_on)
            break
        else:
            punctuation_on = input('Введите корректные данные! 1 - да, 0 - нет: ')

print('Желаете исключить из пароля трудночитаемые символы"il1Lo0O"? 1 - да, 0 - нет')
ambiguous_on = input()
while not ambiguous_on.isdigit():
    print('не число')
    ambiguous_on = input('Введите корректные данные! 1 - да, 0 - нет: ')
else:
    while True:
        if int(ambiguous_on) == 1 or int(ambiguous_on) == 0:
            ambiguous_on = int(ambiguous_on)
            break
        else:
            ambiguous_on = input('Введите корректные данные! 1 - да, 0 - нет: ')


if digits_on:
    chars += digits
if upper_on:
    chars += uppercase_letters
if lower_on:
    chars += lowercase_letters
if punctuation_on:
    chars += punctuation
if ambiguous_on:
    amb = 'il1Lo0O'
    for i in range(len(amb)):
        chars = chars.replace(amb[i], '')


print(chars)
