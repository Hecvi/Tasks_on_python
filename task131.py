# По данному натуральному n вычислите сумму 1²+2²+3²+...+n²

n = int(input())
sum = 0

for i in range(n + 1):
    sum += i ** 2
print(sum)
