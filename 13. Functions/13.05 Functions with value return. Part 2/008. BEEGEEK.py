# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
#
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка и False - в противном случае.

def is_valid_password(password):
    password = password.split(':')
    if len(password) == 3:
        if password[0] == (password[0])[::-1]:
            for num in range(2, int(password[1]) // + 1):
                if int(password[1]) % num == 0:
                    return False
            if int(password[2]) % 2 == 0:
                return True
    return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
