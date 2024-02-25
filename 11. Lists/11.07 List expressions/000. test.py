# Дополните приведенный код, используя списочное выражение так, чтобы получить новый список,
# содержащий строки исходного списка, где у каждой строки удалён первый символ.

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# # new_keywords = [char[1:len(char)] for char in keywords]
# new_keywords = [char[1:] for char in keywords]
#
# print(new_keywords)

# Дополните приведенный код, используя списочное выражение, так чтобы получить новый список, содержащий длины строк исходного списка.

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# lengths = [len(element) for element in keywords]
#
# print(lengths)


# Дополните приведенный код списочным выражением, чтобы получить новый список, содержащий только слова длиной не менее пяти символов (включительно).

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [element for element in keywords if len(element) >= 5]
#
# print(new_keywords)
#
# Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел-палиндромов от 100 до 1000 (включительно).
#
# Примечание. Результирующий список должен состоять из целых чисел.

palindromes = [number for number in range(100, 1001) if str(number) == str(number)[::-1]]

print(palindromes)