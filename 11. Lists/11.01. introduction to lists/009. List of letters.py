# На вход программе подается одно число n. Напишите программу, которая выводит список,
# состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.
#
# Формат входных данных
# На вход программе подается натуральное число n,1≤n≤26.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

num = int(input())
alphabet = list('abcdefghijklmnopqrstuvwxyz')

print(alphabet[:num])

print('________________________')

string_char = ''

for i in range(num):
    string_char += chr(ord('a') + i)

print(list(string_char))
