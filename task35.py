'''
Задача №35:
В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, чтобы выполнялось условие:
    A[i] - 1 = A[i-1].
Найти его.
'''

from random import randint

n = randint(15, 30)  # случайным образом задаем количество элементов
rand = randint(2, n-2)  # случайным образом задаем пропущенный элемент


def Get_massive(n, rand):  # функция заполнения массива
    a = []
    for item in range(1, n+1):
        if item != rand:
            a.append(item)
        else:
            continue
    return a


with open('task35.txt', 'w') as data:  # записываем файл с данными
    str = [str(i) for i in Get_massive(n, rand)]
    str = ' '.join(str)
    data.writelines(str)

print('Задан массив: ', *Get_massive(n, rand))

with open('task35.txt', 'r') as data:  # читаем данные из файла в виде строки
    massive = data.read()

massive = massive.split()  # переводим в массив строк
massive = list(map(int, massive))  # переводим в массив чисел

for i in range(1, len(massive)-1):  # ищем пропущенный элемент, выводим на печать
    if massive[i] != massive[i-1]+1:
        print('Не хватает элемента ', massive[i]-1)
        break
print()
