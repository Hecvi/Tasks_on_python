# Дана строка. Получите новую строку, вставив между каждыми двумя
# символами исходной строки символ *. Выведите полученную строку

s = input()
len = len(s)
i = 0

while i < len:
    print(s[i], end='')
    if i + 1 != len:
        print('*', end='')
    i += 1

# можно и так:
# print(*input(), sep="*")