'''
Задача №21: 
Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
Примеры:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3;
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5;
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1;
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1;
список: [], ищем: "123", ответ: -1.
'''


def my_func(lst, find_str):
    if lst.count(find_str) > 1:
        k = lst.index(find_str)
        print(lst.index(find_str, k+len(find_str)))
    else:
        print(-1)


lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
f = "qwe"
my_func(lst, f)
lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
f = "йцу"
my_func(lst, f)
lst = ["йцу", "фыв", "ячс", "цук", "йцукен"]
f = "йцу"
my_func(lst, f)
lst = ["123", "234", 123, "567"]
f = "123"
my_func(lst, f)
lst = []
f = "123"
my_func(lst, f)
