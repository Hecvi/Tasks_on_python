"""
В олимпиаде по информатике принимало участие несколько человек. Определите
и выведите средние баллы участников олимпиады в 9 классе, в 10 классе, в 11
классе. Информация о результатах олимпиады записана в файле, каждая строка
которого имеет вид:
Фамилия и имя — текстовые строки, не содержащие пробелов. Класс - одно из
трех чисел 9, 10, 11. Балл - целое число от 0 до 100. В этой задаче файл
необходимо считывать построчно, не сохраняя содержимое файла в памяти целиком
Выведите три числа: средние баллы по 9 классу, по 10 классу, по 11 классу.
Входной файл в кодировке utf-8
(используйте open('input.txt', 'r', encoding='utf8'))
"""

with open('input.txt', 'r', encoding='utf8') as file:
    class9 = []
    class10 = []
    class11 = []
    for line in file:
        myList = list(line.split())
        num = int(myList[2])
        val = int(myList[3])
        if num == 9:
            class9.append(val)
        elif num == 10:
            class10.append(val)
        else:
            class11.append(val)
print(sum(class9) / len(class9), sum(class10) / len(class10), end=' ')
print(sum(class11) / len(class11))

# Вот так можно было масштабировать задачу
# inFile = open('input.txt', 'r', encoding='utf8')
# s = [0] * 12
# m = [0] * 12
# for line in inFile:
#     l = line.split()
#     m[int(l[2])] += 1
#     s[int(l[2])] += int(l[3])
# print(s[9] / m[9], s[10] / m[10], s[11] / m[11])
# inFile.close()
