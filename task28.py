'''
Задача №28:
Найти корни квадратного уравнения Ax² + Bx + C = 0:
    a.	Математикой;
    b.	Используя дополнительные библиотеки.
'''

from math import *
from random import *

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))
c = int(input("Введите число C: "))

D = b**2 - 4 * a * c
print("Дискриминант D = %.2f" % D)

if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif D == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
