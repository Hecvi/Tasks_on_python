# В этой задаче необходимо проверить, делится ли число A на число B нацело.
# Использовать можно только арифметические операции, использование любых
# видов ветвлений, функций и т.п. запрещено.
# Вводятся два натуральных числа A и B.
# Выведите "YES", если A кратно B и "NO" в противном случае


a = int(input())
b = int(input())
c = a % b
print('YES' * 0 ** c, end='')
print('NO' * 0 ** 0 ** c)
