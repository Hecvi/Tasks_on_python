# Дан список, заполненный произвольными целыми числами. Найдите в этом
# списке два числа, произведение которых максимально. Выведите эти числа
# в порядке неубывания. Решение должно иметь сложность O(n), где n - размер
# списка. То есть сортировку использовать нельзя


elements = list(map(int, input().split()))
if len(elements) > 0:
    plus_min = 0
    plus_max = 0
    minus_min = 0
    minus_max = 0
    for elem in elements:
        if elem > 0:
            if elem >= plus_max:
                plus_min = plus_max
                plus_max = elem
            elif elem > plus_min:
                plus_min = elem
        elif elem < 0:
            if elem <= minus_max:
                minus_min = minus_max
                minus_max = elem
            elif elem < minus_min:
                minus_min = elem
    if plus_min * plus_max >= minus_min * minus_max:
        print(plus_min, plus_max)
    else:
        print(minus_max, minus_min)
