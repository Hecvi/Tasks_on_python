"""
В выборах Президента Российской Федерации побеждает кандидат, набравший свыше
половины числа голосов избирателей. Если такого кандидата нет, то во второй
тур выборов выходят два кандидата, набравших наибольшее число голосов
Каждая строка входного файла содержит имя кандидата, за которого отдал голос
один избиратель. Известно, что общее число кандидатов не превосходит 20, но
в отличии от предыдущих задач список кандидатов явно не задан. Читайте данные
из файла input.txt с указанием кодировки utf8. Если есть кандидат, набравший
более 50% голосов, программа должна вывести его имя. Если такого кандидата
нет, программа должна вывести имя кандидата, занявшего первое место, затем
имя кандидата, занявшего второе место. Выводите данные в файл output.txt с
указанием кодировки utf8
"""


dictOfCand, sumCand = {}, 0
output = open('output.txt', 'w', encoding='utf8')
with open('input.txt', encoding='utf8') as file:
    for line in file:
        tmpStr = line.strip()
        if tmpStr not in dictOfCand:
            dictOfCand[tmpStr] = 0
        dictOfCand[tmpStr] += 1
tmpList = sorted(list(dictOfCand.items()), key=lambda x: (-x[1], x[0]))
for elem in tmpList:
    sumCand += int(elem[1])
if int(tmpList[0][1]) / sumCand > 1/2:
    print(tmpList[0][0], file=output)
else:
    print(tmpList[0][0], tmpList[1][0], sep='\n', file=output)
