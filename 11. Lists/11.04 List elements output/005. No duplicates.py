# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Считайте, что все строки состоят из строчных символов.

input_list = []

for _ in range(int(input())):
    input_list.append(input())

test_list = []

for length in input_list:
    if length not in test_list:
        test_list.append(length)

print(*test_list, sep='\n')

print('-------------')

n = int(input())

seq = []
for _ in range(n):
    s = input()
    if s not in seq:
        seq.append(s)

print(*seq, sep="\n")
