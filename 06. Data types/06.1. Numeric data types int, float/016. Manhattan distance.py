# Walking around Manhattan, you can't get from point A to point B on the shortest path.
# Unless you know how to walk through walls, you will definitely have to walk along
# its parallel-perpendicular streets.
#
# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути.
# Если только вы не умеете проходить сквозь стены, вам обязательно придется идти вдоль
# его параллельно-перпендикулярных улиц.

start1, start2, finish1, finish2 = int(input()), int(input()), int(input()), int(input())
print(abs(start1 - finish1) + abs(start2 - finish2))
