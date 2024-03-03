# Программа должна запрашивать у пользователя следующую информацию:
#
# Количество паролей для генерации;
# Длину одного пароля;
# Включать ли цифры 0123456789?
# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
# Включать ли символы !#$%&*+-=?@^_?
# Исключать ли неоднозначные символы il1Lo0O?


pass_count = input('Сколько сгенерировать паролей: ')
while not pass_count.isdigit():
    pass_count = input('Неверно! Введите число, сколько сгенерировать паролей: ')
else:
    pass_count = int(pass_count)

print('В пароле нужны большие буквы? 1 - да, 0 - нет')
upper_on = input()
while upper_on != '1' or upper_on != '0':
    upper_on = input('Введите корректные данные! 1 - да, 0 - нет')
else:
    upper_on = int(upper_on)

print('В пароле нужны маленькие буквы? 1 - да, 0 - нет')
lower_on = input()
while lower_on != '1' or lower_on != '0':
    lower_on = input('Введите корректные данные! 1 - да, 0 - нет')
else:
    lower_on = int(lower_on)

print('В пароле нужны символы "!#$%&*+-=?@^_?"? 1 - да, 0 - нет')
punctuation_on = input()
while punctuation_on != '1' or punctuation_on != '0':
    punctuation_on = input('Введите корректные данные! 1 - да, 0 - нет')
else:
    punctuation_on = int(punctuation_on)

print('Желаете исключить из пароля трудночитаемые символы"il1Lo0O"? 1 - да, 0 - нет')
ambiguous_on = input()
while ambiguous_on != '1' or ambiguous_on != '0':
    ambiguous_on = input('Введите корректные данные! 1 - да, 0 - нет')
else:
    ambiguous_on = int(ambiguous_on)
