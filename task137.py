# Циклически сдвиньте элементы списка вправо(A[0] переходит на место
# A[1], A[1] на место A[2], ..., последний элемент переходит на место A[0])
# Используйте минимально возможное количество операций присваивания.
# Измените начальный список и вывдите ответ с помощью print(*listName)


# list = list(map(int, input().split()))
# len = len(list) - 1
# last = list[len]
# while len >= 0:
#     if len == 0:
#         list[len] = last
#     else:
#         list[len] = list[len - 1]
#     len -= 1
# print(*list)


list = list(map(int, input().split()))
last = list[len(list) - 1]
for i in range(len(list) - 1, -1, -1):
    list[i] = list[i - 1]
list[0] = last
print(*list)


# a = list(map(int, input().split()))
# a.insert(0, a[-1])
# a.pop()
# print(*a) простейшее решение!!!! Блин
