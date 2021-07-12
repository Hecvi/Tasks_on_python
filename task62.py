# Даны действительные коэффициенты a, b, c, при этом a != 0
# Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.
# Вводятся три действительных числа. Если уравнение имеет два корня,
# выведите два корня в порядке возрастания, если один корень — выведите
# одно число, если нет корней — не выводите ничего

from math import sqrt

a, b, c = float(input()), float(input()), float(input())

d = b ** 2 - 4 * a * c
if d > 0:
    root1 = round(((-b) - sqrt(d)) / (2 * a), 6)
    root2 = round(((-b) + sqrt(d)) / (2 * a), 6)
    if root1 < root2:
        print(root1, root2)
    else:
        print(root2, root1)
elif d == 0:
    print((-b) / (2 * a))
else:
    print()
