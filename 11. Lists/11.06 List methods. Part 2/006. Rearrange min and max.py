# На вход программе подается строка текста, содержащая различные натуральные числа.
# Из данной строки формируется список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести строку текста в соответствии с условием задачи.
#
# Примечание. Используйте подходящие встроенные функции и списочные методы.

input_numbers = input().split()
int_list = [int(i) for i in input_numbers]

max_char = max(int_list)
max_index = int_list.index(max_char)
min_char = min(int_list)
min_index = int_list.index(min_char)
int_list[max_index] = min_char
int_list[min_index] = max_char


print(*int_list)

print('---------------')

seq = []
for el in input().split():
    seq.append(int(el))

mx_ind = seq.index(max(seq))
mn_ind = seq.index(min(seq))
seq[mx_ind], seq[mn_ind] = seq[mn_ind], seq[mx_ind]

print(*seq)
