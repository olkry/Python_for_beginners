# The print() command is used to display data on the screen.
# Inside the parentheses, we write what we want to display on the screen.
# If this is text, then be sure to indicate it inside quotes.
# Quotes can be single or double. Just be sure to put the same before and after the text.

# Для вывода данных на экран используется команда print().
# Внутри круглых скобок пишем, что хотим вывести на экран.
# Если это текст, то обязательно указываем его внутри кавычек.
# Кавычки могут быть одинарными или двойными. Только обязательно ставим одинаковые до и после текста.

print('Мы изучаем язык Python')

# Remember: quotes can be either single or double. The next two lines do the same thing.
# Запомни: кавычки могут быть и одинарными, и двойными. Следующие две строки делают одно и то же.

print('Python')
print("Python")

# The print() command allows you to specify multiple arguments, in which case they must be separated by commas.
# Команда print() позволяет указывать несколько аргументов, в таком случае их надо отделять запятыми.

print('Скоро я', 'буду программировать', 'на языке', 'Python!')

# The print() command with an empty argument list simply inserts a new empty line. For example:
# Команда print() с пустым списком аргументов просто вставляет новую пустую строку. Например:

print('Какой хороший день!')
print()
print('Работать мне не лень!')

# Why is it possible to use both single and double quotes in Python to frame text?
# The answer is very simple - quotes are often part of the text.
# And so that Python can correctly recognize such text, we use different ones:
# Почему в Python можно использовать как одинарные, так и двойные кавычки для обрамления текста?
# Ответ очень прост — часто кавычки это часть текста.
# И чтобы Python мог правильно распознать такой текст, пользуемся разными:

print('В тексте есть "двойные" кавычки')
print("В тексте есть 'одинарные' кавычки")

