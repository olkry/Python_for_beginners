# n schoolchildren divide k tangerines equally, the non-divisible remainder remains in the basket.
# How many whole tangerines will each student get? How many whole tangerines will be left in the basket?

# n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине.
# Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?

schoolchildren = int(input('Сколько школьников? '))
tangerines = int(input('Сколько мандаринов? '))
print("Каждый возьмет по ", tangerines // schoolchildren)
print("В корзине остается ", tangerines % schoolchildren)