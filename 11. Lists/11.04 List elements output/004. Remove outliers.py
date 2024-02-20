# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.
# На вход программе подается натуральное число n, а затем n различных натуральных чисел.
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел,
# а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

input_list = []

for num in range(int(input())):
    input_list.append(int(input()))

maximum = input_list.index(max(input_list))
del input_list[maximum]
minimum = input_list.index(min(input_list))
del input_list[minimum]

print(*input_list, sep='\n')

print('-----------------')

n = int(input())

mx_ind = 0
mn_ind = 0
seq = []
for _ in range(n):
    seq.append(int(input()))

for i in range(n):
    if seq[i] > seq[mx_ind]:
        mx_ind = i
    if seq[i] < seq[mn_ind]:
        mn_ind = i

del seq[max(mx_ind, mn_ind)]
del seq[min(mx_ind, mn_ind)]

print(*seq, sep="\n")
