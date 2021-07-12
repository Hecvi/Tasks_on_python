# Напишите функцию, вычисляющую длину отрезка по координатам его концов
# С помощью этой функции напишите программу, вычисляющую периметр
# треугольника по координатам трех его вершин
# На вход программе подается 6 целых чисел — координат x₁, y₁, x₂,
# y₂, x₃, y₃ вершин треугольника. Все числа по модулю не превосходят 30 000
# Выведите значение периметра этого треугольника с точностью до 6 знаков
# после десятичной точки

from math import sqrt


def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def perimetr(x1, y1, x2, y2, x3, y3):
    s1 = dist(x1, y1, x2, y2)
    s2 = dist(x1, y1, x3, y3)
    s3 = dist(x2, y2, x3, y3)
    return s1 + s2 + s3


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
print(round((perimetr(x1, y1, x2, y2, x3, y3)), 6))
