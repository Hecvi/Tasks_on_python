"""
На Новом проспекте для разгрузки было решено пустить два новых автобусных
маршрута на разных участках проспекта. Известны конечные остановки каждого
из автобусов. Определите количество остановок, на  которых можно пересесть с
одного автобуса на другой. Вводятся четыре числа, не превосходящие 100,
задающие номера конечных остановок. Сначала для первого, потом второго
автобуса (см. примеры и рисунок). Ваша программа должна выводить одно
число – искомое количество остановок
"""

data = list(map(int, input().split()))
bus1, bus2 = sorted([data[0], data[1]]), sorted([data[2], data[3]])
res = set(range(bus1[0], bus1[1] + 1)) & set(range(bus2[0], bus2[1] + 1))
print(len(res))
