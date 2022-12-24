'''
Задача №37.	
Дан список чисел. Создать список в который попадают числа,\
    описывающие возрастающую последовательность и \
        содержащие максимальное количество элементов. 
Пример: 
    [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7];
    [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7].
Порядок элементов менять нельзя!
'''
from random import *

nums = [randint(1, 9) for i in range(21)]
print('Задан список: ', nums)


def get_create(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups


print('Последовательность: ', get_create(nums))

largest = 0
index = 0

for i in range(len(nums)):
    if len(get_create(nums[i:])) > largest:
        largest = len(get_create(nums[i:]))
        index = i

print('Итого, создан список: ', nums[index:])
print('Итого, последовательность: ', get_create(nums[index:]), '\n')
