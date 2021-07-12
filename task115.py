# По данному натуральному n≤9 выведите лесенку из n ступенек,
# i-я ступенька состоит из чисел от 1 до i без пробелов

# n = int(input())
# for i in range(1, n + 1):
#     k = 1
#     while k <= i:
#         print(k, end='')
#         k += 1
#     if i != n:
#         print()

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    if i != n:
        print()
