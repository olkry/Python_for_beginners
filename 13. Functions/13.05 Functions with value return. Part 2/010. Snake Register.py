# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку
# в «верблюжьем регистре» и преобразует его в «змеиный регистр».

def convert_to_python_case(text):
    snake_case = text[0].lower()
    for char in text[1:]:
        if char == char.upper() and char.isalpha():
            snake_case += '_' + char.lower()
        else:
            snake_case += char.lower()
    return snake_case
# ==============================
#
# def convert_to_python_case(text):
#     new_text = ""
#     for el in text:
#         if not el == el.lower():  # проверяем, что элемент в верхнем регистре (пропускаем цифры)
#             new_text += "_" + el.lower()
#         else:
#             new_text += el
#
#     return new_text[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
