# Дан список чисел. Если в нем есть два соседних элемента одного знака,
# выведите эти числа. Если соседних элементов одного знака нет - не выводите
# ничего. Если таких пар соседей несколько - выведите первую пару.
# Вводится список чисел. Все числа списка находятся на одной строке


def twice(list):
    tmp = list[0]
    for i in list[1:]:
        if i > 0 and tmp > 0 or i < 0 and tmp < 0:
            return print(tmp, i)
        tmp = i


list = list(map(int, input().split()))
twice(list)
