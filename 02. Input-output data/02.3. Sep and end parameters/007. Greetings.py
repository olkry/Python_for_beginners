# Write a program that greets the user by displaying the word "Hello" (without the quotes),
# followed by a comma and a space, followed by the user's name and an exclamation point.
#
# Напишите программу, которая приветствует пользователя, выводя слово «Привет» (без кавычек),
# после которого должна стоять запятая и пробел, а затем введенное имя и восклицательный знак.

name = input()
print("Привет", name, sep=', ', end='!')
