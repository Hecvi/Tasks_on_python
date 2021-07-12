# Переставьте элементы данного списка в обратном порядке, затем выведите
# элементы полученного списка. Эта задача отличается от предыдущей тем,
# что вам нужно изменить значения элементов самого списка, поменяв местами
# A[0] c A[n-1], A[1] с A[n-2], а затем вывести элементы списка подряд
# Предлагается в учебных целях проделать это вручную, например, не используя
# срезов и стандартных функций


list = list(map(int, input().split()))
len = len(list) - 1
i = 0
while i <= len // 2:
    list[i], list[len - i] = list[len - i], list[i]
    i += 1
print(*list)


# lst = list(map(int, input().split()))
# for i in range(len(lst) // 2):
#     lst[i], lst[-i - 1] = lst[-i - 1], lst[i]
# print(*lst)
