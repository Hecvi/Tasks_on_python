# Даны два четырёхзначных числа A и B. Выведите все четырёхзначные числа
# на отрезке от A до B, запись которых является палиндромом
# Вводятся два целых числа A и B

for i in range(int(input()), int(input()) + 1):
    pal = tuple(str(i))
    if pal[0] == pal[3] and pal[1] == pal[2]:
        print(i)