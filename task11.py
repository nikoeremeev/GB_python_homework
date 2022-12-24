'''
Задача №11: 
Сформировать список из  N членов последовательности.
Для N = 5: 1, -3, 9, -27, 81 и т.д.
'''

number = int(input("Введите число: "))
lst = []
for i in range(number):
    lst.append((-3)**i)
print(f"Итоговая последовательность: {lst}")

# улучшение

lst = [(-3)**i for i in range(number)]
print(
    f"Итоговая последовательность после применения list comprehension: {lst}")
