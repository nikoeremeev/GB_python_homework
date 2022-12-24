# Задача №14: Подсчитать сумму цифр в вещественном числе.

number = float(input("Введите вещественное число: "))

lst = list(str(number).split('.'))
summ = 0
for i in lst:
    for j in i:
        summ += int(j)
print(f"Сумма цифр вещественного числа равна = {summ}")

# улучшение программы
new_sum = sum(map(int, str(number).replace('.', '')))
print(f"Сумма цифр вещественного числа равна = {new_sum}")
