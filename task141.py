# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось
# определить своё место в строю.Помогите ему это сделать. Программа
# получает на вход невозрастающую последовательность натуральных чисел,
# означающих рост каждого человека в строю. После этого вводится число
# X – рост Пети. Все числа во входных данных натуральные и не превышают 200
# Выведите номер, под которым Петя должен встать в строй. Если в строю есть
# люди с одинаковым ростом,таким же, как у Пети, то он должен встать после них


elems, x = list(map(int, input().split())), int(input())
for i in range(len(elems)):
    if elems[i] < x:
        print(i + 1)
        break
    elif i + 1 == len(elems) and elems[i] >= x:
        print(len(elems) + 1)
