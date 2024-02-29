# Добавьте подсчет попыток, сделанных пользователем. Когда число отгадано, программа должна показать количество попыток;
# Добавьте возможность генерации нового числа (повторная игра), после того, как пользователь угадал число;
# Добавить возможность указания правой границы для случайного выбора числа (от 1 до n).

from random import *


def is_valid(line):
    return 1 <= int(line) <= 100


print('Добро пожаловать в числовую угадайку')
print('В этой игре Вам предстоит найти загаданное число.')
print('До какого числа загадываем?')
limit = input()
while not limit.isdigit():
    print("Это не число")
    limit = input('Попробуйте снова: ')
hidden_number = randint(1, int(limit))
flag = True
count = 0
while flag:
    input_number = input(f'Введите число от 1 до {limit}: ')
    if input_number.isdigit() and is_valid(input_number):
        input_number = int(input_number)
        if input_number > hidden_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        elif input_number < hidden_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif input_number == hidden_number:
            print('Вы угадали, поздравляем!')
            print(f'И угадали с {count} попытки')
            print()
            print('Сыграем ещё? y = да, или введите любые другие символы для завершения.')
            agen = input()
            if agen not in 'yн':
                flag = False
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            hidden_number = randint(1, int(limit))

    else:
        print(f'А может быть все-таки введем целое число от 1 до {limit}?')