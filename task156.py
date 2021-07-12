"""
Во входной строке записана последовательность чисел через пробел. Для каждого
числа выведите слово YES (в отдельной строке), если это число ранее
встречалось в последовательности или NO, если не встречалось
"""


# list1 = list(map(int, input().split()))
# mas = []
# for elem in list1:
#     if elem in mas:
#         print('YES')
#     else:
#         mas.append(elem)
#         print('NO')


list1 = list(map(int, input().split()))
mas = set()
for elem in list1:
    if elem in mas:
        print('YES')
    else:
        mas.add(elem)
        print('NO')

"""
Удивительно, но видимо добавление элемента в set и прохождение по нему
работает быстрее, чем со списком, хотя в остальном код одинаковый
"""