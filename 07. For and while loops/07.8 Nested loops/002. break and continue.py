for i in range(3):
    for j in range(3):
        print(i, j)

print('-------------------------------------')

for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)

print('-------------------------------------')

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)
        
print('-------------------------------------')
