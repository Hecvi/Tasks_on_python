"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N.
Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с
номерами от lᵢ до rᵢ включительно. Определите, какие кегли остались стоять на
месте. Программа получает на вход количество кеглей N и количество бросков K.
Далее идет K пар чисел lᵢ, rᵢ, при этом 1 ≤ lᵢ ≤ rᵢ ≤ N ≤ 100.
Программа должна вывести последовательность из N символов, где j-й символесть
“I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита
"""

pins, balls = list(map(int, input().split()))
pinsList = [i for i in range(1, pins + 1)]
len_pinList = len(pinsList)
for elem in range(balls):
    start, finish = list(map(int, input().split()))
    for i in range(len_pinList):
        if pinsList[i] != '.' and start <= pinsList[i] <= finish:
            pinsList[i] = '.'
for elem in range(len_pinList):
    if pinsList[elem] != '.':
        pinsList[elem] = 'I'
s = (''.join(map(str, pinsList)))
print(s)
