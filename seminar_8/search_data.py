# модуль поиска контакта

from read_data import read_data
from print_data import print_data

def search_data(word, data):
    if len(data) > 0:
        lst = []
        for item in data:
            if word in item:
                lst.append(item)
        if lst == []:
            return None
        else:
            return lst
    else:
        return None