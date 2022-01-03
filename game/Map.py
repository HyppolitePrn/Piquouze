from os import system
def map_print(Avion, Terminal, Hall, Parking,os, hall_loc, terminal_loc, avion_loc, duty, duty_map):
    Boss = "[Ä]"
    space = " "
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print(("________")* 11)
    print("\n")
    if avion_loc == "1":
        print((space * 6), "Boss", Boss)
        for v in Avion:
            print((space * 3), "Avion", v)
    if terminal_loc == "1":
        for v in Terminal:
            print((space * 21), "Terminal", v)
    if hall_loc == "1":
        for v in Hall:
            print((space * 11), "Hall", v)
    for v in Parking:
        print((space * 29), "Parking", v)
    print("\n")
    print(("________")* 11)
    if duty == "1" and duty_map == "1":
        Hall[2][0] = "[$]"

def map_create(l):
    shape = "[ ]"
    i = 0
    liste = []
    while i < l:
        j = 0
        liste.append([])
        while j < 4:
            liste[i].append(shape)
            j = j + 1
        i = i + 1
    return liste

def map_place():
    Avion = map_create(5)
    Terminal = map_create(4)
    Hall = map_create(3)
    Parking = map_create(5)
    return Avion,Terminal, Hall, Parking

Avion, Terminal, Hall, Parking = map_place()

