'''
Задача №43.	
Дана последовательность чисел. 
Получить список уникальных элементов заданной последовательности.
Пример: 
    [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10].
'''

from random import *

nums = [randint(1, 15) for i in range(21)]
print('Задан список: ', nums, '\n')

nums1 = list(filter(lambda x: nums.count(x) == 1, nums))    # первое решение
nums2 = [i for i in nums if nums.count(i) == 1]             # второе решение

print('Список уникальных элементов: ', nums1)
print('Список уникальных элементов: ', nums2, '\n')
