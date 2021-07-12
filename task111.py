# Найдите количество положительных элементов в данном списке


count = 0
list = list(map(int, input().split()))
for i in list:
    if i > 0:
        count += 1
print(count)
