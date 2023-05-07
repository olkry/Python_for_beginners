# Write a program that determines if a year with a given number ends in two zeros.
# If the year ends, then print "YES", otherwise print "NO".
#
# Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля.
# Если год оканчивается, то выведите «YES», иначе выведите «NO».

year = int(input())
end_dig = year % 100
if end_dig == 00:
    print('YES')
else:
    print('NO')