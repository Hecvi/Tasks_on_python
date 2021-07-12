# Дан список чисел. Выведите все элементы списка, которые больше предыдущего
# элемента. Вводится список чисел. Все числа списка находятся на одной строке


list = list(map(int, input().split()))
len = len(list)
for i in range(0, len):
    if i + 1 < len and list[i] < list[i + 1]:
        print(list[i + 1], end=' ')

# spisok = list(map(int, input().split()))
# prevNum = spisok[0]
# for i in spisok:
#     if i > prevNum:
#         print(i, end=' ')
#     prevNum = i

# spis = list(map(int, input().split()))
# for n in range(1, len(spis)):
#     if n != 0 and spis[n] > spis[n-1]:
#         print(spis[n], end=" ")