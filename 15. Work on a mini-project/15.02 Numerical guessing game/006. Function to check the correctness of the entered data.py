# Напишите функцию is_valid() в которую передается один строковый аргумент.
# Функция возвращает значение True если переданный аргумент является целым числом от 1 до 100 и False в противном случае.

def is_valid(line):
    return 1 <= int(line) <= 100


print(is_valid(0))
print(is_valid(152))
print(is_valid(1))
print(is_valid(25))
print(is_valid(100))
