# В списке все элементы попарно различны. Поменяйте местами минимальный
# и максимальный элемент этого списка. Вводится список целых чисел. Все
# числа списка находятся на одной строке


list = list(map(int, input().split()))
min = list.index(min(list))
max = list.index(max(list))
list[min], list[max] = list[max], list[min]
print(*list)
