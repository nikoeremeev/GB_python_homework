def check(tab):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if tab[each[0]] == tab[each[1]] == tab[each[2]]:
            return tab[each[0]]
    return False