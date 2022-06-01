def print_line():
    print("-" * 13)

def print_tab(tab):
    print_line()
    for i in range(3):
        print ("|", tab[0+i*3], "|", tab[1+i*3], "|", tab[2+i*3], "|")
        print_line()