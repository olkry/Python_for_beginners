# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и
# возвращает значение True, если пароль является надежным и False - в противном случае.
#
# Пароль является надежным если:
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

# объявление функции
def is_password_good(password):
    if len(password) >= 8:
        big, little, number = 0, 0, 0
        for char in password:
            if char.isdigit():
                number += 1
            elif char == char.upper():
                big += 1
            elif char == char.lower():
                little += 1
        if big >= 1 and little >= 1 and number >= 1:
            return True
        else:
            return False
    return False
# ================================
# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     for c in password:
#         if c.isupper():
#             flag1 = True
#         elif c.islower():
#             flag2 = True
#         elif c.isdigit():
#             flag3 = True
#     return flag1 and flag2 and flag3
# ==================================
#
# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     if password.isupper() or password.islower() or password.isalpha() or password.isdigit():
#         return False
#
#     return True

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
