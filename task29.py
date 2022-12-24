# Задача №29: Найти НОК двух чисел.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
for i in range(a * b, 1, -1):
    if i % a == 0 and i % b == 0:
        nok = i
print('НОК = ', nok, '\n')
