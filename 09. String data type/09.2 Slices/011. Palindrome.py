# На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая определяет, является ли оно палиндромом.
#
# Формат входных данных
# На вход программе подается одно слово в нижнем регистре.
#
# Формат выходных данных
# Программа должна вывести «YES», если слово является палиндромом, и «NO» в противном случае.


word = input()
slice_center = int(len(word) / 2)

if int(len(word)) % 2 == 0:
    if word[:slice_center] == word[:slice_center-1:-1]:
        print('YES')
    else:
        print('NO')
if int(len(word)) % 2 == 1:
    if word[:slice_center] == word[:slice_center:-1]:
        print('YES')
    else:
        print('NO')


print('------------------')

s = input()

if s == s[::-1]:
    print("YES")
else:
    print("NO")