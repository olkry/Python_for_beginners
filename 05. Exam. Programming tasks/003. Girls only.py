# The football team recruits girls from 10 to 15 years old inclusive.
# Write a program that asks for the age and gender of an applicant,
# using the gender designation of the letters m (from male - male) and f (from female - woman)
# and determines whether the applicant is suitable for joining the team or not.
# If the applicant is suitable, then print "YES", otherwise print "NO".
# The input to the program is a natural number - the age of the applicant
# and the gender letter m (male) or f (female).
#
# Футбольная команда набирает девочек от 10 до 15 лет включительно.
# Напишите программу, которая запрашивает возраст и пол претендента,
# используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина)
# и определяет подходит ли претендент для вступления в команду или нет.
# Если претендент подходит, то выведите «YES», иначе выведите «NO».
# На вход программе подаётся натуральное число – возраст претендента
# и буква обозначающая пол m (мужчина) или f (женщина).


age, gender = int(input()), input()
if 10 <= age <= 15 and gender == 'f':
    print('YES')
else:
    print('NO')