number = int(input())

print(bin(number)[2:], oct(number)[2:], hex(number)[2:].upper(), sep='\n')

# ==================

n = int(input())
[print(f(n)[2:].upper()) for f in (bin, oct, hex)]