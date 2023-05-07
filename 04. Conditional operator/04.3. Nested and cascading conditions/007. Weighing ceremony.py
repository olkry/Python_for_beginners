# Known weight of an amateur boxer (integer).
# It is known that the weight is such that a boxer can be assigned to one of three weight categories:
# Light weight - up to 60 kg;
# First welterweight - up to 64 kg;
# Welterweight - up to 69 kg.
# Write a program that determines which category a given boxer will compete in.
#
# Известен вес боксера-любителя (целое число).
# Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:
# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.

weight = int(input())
if weight < 60:
    print('Легкий вес')
elif 60 <= weight < 64:
    print('Первый полусредний вес')
else:
    print('Полусредний вес')
