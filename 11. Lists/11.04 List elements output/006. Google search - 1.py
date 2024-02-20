# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
#
# Формат входных данных
# На вход программе подаются натуральное число n — количество строк,
# затем сами строки в указанном количестве, затем один поисковый запрос.
#
# Формат выходных данных
# Программа должна вывести все введенные строки, в которых встречается поисковый запрос.
#
# Примечание. Поиск не должен быть чувствителен к регистру символов.

input_list = []

for _ in range(int(input())):
    input_list.append(input())

key_word = input()
lists_for_key = []

for lists in input_list:
    if key_word.lower() in lists.lower():
        lists_for_key.append(lists)

print(*lists_for_key, sep='\n')
