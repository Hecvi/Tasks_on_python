# Напишите программу, которая по данному числу n от 1 до 9 выводит
# на экран n флагов. Изображение одного флага имеет размер 4×4 символов,
# между двумя соседними флагами также имеется пустой (из пробелов) столбец
# Разрешается вывести пустой столбец после последнего флага. Внутри каждого
# флага должен быть записан его номер — число от 1 до n


def num(s, k):
    i = 1
    while i <= k:
        print(s[0] + str(i) + s[2:], end=' ')
        # print('|' + str(i) + ' ' + '/', end=' ')
        i += 1


n = int(input())
print('+___ ' * n)
num('|  /', n)
print()
print('|__\\ ' * n)
print('|    ' * n)