# По данному натуральному n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл

mult = 0
n = int(input())
for i in range(1, n + 1):
    sum = 1
    for j in range(1, i + 1):
        sum *= j
    mult += sum
print(mult)
