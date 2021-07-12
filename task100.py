# По данным целым числам n и k (0≤k≤n) вычислите C из n по k.
# Решение оформите в виде функции C(n, k)


def c(n, k):
    if k == 0 or k == n:
        return 1
    return c(n - 1, k) + c(n - 1, k - 1)


print(c(int(input()), int(input())))
