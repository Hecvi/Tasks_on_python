# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент, а значения
# всех элементов списка по модулю не превосходят 1000
# Вводится список чисел. Все числа списка находятся на одной строке


list = list(map(int, input().split()))

min = 1000
for i in list:
    if 0 < i < min:
        min = i
print(min)