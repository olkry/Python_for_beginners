# На вход программе подается строка текста.
# Напишите программу, которая определяет, является ли введенная строка корректным телефонным номером.
# Строка текста является корректным телефонным номером, если она имеет формат:abc-def-hijk или7-abc-def-hijk,
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести «YES», если строка является корректным телефонным номером и «NO» в противном случае.
#
# Примечание. Телефонный номер должен содержать только цифры и символ -, а количество цифр в каждой группе должно быть правильным.

phone = input()

if '-' in phone:
    count = 0
    spl_phone = phone.split('-')
    for i in range(len(spl_phone)):
        if spl_phone[i] == '7':
            count += 1
        elif i == len(spl_phone) - 1 and len(spl_phone[i]) == 4 and spl_phone[i].isdigit():
            count += 1
        elif len(spl_phone[i]) == 3 and spl_phone[i].isdigit():
            count += 1
    print('YES' if count == len(spl_phone) else 'NO')

else:
    print('NO')

seq = input().split("-")
lens = [len(el) for el in seq]

if lens == [1, 3, 3, 4] and "".join(seq).isdigit() and seq[0] == "7":
    print("YES")
elif lens == [3, 3, 4] and "".join(seq).isdigit():
    print("YES")
else:
    print("NO")
    