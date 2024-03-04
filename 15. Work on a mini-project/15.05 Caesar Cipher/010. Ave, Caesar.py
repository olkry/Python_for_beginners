# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.
#
# Формат входных данных
# На вход программе подается строка текста на английском языке.
#
# Формат выходных данных
# Программа должна вывести зашифрованный текст в соответствии с условием задачи.
#
# Примечание. Символы, не являющиеся английскими буквами, не изменяются.

input_string = input().split()
code = ''

for string in input_string:
    shift = 0
    for char in string:
        if char.isalpha():
            shift += 1
    for char in string:
        if char.isalpha():
            if char == char.lower():
                encode = ord(char) + shift
                if encode > ord('z'):
                    code += chr(encode - (ord('z') - ord('a') + 1))
                else:
                    code += chr(encode)
            else:
                encode = ord(char) + shift
                if encode > ord('Z'):
                    code += chr(encode - (ord('Z') - ord('A') + 1))
                else:
                    code += chr(encode)
        else:
            code += char
    code += ' '

print(code)

# ========================
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# s_old = input()
# words = s_old.split()  # разбиваем строку на слова
#
# s_new = ""
# for word in words:
#     shift = sum([int(letter.lower() in alphabet) for letter in word])  # считаем длину каждого слова
#
#     for letter in word:
#         if letter in alphabet:  # проверяем, что это строчная буква
#             old_letter_position = alphabet.index(letter)
#             letter = alphabet[(old_letter_position + shift) % 26]
#
#         elif letter.lower() in alphabet:  # проверяем, что это прописная буква
#             old_letter_position = alphabet.index(letter.lower())
#             letter = alphabet[(old_letter_position + shift) % 26].upper()
#
#         s_new += letter
#
#     s_new += " "
#
# print(s_new)
