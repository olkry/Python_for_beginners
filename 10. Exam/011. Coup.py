word = input()
first = word.find('h')
last = word.rfind('h')

print(word[:first] + word[last:first:-1] + word[last:])
