"""
Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения
от 0 до 100 (100 включая). Отсортируйте этот список в порядке неубывания
элементов. Выведите полученный список. Решение оформите в виде функции
CountSort(A), которая модифицирует передаваемый ей список. Использовать
встроенные функции сортировки нельзя
"""


def countSort(myList):
    res = []
    mas = [0] * 101
    for elem in myList:
        mas[elem] += 1
    for elem in range(101):
        while mas[elem]:
            res.append(elem)
            mas[elem] -= 1
    return res


myList = list(map(int, input().split()))
print(*countSort(myList))
