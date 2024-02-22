# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу, которая выводит инициалы человека.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

input_string = input().split()
initials = ''
# initials = '.'.join(elem[0] for elem in input_string)

for elem in input_string:
    initials += ''.join(elem[0]) + '.'

print(initials)

print('-----------')
full_name = input().split()
first_name, patronymic, last_name = full_name[0], full_name[1], full_name[2]

print(first_name[0], patronymic[0], last_name[0], sep=".", end=".")

print('--------------')
full_name = input().split()
print(full_name[0][0], full_name[1][0], full_name[2][0], sep=".", end=".")
