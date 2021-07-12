# Даны четыре действительных числа: x₁, y₁, x₂, y₂
# Напишите функцию distance(x1, y1, x2, y2), вычисляющую
# расстояние между точками (x₁,y₁) и (x₂,y₂). Считайте четыре
# действительных числа и выведите результат работы этой функции
# Вводятся четыре действительных числа

from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
print(distance(x1, y1, x2, y2))
