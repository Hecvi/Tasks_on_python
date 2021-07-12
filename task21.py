sec = int(input())

hours = (sec // 3600) % 24
min = (sec // 60) % 60
sec = (sec % 3600) % 60
print(hours, ':', min // 10, min % 10, ':', sec // 10, sec % 10, sep='')
