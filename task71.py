# Дана последовательность натуральных чисел x₁, x₂ ..., xn
# Стандартным отклонением называется величина
# σ=sqrt(((x₁-s)²+(x₂-s)²+…+(xn-s)²) / (n-1))
# где s = ((x₁+x₂+…+xn) / n) — среднее арифметическое последовательности,
# а sqrt - квадратный корень. Определите стандартное отклонение для данной
# последовательности натуральных чисел, завершающейся числом 0.
# Вводится последовательность целых чисел, оканчивающаяся числом 0
# (само число 0 в последовательность не входит, а служит как признак
# ее окончания)

import math

n = int(input())
counter, sumsqr, sum = 0, 0, 0

while n:
    sum += n
    sumsqr += n ** 2
    counter += 1
    n = int(input())
print(round(math.sqrt((sumsqr - sum ** 2 / counter) / (counter - 1)), 11))
