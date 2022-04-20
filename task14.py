# Задача №14: Подсчитать сумму цифр в вещественном числе.

number = float(input("Введите вещественное число: "))

lst = list(str(number).split('.'))
summ = 0
for i in lst:
    for j in i:
        summ += int(j)
print(f"Сумма цифр вещественного числа равна = {summ}")