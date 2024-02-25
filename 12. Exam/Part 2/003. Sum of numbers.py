# На вход программе подается строка текста, содержащая натуральные числа.
# Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Строковый метод join() работает только со списком строк.

input_line = input().split()
plus_list = ''

for i in range(len(input_line)):
    if i != len(input_line) - 1:
        plus_list += f'{input_line[i]}+'
    else:
        plus_list += f'{input_line[i]}='

print(plus_list, sum(int(i) for i in input_line), sep='')

seq = input().split()
expression = "+".join(seq)

sm = 0
for el in seq:
    sm += int(el)
expression += f"={sm}"

print(expression)
