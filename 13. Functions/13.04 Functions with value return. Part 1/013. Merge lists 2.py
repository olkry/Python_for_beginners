# На вход программе подается числоn, а затемn строк, содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки в о
# дин отсортированный список с помощью функции quick_merge(), а затем выводит его.


def quick_merge():
    result_list = []
    for _ in range(int(input())):
        input_list = input().split()
        for char in input_list:
            result_list.append(int(char))

    return sorted(result_list)


print(*quick_merge())


# =================================
#
# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     else:  # иначе прицепляем остаток другого списка
#         result += list2[p2:]
#
#     return result
#
#
# n = int(input())
# seq = []
# for _ in range(n):
#     seq.append([int(el) for el in input().split()])
#
# while len(seq) >= 2:
#     list1 = seq.pop(0)
#     list2 = seq.pop(0)
#
#     new_list = quick_merge(list1, list2)
#     seq.append(new_list)
#
# print(*seq[0])
# ====================================
def quick_merge(input_list):
    input_list.sort()
    return input_list


list_my = []
for _ in range(int(input())):
    list += [int(c) for c in input().split()]

print(*quick_merge(list_my))
