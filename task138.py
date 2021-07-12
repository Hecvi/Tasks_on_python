"""
Дан список. Не изменяя его и не используя дополнительные списки, определите,
какое число в этом списке встречается чаще всего. Если таких чисел несколько,
выведите любое из них. Вводится список чисел. Все числа списка находятся на
одной строке.
"""


nums = list(map(int, input().split()))
len_nums = len(nums)
max = 0
number = nums[0]
for i in nums:
    count = nums.count(i)
    if count >= max:
        max = count
        number = i
print(number)
