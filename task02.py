# Задача №2: Найти максимальное из пяти чисел.

a, b, c, d, e = int(input("Введите 1 число: ")),\
    int(input("Введите 2 число: ")),\
    int(input("Введите 3 число: ")),\
    int(input("Введите 4 число: ")),\
    int(input("Введите 5 число: "))
maxNum = a
if maxNum < b:
    maxNum = b
if maxNum < c:
    maxNum = c
if maxNum < d:
    maxNum = d
if maxNum < e:
    maxNum = e
print(f"Максимальное число = {maxNum}")
