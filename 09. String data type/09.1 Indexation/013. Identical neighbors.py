# На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней одинаковых соседних символов.
#
# Формат входных данных
# На вход программе подается одна строка.
#
# Формат выходных данных
# Программа должна вывести количество одинаковых соседних символов.

input_string = input()
count = 0

for i in range(1, len(input_string)):
    if input_string[i] == input_string[i-1]:
        count += 1

print(count)

print('-----------')

s = input()
n = len(s)
cnt = 0

for i in range(n - 1):
    if s[i] == s[i + 1]:
        cnt += 1

print(cnt)