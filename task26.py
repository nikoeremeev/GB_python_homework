'''
Задача №26: 
Дано число. Составить список чисел Фибоначчи, \
    в том числе для отрицательных индексов. 
 т.е. для k = 8, список будет выглядеть так:
    [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи.
'''


def findFib(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return findFib(index-1) + findFib(index-2)


n = int(input(
    "Введите число для преобразовывания десятичного числа в двоичное:\n"))
lst = [findFib(i) for i in range(1, n+2)]
print(lst)
lst = lst[::-1] + lst[1:]
print(lst, '\n')
