# Дана строка. Замените в этой строке все появления буквы h
# на букву H, кроме первого и последнего вхождения

s = input()

new = s[s.find('h') + 1:s.rfind('h')]
print(s[:s.find('h') + 1] + new.replace('h', 'H') + s[s.rfind('h'):])
