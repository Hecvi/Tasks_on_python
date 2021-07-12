# Даны два целочисленных списка A и B, упорядоченных по неубыванию. Объедините
# их в один упорядоченный список С (то есть он должен содержать len(A)+len(B)
# элементов). Решение оформите в виде функции merge(A, B), возвращающей новый
# список. Алгоритм должен иметь сложность O(len(A)+len(B)). Модифицировать
# исходные списки запрещается. Использовать функцию sorted и метод sort
# запрещается. Программа получает на вход два неубывающих списка, каждый в
# отдельной строке. Программа должна вывести последовательность неубывающих
# чисел, полученных объединением двух данных списков


def merge(list1, list2):
    list3, len1, len2 = [], -len(list1), -len(list2)
    len_all = len1 + len2
    while len_all:
        if len1 and not len2:
            list3.append(list1[len1])
            len1 += 1
        elif not len1 and len2:
            list3.append(list2[len2])
            len2 += 1
        elif list1[len1] <= list2[len2]:
            list3.append(list1[len1])
            len1 += 1
        else:
            list3.append(list2[len2])
            len2 += 1
        len_all += 1
    return list3


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(*merge(list1, list2))
