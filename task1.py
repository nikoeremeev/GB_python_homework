''' 
Задача №1: 
По двум заданным числам проверить является ли одно квадратом второго.
'''

numA = int(input("Введите первое число: "))
numB = int(input("Введите второе число: "))
if numA == numB ** 2 or numB == numA ** 2:
    print("ЯВЛЯЕТСЯ")
else:
    print("НЕ ЯВЛЯЕТСЯ")
