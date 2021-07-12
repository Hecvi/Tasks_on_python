# Дано натуральное число n. Напечатайте все n-значные нечетные
# натуральные числа в порядке убывания


n, sum = int(input()), 0
tmp = n

while n:
    sum += 9 * 10 ** (n - 1)
    n -= 1

for step in range(sum, 10 ** (tmp - 1) - 1, -1):
    if step % 2 != 0:
        print(step, end=' ')

# n = int(input())
# maxNum = 10 ** n - 1
# minNum = 10 ** (n - 1)
# for i in range(maxNum, minNum - 1, -2):
#     print(i, end=' ')
