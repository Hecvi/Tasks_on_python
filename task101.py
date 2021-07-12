# Напишите программу, которая находит в массиве элемент, самый близкий
# по величине к данному числу.В первой строке задается одно натуральное
# число N, не превосходящее 1000 – размер массива. Во второй строке
# содержатся N чисел – элементы массива (целые числа, не превосходящие
# по модулю 1000). В третьей строке вводится одно целое число x, не
# превосходящее по модулю 1000. Вывести значение элемента массива, ближайшее
# к x. Если таких чисел несколько, выведите любое из них


n, elems, num = int(input()), list(map(int, input().split())), int(input())
max, min = 2000, 2000
for i in range(n):
    if abs(num - elems[i]) <= min:
        min = abs(num - elems[i])
        max = elems[i]
print(max)
