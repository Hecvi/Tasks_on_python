# Даны пять действительных чисел: x, y, xc, yc, r.
# Проверьте, принадлежит ли точка (x,y) кругу с центром (xc, yc) и радиусом r
# Если точка принадлежит кругу, выведите слово YES, иначе выведите слово NO
# Решение должно содержать функцию IsPointInCircle(x, y, xc, yc, r),
# возвращающую True, если точка принадлежит кругу и False, если не принадлежит
# Основная программа должна считать координаты точки, вызвать функцию
# IsPointInCircle и в зависимости от возвращенного значения вывести на экран
# необходимое сообщение. Функция IsPointInCircle не должна содержать
# инструкцию if

from math import sqrt


def IsPointInSquare(x, y, xc, yc, r):
    return sqrt((x - xc) ** 2 + (y - yc) ** 2) <= r


xc, yc = float(input()), float(input())
x, y, r = float(input()), float(input()), float(input())
if IsPointInSquare(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
