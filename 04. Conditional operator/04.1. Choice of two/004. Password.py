# Write a program that compares the password and its confirmation.
# If they match, then the program displays: "Password accepted", otherwise: "Password not accepted".
#
# Напишите программу, которая сравнивает пароль и его подтверждение.
# Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».

p1, p2 = input(), input()
if p1 == p2:
    print('Пароль принят')
else:
    print('Пароль не принят')
