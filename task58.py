# Дана строка, в которой буква h встречается как минимум два раза.
# Выведите измененную строку: повторите последовательность символов,
# заключенную между первым и последним появлением буквы h два раза
# (сами буквы h не входят в повторяемый фрагмент, т. е. их повторять не надо)

s = input()

first = s.find('h')
tmp = s[::-1]
last = tmp.find('h')
print(s[:first + 1] + s[first + 1:len(s) - 1 - last] * 2, end='')
print(s[len(s) - 1 - last:])
