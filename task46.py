# Переставьте цифры числа в обратном порядке
# Задано единственное число N

num = int(input())

while num // 10:
    print(num % 10, end='')
    num //= 10
print(num)
