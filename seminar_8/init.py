from read_data import read_data


def init():
    if not (len(read_data()) > 0):
        
        with open("name.csv", 'a+') as file:
            file.write("id;surname;name;class;status\n")

        with open("adress.csv", 'a+') as file:
            file.write("id;city;street;house;apartament;other\n")

        with open("class.csv", 'a+') as file:
            file.write("id;row;col\n")
