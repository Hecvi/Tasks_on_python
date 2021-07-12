# Дан список чисел. Определите, сколько в этом списке элементов, которые
# больше двух своих соседей и выведите количество таких элементов.
# Вводится список чисел. Все числа списка находятся на одной строке

count = 0
myList = list(map(int, input().split()))
for i in range(0, len(myList)):
    if i != 0 and myList[i] > myList[i - 1]:
        if i + 1 != len(myList) and myList[i] > myList[i + 1]:
            count += 1
print(count)
