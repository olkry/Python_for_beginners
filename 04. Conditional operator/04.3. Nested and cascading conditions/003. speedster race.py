# Zoom challenged the Flash and offered him a fair fight in the form of a race around the magnetar.
# If you lose, this neutron star will charge up and destroy the world,
# so the Flash decided not to risk it for no reason, and ask his friend Cisco Ramon
# does it make sense to accept the challenge.
# Cisco received data that Zoom's speed is n and Flash's speed is k.
#
# Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара.
# В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир,
# поэтому Флэш решил не рисковать без причины, и узнать у своего друга Циско Рамона
# есть ли смысл принимать вызов.
# Циско получил данные, что скорость Зума равна n, а скорость Флэша равна k.

zoom, flash = int(input()), int(input())
if zoom < flash:
    print('YES')
elif zoom > flash:
    print('NO')
else:
    print("Don't know")
    