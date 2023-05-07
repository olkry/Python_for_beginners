# Write a program that calculates the cost of three computers,
# consisting of a monitor, a system unit, a keyboard, and a mouse.
# Напишите программу, которая считает стоимость трех компьютеров,
# состоящих из монитора, системного блока, клавиатуры и мыши.

monitor = int(input('monitor cost'))
system_unit = int(input('system unit cost'))
keyboard = int(input('keyboard cost'))
mouse = int(input('mouse cost'))
print((monitor + system_unit + keyboard + mouse) * 3)
