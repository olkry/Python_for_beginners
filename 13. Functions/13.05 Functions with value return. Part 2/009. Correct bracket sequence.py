# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
# состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной
# скобочной последовательностью и False в противном случае.
#
# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ),
# где каждой открывающей скобке найдется парная закрывающая скобка
# (при этом каждая открывающая скобка должна быть левее соответствующей ей закрывающей скобки).

# объявление функции
def is_correct_bracket(text):
    if text[0] == '(' and text[-1] == ')':
        count = 0
        for char in text:
            if count >= 0:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
        if count == 0:
            return True
    return False
# =============================
#
# def is_correct_bracket(text):
#     while "()" in text:
#         text = text.replace("()", "")
#
#     return text == ""

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))