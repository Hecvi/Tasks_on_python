# Выведите значение наименьшего нечетного элемента списка, гарантируется,
# что хотя бы один нечётный элемент в списке есть.
# Вводится список чисел. Все числа списка находятся на одной строке


def min(list):
    for i in list:
        if i % 2 != 0:
            min = i
            for i in list:
                if i % 2 != 0 and i < min:
                    min = i
            return print(min)


list = list(map(int, input().split()))
min(list)


# intList = list(map(int, input().split()))
# list = [item for item in intList if item % 2 != 0] #новый список, состоящий только из нечётных элементов
# print(min(list))
