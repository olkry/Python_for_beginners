# На вход программе подается строка текста.
# Напишите программу, использующую списочное выражение, которая выводит все цифровые символы данной строки.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Программу можно написать в одну строку кода.

print(*(number for number in input() if number.isdigit()), sep='')

# digits = [el for el in input() if el.isdigit()]
# print(*digits, sep="")
