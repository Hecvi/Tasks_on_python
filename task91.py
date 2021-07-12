# Даны два натуральных числа n и m. Сократите дробь (n / m), то есть
# выведите два других числа p и q таких, что (n / m) = (p / q) и
# дробь (p / q) — несократимая. Решение оформите в виде функции
# ReduceFraction(n, m), получающая значения n и m и возвращающей
# кортеж из двух чисел: return p, q.
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m))
# Вводятся два натуральных числа


def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b:
        b = gcd(a % b, b)
    return b


def ReduceFraction(n, m):
    return n // gcd(n, m), m // gcd(n, m)


print(*ReduceFraction(int(input()), int(input())))
