# На вход программе подается одна строка. Напишите программу, которая выводит элементы строки с индексами 0, 2, 4, ... в столбик.
#
# Формат входных данных
# На вход программе подается одна строка.

word = input()

for i in range(0, len(word), 2):
    print(word[i])

print('-------------------')
count = 2
for char in word:
    if count % 2 == 0:
        print(char)
    count += 1
