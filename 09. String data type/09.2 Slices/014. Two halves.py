# На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части, переставит их местами и выведет на экран.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
word = input()
slice_center = int(len(word) / 2)

if int(len(word)) % 2 != 0:
    word = word[slice_center + 1:] + word[:slice_center + 1]
else:
    word = word[slice_center:] + word[:slice_center]

print(word)

print('--------------------')

s = input()
n = len(s)

a = s[:(n + 1) // 2]
b = s[(n + 1) // 2:]

print(b + a)

print('-----------------')

s = input()
x = len(s)
a = x // 2 + x % 2
print(s[a:] + s[:a])
