# By default, the print() command takes several arguments (parameters),
# outputs them separated by one space, and then puts a newline.
# This behavior can be changed using the optional named
# parameters sep (separator, separator) and end (end).
# По умолчанию команда print() принимает несколько аргументов (параметров),
# выводит их через один пробел, после чего ставит перевод строки.
# Это поведение можно изменить, используя необязательные именованные
# параметры sep (separator, разделитель) и end (окончание).

print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**')

# If you do not need to do a line feed or you need to specify a special ending,
# then you must explicitly specify a value for the 'end' parameter.
# Если перевод строки делать не нужно или требуется указать специальное окончание,
# то следует явно указать значение для параметра end.

print('a', 'b', 'c', end='@')
print('d', 'e', 'f', end='@@')
print()

# The 'sep' and 'end' parameters can be used together. Consider the following code:
# Параметры sep и end можно использовать вместе. Рассмотрим следующий код:

print('a', 'b', 'c', sep='*', end='finish')
print('d', 'e', 'f', sep='**', end='^__^')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='#')
print('m', 'n', 'o', sep='/', end='!')
print()

# The default values for the sep and end parameters are as follows:
# sep=' ' # space
# end='\n' # newline

# Значения по умолчанию у параметров sep и end следующие:
# sep=' '   # пробел
# end='\n'  # перевод строки

# If more than one newline is needed after the output, then the following code must be used:
# Если после вывода данных нужно более одного перевода строки, то необходимо использовать следующий код:
print('Python', end='\n\n\n')
