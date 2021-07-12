"""
В данном списке из n≤10⁵ целых чисел найдите три числа,произведение которых
максимально. Решение должно иметь сложность O(n), где n - размер списка.
То есть сортировку использовать нельзя. Выведите три искомых числа в любом
порядке.
"""


def mult(number1, number2, number3):
    return number1 * number2 * number3


elements = list(map(int, input().split()))
len_elements = len(elements)
if len_elements > 0:
    sign = 0
    plus_list = [0, 0, 0]
    minus_list = [0, 0, 0]
    for elem in elements:
        if elem >= 0:
            sign = 1
            if elem >= plus_list[0]:
                plus_list[2] = plus_list[1]
                plus_list[1] = plus_list[0]
                plus_list[0] = elem
            elif elem >= plus_list[1]:
                plus_list[2] = plus_list[1]
                plus_list[1] = elem
            elif elem > plus_list[2]:
                plus_list[2] = elem
        elif elem < 0:
            if elem <= minus_list[0]:
                minus_list[2] = minus_list[1]
                minus_list[1] = minus_list[0]
                minus_list[0] = elem
            elif elem <= minus_list[1]:
                minus_list[2] = minus_list[1]
                minus_list[1] = elem
            elif elem < minus_list[2]:
                minus_list[2] = elem
    res_plus = mult(*plus_list)
    res_minus = mult(*minus_list)
    if len_elements == 3:
        print(*elements)
    elif len_elements > 3 and sign == 0:
        
    elif ((res_plus < mult(plus_list[0], minus_list[0], minus_list[1]) or
            plus_list[0] == 0) and sign == 1):
        print(plus_list[0], minus_list[0], minus_list[1])
    elif res_plus > 0:
        print(*plus_list)
    elif res_plus == 0 and plus_list[0] == 0 and sign == 1:
        print(*plus_list)
    else:
        print(*minus_list)
