# Даны вещественные числа a, b, c, d, e, f. Известно,
# что система линейных уравнений:
# ax + by = e
# cx + dy = f
# имеет ровно одно решение. Выведите два числа x и y,
# являющиеся решением этой системы.
# Вводятся шесть чисел a, b, c, d, e, f

a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

y = (e * c - a * f) / (c * b - a * d)
x = (f * b - d * e) / (b * c - d * a)
print(x, y)
