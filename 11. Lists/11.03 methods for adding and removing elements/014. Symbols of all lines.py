# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает список из символов всех строк, а затем выводит его.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список состоящий из символов всех введенных строк.
#
# Примечание. В результирующем списке могут содержаться одинаковые символы.

all_symbols = []

for i in range(int(input())):
    strg = input()
    all_symbols.extend(strg)

print(all_symbols)

print('----------------------')

print(list(''.join([input() for _ in range(int(input()))])))