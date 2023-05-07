# Write a program that, given the user's age, tells what age group he belongs to:
# up to 13 inclusive - childhood;
# from 14 to 24 - youth;
# from 25 to 59 - maturity;
# from 60 - old age.

# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.

a = int(input())
if 0 <= a <= 13:
    print('детство')
if 14 <= a <= 24:
    print('молодость')
if 25 <= a <= 59:
    print('зрелость')
if 60 <= a:
    print('старость')