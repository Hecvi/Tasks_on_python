"""
Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в
виде ЕГЭ, каждый из них оценивается целым числом от 0 до 100 баллов. При этом
абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку) по любому
экзамену из конкурса выбывают. Остальные абитуриенты участвуют в конкурсе по
сумме баллов за три экзамена. В конкурсе участвует N человек, при этом
количество мест равно K. Определите проходной балл, то есть такое количество
баллов, что количество участников, набравших столько или больше баллов не
превосходит K, а при добавлении к ним абитуриентов, набравших наибольшее
количество баллов среди непринятых абитуриентов, общее число принятых
абитуриентов станет больше K. Программа получает на вход количество мест K.
Далее идут строки с информацией об абитуриентах, каждая из которых состоит из
имени (текстовая строка содержащая произвольное число пробелов) и трех чисел
от 0 до 100, разделенных пробелами. Используйте для ввода файл input.txt с
указанием кодировки utf8 (для создания такого файла на своем компьютере в
программе Notepad++ следует использовать кодировку UTF-8 без BOM). Программа
должна вывести проходной балл в конкурсе. Выведенное значение должно быть
минимальным баллом, который набрал абитуриент, прошедший по конкурсу
Также возможны две ситуации, когда проходной балл не определен.
Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок,
программа должна вывести число 0. Если количество имеющих равный максимальный
балл абитуриентов больше чем K, программа должна вывести число 1.
Используйте для вывода файл output.txt с указанием кодировки utf8
"""


def checkList(newList):
    for elem in newList:
        if elem < 40:
            return 0
    return 1


with open('input.txt', 'r', encoding='utf8') as file:
    mas = []
    num = int(file.readline())
    for line in file:
        tmpList = [line.split()[-3], line.split()[-2], line.split()[-1]]
        newList = list(map(int, tmpList))
        if checkList(newList):
            mas.append(sum(newList))
if len(mas) <= num:
    print(0)
elif mas.count(max(mas)) > num:
    print(1)
else:
    tmpMas = sorted(set(mas), reverse=True)
    for elem in range(len(tmpMas)):
        num -= mas.count(tmpMas[elem])
        if num == 0:
            print(tmpMas[elem])
            break
        elif num < 0:
            print(tmpMas[elem - 1])
            break
