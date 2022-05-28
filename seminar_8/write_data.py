# модуль

def write_data(data, name):
    with open(name, 'a+') as file:
        file.write(";".join(map(str, data)))
        file.write(f"\n")


def count_data(name):
    with open(name, 'r') as file:
        data = file.read()
    return data.count('\n')


