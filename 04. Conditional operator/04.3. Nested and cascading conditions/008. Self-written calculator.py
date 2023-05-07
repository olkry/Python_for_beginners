# Write a program that reads two integers and a string from the keyboard.
# If this string is one of the four mathematical symbols
# operations (+, -, *, /), then print the result of applying this operation
# to the numbers entered earlier, otherwise print "Invalid operation".
# If the user wants to divide by zero, display the text "You can't divide by zero!".
#
# Напишите программу, которая считывает с клавиатуры два целых числа и строку.
# Если эта строка является обозначением одной из четырёх математических
# операций (+, -, *, /), то выведите результат применения этой операции
# к введённым ранее числам, в противном случае выведите «Неверная операция».
# Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».

num1, operator, num2 = int(input('Число ')), input(), int(input())
if num2 == 0 and operator == '/':
    print('На ноль делить нельзя!')
elif operator != '+' and operator != '-' and operator != '/' and operator != '*':
    print('Неверная операция')
else:
    if operator == '+':
        print(num1 + num2)
    if operator == '-':
        print(num1 - num2)
    if operator == '/':
        print(num1 / num2)
    if operator == '*':
        print(num1 * num2)
