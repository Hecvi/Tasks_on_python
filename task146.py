# Даны два списка, упорядоченных по возрастанию (каждый список состоит из
# различных элементов). Найдите пересечение множеств элементов этих списков,
# то есть те числа, которые являются элементами обоих списков. Алгоритм должен
# иметь сложность O(len(A)+len(B)). Решение оформите в виде функции
# Intersection(A, B). Функция должна возвращать список пересечения данных
# списков в порядке возрастания элементов. Модифицировать исходные списки
# запрещается. Программа получает на вход два возрастающих списка, каждый в
# отдельной строке. Программа должна вывести последовательность возрастающих
# чисел, являющихся элементами обоих списков


def intersection(list1, list2):
    list3, len1, len2 = [], -len(list1), -len(list2)
    while len1 and len2:
        if list1[len1] < list2[len2]:
            len1 += 1
        elif list1[len1] > list2[len2]:
            len2 += 1
        else:
            list3.append(list1[len1])
            len1 += 1
            len2 += 1
    return list3


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(*intersection(list1, list2))
