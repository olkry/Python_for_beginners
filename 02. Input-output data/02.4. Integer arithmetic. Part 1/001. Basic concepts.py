# All the previous programs we wrote dealt with textual data.
# Indeed, the input() command reads a line of text.
# However, in many cases we need to work with numbers.
# To create a variable of an integer data type in Python,
# you need to omit the quotes when declaring the variable.
#
# Все предыдущие программы, которые мы писали, работали с текстовыми данными.
# Действительно, команда input() считывает строку текста.
# Однако во многих случаях нам нужно работать именно с числами.
# Чтобы в Python создать переменную целого типа данных,
# нужно опустить кавычки при объявлении переменной.

num1 = 7            # num1 - это число
num2 = 10           # num2 - это число
num3 = num1 + num2  # num3 - это число
print(num3)

# In Python, as in mathematics, there are 4 basic operations that can be performed on numbers (+, −, *, /).
# В языке Python, как и в математике, над числами можно совершать 4 основные операции (+, −, *, /).

a = 3
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Convert string to integer. To convert a string to an integer, we use the int() command.
# Consider the following code:
# Преобразование строки к целому числу. Для того, чтобы преобразовать строку к целому числу,
# мы используем команду int(). Рассмотрим следующий код:

s = '1992'
year = int(s)

# In order to explicitly indicate that you want to work with variables of an integer type, you need to write this:
# Для того, чтобы явно указать, что требуется работать с переменными целого типа, надо написать так:

num1 = int(input())
num2 = int(input())
print(num1 + num2)

# Converting an integer to a string.
# To convert an integer to a string, we use the str() command. Consider the following code:
# Преобразование целого числа к строке.
# Для того, чтобы преобразовать целое число в строку, мы используем команду str(). Рассмотрим следующий код:

num = 17
s = str(17)

