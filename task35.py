# Для данного числа n<100 закончите фразу “На лугу пасется...”
# одним из возможных продолжений: “n коров”, “n корова”, “n коровы”,
# правильно склоняя слово “корова”.

cows = int(input())

if cows % 10 == 1 and cows != 11:
    print(cows, 'korova')
elif cows % 10 == 2 or cows % 10 == 3 or cows % 10 == 4:
    if cows < 12 or cows > 14:
        print(cows, 'korovy')
    else:
        print(cows, 'korov')
else:
    print(cows, 'korov')
