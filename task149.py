"""
В олимпиаде участвовало N человек. Каждый получил определенное количество
баллов, при этом оказалось, что у всех участников разное число баллов.
Упорядочите список участников олимпиады в порядке убывания набранных баллов
Программа получает на вход число участников олимпиады N. Далее идет N строк,
в каждой строке записана фамилия участника, затем, через пробел, набранное
им количество баллов. Выведите список участников (только фамилии) в порядке
убывания набранных баллов
"""

n = int(input())
mas = []
for line in range(n):
    mas.append(input().split())
mas.sort(key=lambda x: -int(x[1]))
for elem in mas:
    print(elem[0])
