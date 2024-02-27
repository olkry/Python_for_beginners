# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает
# значение True если указанный текст является палиндромом и False в противном случае.
#
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.

# объявление функции
def is_palindrome(text):
    test_line = ''
    for i in range(len(text)):
        if text[i].isalpha():
            test_line += text[i]
    return test_line.lower() == test_line.lower()[::-1]
# =================================
# def is_palindrome(text):
#     symbols = [' ', ',', '.', '!', '?', '-']
#     for c in symbols:
#         text = text.replace(c, '')
#     text = text.lower()
#     return text == text[::-1]
# ======================================
# def is_palindrome(text):
#     text = [i.lower() for i in text if i not in (',.!?- ')]
#     return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
