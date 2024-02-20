# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов,
# затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки, в которых встречаются одновременно все поисковые запросы.
#
# Формат входных данных
# На вход программе подаются натуральное число n — количество строк,
# затем сами строки в указанном количестве, затем число k, затем сами поисковые запросы.
#
# Формат выходных данных
# Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.
#
# Примечание. Поиск не должен быть чувствителен к регистру символов.

# input_list = [input() for _ in range(int(input()))]
# key_list = [input() for _ in range(int(input()))]
# serch_list = []
#
# for i in range(len(input_list)):
#     count = 0
#     for j in range(len(key_list)):
#         if key_list[j].lower() in input_list[i].lower():
#             count += 1
#     if count == len(key_list):
#         serch_list.append(input_list[i])
#
#
# print(*serch_list, sep='\n')

print('----------')

n = int(input())

strings = []
for _ in range(n):
    s = input()
    strings.append(s)

k = int(input())

search_queries = []
for _ in range(k):
    search_query = input()
    search_queries.append(search_query)

for s in strings:
    for search_query in search_queries:
        if search_query.lower() not in s.lower():
            break
    else:
        print(s)

