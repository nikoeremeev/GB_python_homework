'''
Задача №27:
Строка содержит набор чисел. Показать большее и меньшее число. \
    Символ-разделитель - пробел.
'''

str = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Максимальное число: {max(str)}.")
print(f"Минимальное число: {min(str)}.\n")
