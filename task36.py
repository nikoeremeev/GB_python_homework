'''
Задача №36:
Дан список чисел. 
Создать список, в который попадают числа, \
    описываемые возрастающую последовательность. 
Пример: 
    [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
Порядок элементов менять нельзя!
'''

nums = [3, 1, 2, 3, 4, 6, 1, 7]

# Первый вариант


def get_create(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups


print(get_create(nums))

# Второй вариант


def get_create2(nums):
    ups = []
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
            ups.append(nums[i])
    return ups


print(get_create2(nums))
