# Задача №20: Определить, присутствует ли в заданном списке строк, некоторое число

lst_len = int(input("Введите количество строк для создания списка: "))
lst = [input(f"Введие {i+1} строку: ") for i in range(lst_len)]
number = input("Введите число для поиска: ")
flag = False
for i in lst:
    if number in i:
        flag = True
        break
print("Присутствует" if flag else "Не присутствует")