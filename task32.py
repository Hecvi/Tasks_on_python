# В доме несколько подъездов. В каждом подъезде одинаковое количество квартир.
# Квартиры нумеруются подряд, начиная с единицы. Может ли в некотором подъезде
# первая квартира иметь номер x, а последняя – номер y?
# Вводятся два натуральных числа x и y (x ≤ y).
# Выведите слово YES (заглавными латинскими буквами), если такое возможно,
# и NO в противном случае.

low = int(input())
up = int(input())

if (low - 1) % (up - low + 1) == 0:
    print('YES')
else:
    print('NO')
