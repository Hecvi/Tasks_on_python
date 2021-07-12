# Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂.
# Определите, можно ли разместить одну из этих коробок внутри другой,
# при условии, что поворачивать коробки можно только на 90 градусов вокруг
# ребер. Программа получает на вход числа A₁,B₁,C₁,A₂,B₂,C₂.
# Программа должна вывести одну из следующих строчек:
# Boxes are equal, если коробки одинаковые,
# The first box is smaller than the second one, если первая коробка
# может быть положена во вторую,
# The first box is larger than the second one, если вторая коробка
# может быть положена в первую,
# Boxes are incomparable, во всех остальных случаях.

a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

if a1 > b1:
    (a1, b1) = (b1, a1)
if b1 > c1:
    (b1, c1) = (c1, b1)
if a1 > b1:
    (a1, b1) = (b1, a1)
if a2 > b2:
    (a2, b2) = (b2, a2)
if b2 > c2:
    (b2, c2) = (c2, b2)
if a2 > b2:
    (a2, b2) = (b2, a2)
if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print('The first box is smaller than the second one')
elif a1 >= a2 and b1 >= b2 and c1 >= c2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')