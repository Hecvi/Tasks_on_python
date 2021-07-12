# Выведите элементы данного списка в обратном порядке, не изменяя сам список


list = list(map(str, input().split()))
print(*list[::-1])

# print(' '.join(input().split()[::-1]))
