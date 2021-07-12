# Возводить в степень можно гораздо быстрее, чем за n умножений!
# Для этого нужно воспользоваться следующими рекуррентными соотношениями:
# aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n. Реализуйте алгоритм
# быстрого возведения в степень. Если вы все сделаете правильно,то сложность
# вашего алгоритма будет O(logn).
# Вводится действительное число a и целое неотрицательное число n


def step(a, n):
    if n % 2 != 0:
        return a * step(a, n - 1)
    return (a ** 2) ** (n / 2)


print(step(float(input()), int(input())))