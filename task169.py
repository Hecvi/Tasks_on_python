"""
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится. Программа получает
на вход количество стран N. Далее идет N строк, каждая строка начинается с
названия страны, затем идут названия городов этой страны. Название каждого
города состоит из одного слова. В следующей строке записано число M, далее
идут M запросов — названия каких-то M городов, перечисленных выше. Для каждого
из запроса выведите название страны, в котором находится данный город
"""


# dictOfCities = {}
# for elem in range(int(input())):
#     tmpList = list(input().split())
#     if tmpList[0] not in dictOfCities:
#         dictOfCities[tmpList[0]] = tmpList[1:]
#     else:
#         dictOfCities[tmpList[0]] += tmpList[1:]
# for elem in range(int(input())):
#     tmp = input().strip()
#     for key in dictOfCities:
#         if tmp in dictOfCities[key]:
#             print(key)
#             break

dictOfCities = {}
for elem in range(int(input())):
    tmpList = list(input().split())
    country, tmpList = tmpList[0], tmpList[1:]
    for city in tmpList:
        if city not in dictOfCities:
            dictOfCities[city] = country
for elem in range(int(input())):
    findCity = input().strip()
    if findCity in dictOfCities:
        print(dictOfCities[findCity])
