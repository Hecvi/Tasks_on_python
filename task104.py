# Дан список. Определите, является ли он монотонно возрастающим(то есть
# верно ли, что каждый элемент этого списка больше предыдущего).Выведите
# YES, если массив монотонно возрастает и NO в противном случае.Решение
# оформите в виде функции IsAscending(A).В данной функции должен быть
# один цикл while, не содержащий вложенных условий и циклов — используйте
# схему линейного поиска


def IsAscending(list):
    i = 1
    min = list[0]
    while i < len(list) and list[i] > min: # порядок условий имеет значение!!!
        min = list[i]
        i += 1
    return bool(i == len(list))


# def IsAscending(list):
#     for i in range(0, len(list)):
#         if i != 0 and list[i] <= list[i - 1]:
#             return 0
#     return 1


if IsAscending(list(map(int, input().split()))):
    print('YES')
else:
    print('NO')
