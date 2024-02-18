# Напишите программу, выводящую следующий список:
# #
# # ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# # Формат выходных данных
# # Программа должна вывести указанный список.
# #
# # Примечание 1. Последний элемент списка должен состоять из 26 символов z.
# # Примечание 2. Английский алфавит (для копирования) 😇:
# # abcdefghijklmnopqrstuvwxyz

alpha = 'abcdefghijklmnopqrstuvwxyz'
list_alpha = []

for i in range(len(alpha)):
    list_alpha.append(alpha[i] * (i + 1))
print(list_alpha)

print('-----------------')

res = []
for i in range(26):
    cur = ""
    for j in range(i + 1):
        cur += chr(ord("a") + i)

    res.append(cur)

print(res)
