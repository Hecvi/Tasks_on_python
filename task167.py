"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если
таких слов несколько, выведите то, которое меньше в лексикографическом порядке
"""


myDict = {}
with open('input.txt', encoding='utf8') as file:
    for line in file:
        tmpList = line.split()
        for elem in tmpList:
            if elem not in myDict:
                myDict[elem] = 0
            myDict[elem] += 1
tmpList = list(myDict.items())
tmpList.sort(key=lambda i: (-i[1], i[0]))
print(tmpList[0][0])
