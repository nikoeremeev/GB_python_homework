def init():
    with open("name.csv", 'a+') as file:
        if file.read().count('\n') == 0:
            file.write("id;surname;name;class;status\n")

    with open("adress.csv", 'a+') as file:
        if file.read().count('\n') == 0:
            file.write("id;city;street;house;apartament;other\n")

    with open("class.csv", 'a+') as file:
        if file.read().count('\n') == 0:
            file.write("id;row;col\n")
