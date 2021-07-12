# Напишите программу, которая выбирает из полученной последовательности
# квадраты целых чисел выводит их в обратном порядке. Использовать массив
# для хранения последовательности не разрешается.
# Во входных строках записаны целые числа, по одному в каждой строке.
# В последней строке записано число 0.
# Программа должна вывести элементы полученной последовательности, которые
# представляют собой квадраты целых чисел, в обратном порядке в одну строчку,
# разделив их пробелами. Если таких нет, программа должна вывести число 0


def quadro(i):
    num = int(input())
    if num == 0 and i == 0:
        return print(0)
    elif num == 0:
        return
    if num % (num ** 0.5) == 0:
        i += 1
        quadro(i)
        return print(num, end=' ')
    quadro(i)


quadro(0)
