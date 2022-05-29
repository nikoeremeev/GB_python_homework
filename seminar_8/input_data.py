from write_data import count_data

def input_data():
    dct = dict()
    Id = count_data("name.csv") 
    dct["id"] = Id     # list[0] - это Id ученика
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["class"] = input('Введите Класс: ')
    dct["status"] = input('Введите Статус: ')
    dct["row"] = input('Введите Ряд: ')
    dct["col"] = input('Введите Номер парты: ')
    dct["city"] = input('Введите Город: ')
    dct["street"] = input('Введите Улица: ')
    dct["house"] = input('Введите Дом: ')
    dct["apartament"] = input('Введите Квартира: ')
    dct["other"] = input('Введите Примечание: ')
    # dct["id"] = Id     # list[0] - это Id ученика
    # dct["surname"] = "Фамилия"
    # dct["name"] = "Имя"
    # dct["class"] = "Класс"
    # dct["status"] = "статус"
    # dct["row"] = "ряд"
    # dct["col"] = "номер парты"
    # dct["city"] = "город"
    # dct["street"] = "улица"
    # dct["house"] = "дом"
    # dct["apartament"] = "квартира"
    # dct["other"] = "примечание"
    return dct