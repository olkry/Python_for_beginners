# The Mad Titan Thanos has collected all 6 Infinity Stones and intends to wipe
# out half the population of the universe with a snap of his fingers. Moreover,
# if the population of the Universe is an odd number, then the titan will show
# mercy and round the number of survivors up. Help the Avengers count the number of survivors.
#
# Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить
# половину населения Вселенной по щелчку пальцев. При этом если население Вселенной
# является нечетным числом, то титан проявит милосердие и округлит количество выживших
# в большую сторону. Помогите Мстителям подсчитать количество выживших.

population = int(input())
print((population + 1) // 2)