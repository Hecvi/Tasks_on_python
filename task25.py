# Последовательность состоит из натуральных чисел и завершается числом 0
# Определите значение второго по величине элемента в этой последовательности,
# то есть элемента, который будет наибольшим, если из последовательности
# удалить одно вхождение наибольшего элемента.
# Вводится последовательность натуральных чисел, оканчивающаяся числом 0
# (само число 0 в последовательность не входит, а служит как признак ее
# окончания)

nums = int(input())
max = nums
smax = 0

while nums != 0:
    nums = int(input())
    if nums >= max:
        smax = max
        max = nums
    elif nums > smax:
        smax = nums
print(smax)