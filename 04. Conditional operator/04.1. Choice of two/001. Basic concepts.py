
# Conditional if-else statement
# Условный оператор if-else

# In Python, condition testing is done with the if keyword.
# В Python проверка условия осуществляется при помощи ключевого слова if.

answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')

# There are 6 basic comparison operators in Python.
# В Python существует 6 основных операторов сравнения.

#   Выражение  	Описание
# if x > 7	если x больше 7
# if x < 7	если x меньше 7
# if x >= 7	если x больше либо равен  7
# if x <= 7	если x меньше либо равен  7
# if x == 7	если x равен  7
# if x != 7	если x не равен  7

# Comparison operators in Python can be chained together (unlike most other programming languages,
# where you need to use logical connectives for this), for example, a == b == c or 1 <= x <= 10.
# The following code checks to see if the value of the age variable in the range from 3 to 6:
# Операторы сравнения в Python можно объединять в цепочки (в отличии от большинства других языков
# программирования, где для этого нужно использовать логические связки), например, a == b == c или 1 <= x <= 10.
# Следующий код проверяет, находится ли значение переменной age в диапазоне от 3 до 6:

age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок')

if a == b == c:
    print('числа равны')
else:
    print('числа не равны')


