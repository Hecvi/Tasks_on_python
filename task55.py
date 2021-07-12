# Дана строка. Найдите в этой строке второе вхождение буквы f
# и выведите индекс этого вхождения. Если буква f в данной строке
# встречается только один раз, выведите число -1, а если не встречается
# ни разу, выведите число -2. При решении этой задачи нельзя использовать
# метод count

s = input()
i = 0
sign = 1
buf = -1

count = s.find('f')
while count != -1:
    if count > buf:
        buf = count
        i += 1
    if i == 2 and sign:
        sign = 0
        print(count)
    count = s.find('f', count + 1)
if i == 1:
    print(-1)
elif i == 0:
    print(-2)

# s = input()
# a = s.find('f')
# b = s[:a] + s[a + 1:]
# c = b.find('f')
# if a == -1:
#     print(-2)
# elif c == -1:
#     print(-1)
# else:
#     print(c + 1)
