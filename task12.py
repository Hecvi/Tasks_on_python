hours1 = int(input())
min1 = int(input())
sec1 = int(input())
hours2 = int(input())
min2 = int(input())
sec2 = int(input())

clock1 = hours1 * 3600 + min1 * 60 + sec1
clock2 = hours2 * 3600 + min2 * 60 + sec2
print(clock2 - clock1)
