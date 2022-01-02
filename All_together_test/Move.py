from Map import *
from Affichage import *
from fight import battle
from fight import inventory
from Mac_or_wind import os
from duty_free import duty_free
from liste import menu_ig
from mini_jeux import *
from pickle import *

def move(direction, position):
    shape = "[ ]"
    user = "[Ï]"
    i = 0
    if direction.lower() == "q":
        while i < len(position):
            j = 0
            while j < len(position[i]):
                if position[i][j] == user:
                    if j-1 < 0:
                        position[i][j] = user
                    else:
                        position[i][j] = shape
                        position[i][j-1] = user
                    return position
                j = j + 1
            i = i + 1
    if direction.lower() == "z":
        while i < len(position):
            j = 0
            while j < len(position[i]):
                if position[i][j] == user:
                    if i-1 < 0:
                        position[i][j] = user
                    else:
                        position[i][j] = shape
                        position[i-1][j] = user
                    return position
                j = j + 1
            i = i + 1
    if direction.lower() == "d":
        while i < len(position):
            j = 0
            while j < len(position[i]):
                if position[i][j] == user:
                    if j+1 >= len(position[i]):
                        position[i][j] = user
                    else:
                        position[i][j] = shape
                        position[i][j+1] = user
                    return position
                j = j + 1
            i = i + 1
    if direction.lower() == "s":
        while i < len(position):
            j = 0
            while j < len(position[i]):
                if position[i][j] == user:
                    if i+1 >= len(position):
                        position[i][j] = user
                    else:
                        position[i][j] = shape
                        position[i+1][j] = user
                    return position
                j = j + 1
            i = i + 1

    return position

def action(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map, player):
    stop = " "
    save = " "
    map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
    print("   Tapez 'menu' pour accéder aux contenues associé.")
    print("   Pour vous déplacer")
    direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
    while direction.lower() != "z" and direction.lower() != "s" and direction.lower() != "q" and direction.lower() != "d" and direction.lower() != "stop" and direction.lower() != "menu":
            map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
            print("   Tapez 'menu' pour accéder aux contenues associé.")
            print("   Pour vous déplacer")
            direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
    if direction.lower() == "stop":
            stop = "stop"
            if os == "mac":
                system("clear")
            elif os == "windows":
                system("cls")
    if direction.lower() == "menu":
        choice = " "
        if os == "mac":
            from menu_nav_mac import menu_nav_mac
            while choice != "Retour" and choice != "stop":
                system("clear")
                choice = menu_nav_mac(menu_ig)
                if choice == "stats":
                    stat_print(player, os)
                if choice == "equipment":
                    equipement_print(player, os)
                if choice == "argent":
                    argent_print(player, os)
                if choice == "inv":
                    inventory(player, os)
                if choice == "stop":
                    stop = "stop"
                    if os == "mac":
                        system("clear")
                    elif os == "windows":
                        system("cls")
                if choice == "save":
                    save = "save"
        elif os == "windows":
            from Menu_nav import menu_nav
            while choice != "Retour" and choice != "stop":
                system("cls")
                choice = menu_nav(menu_ig)
                if choice == "stats":
                    stat_print(player, os)
                if choice == "equipment":
                    equipement_print(player, os)
                if choice == "argent":
                    argent_print(player, os)
                if choice == "inv":
                    inventory(player, os)
                if choice == "stop":
                    stop = "stop"
                if choice == "save":
                    save = "save"
    return direction.lower(), stop, save

def verif_position(Avion, Terminal, Hall, Parking):
    user = "[Ï]"
    i = 0
    while i < len(Avion):
        j = 0
        while j < len(Avion[i]):
            if Avion[i][j] == user:
                localisation = Avion
                return localisation
            j = j + 1
        i = i + 1
    i = 0
    while i < len(Parking):
        j = 0
        while j < len(Parking[i]):
            if Parking[i][j] == user:
                localisation = Parking
                return localisation
            j = j + 1
        i = i + 1

    i = 0
    while i < len(Terminal):
        j = 0
        while j < len(Terminal[i]):
            if Terminal[i][j] == user:
                localisation = Terminal
                return localisation
            j = j + 1
        i = i + 1

    i = 0
    while i < len(Hall):
        j = 0
        while j < len(Hall[i]):
            if Hall[i][j] == user:
                localisation = Hall
                return localisation
            j = j + 1
        i = i + 1
    
def save_game(localisation, player, Parking, Avion, Hall, Terminal, duty_map, duty, citoyen3, citoyen2, citoyen1, antivax1,antivax2, antivax3, antivax4, antivax5, antivax6, antivax7, avion_loc, hall_loc, terminal_loc, list_sell):
    save_variable = open("save.pickle","wb")
    dump(localisation, save_variable)
    dump(player, save_variable)
    dump(Parking, save_variable)
    dump(Avion, save_variable)
    dump(Hall, save_variable)
    dump(Terminal, save_variable)
    dump(duty_map, save_variable)
    dump(duty, save_variable)
    dump(citoyen3, save_variable)
    dump(citoyen2, save_variable)
    dump(citoyen1, save_variable)
    dump(antivax1, save_variable)
    dump(antivax2, save_variable)
    dump(antivax3, save_variable)
    dump(antivax4, save_variable)
    dump(antivax5, save_variable)
    dump(antivax6, save_variable)
    dump(antivax7, save_variable)
    dump(avion_loc, save_variable)
    dump(hall_loc, save_variable)
    dump(terminal_loc, save_variable)
    dump(list_sell, save_variable)
    save_variable.close()
    return


def localisation_of_door_enemy_item(Avion, Terminal, Hall, Parking, start_var):
    stop = " "
    user = "[Ï]"
    shape = "[ ]"
    xavitna = [5, 6, 0, "Xavitna"]
    seukitpes = [8, 3, 0, "Seukitpes"]
    boss = [50, 30, 0, "Boss"]
    if start_var == "new":
        localisation = Parking
        hall_loc = "0"
        terminal_loc = "0"
        avion_loc = "0"
        antivax1 = "1"
        antivax2 = "1"
        antivax3 = "1"
        antivax4 = "1"
        antivax5 = "1"
        antivax6 = "1"
        antivax7 = "1"
        citoyen1 = "1"
        citoyen2 = "1"
        citoyen3 = "1"
        duty = "0"
        duty_map = "0"
        player = [["Stats:", "Pv:", 10, "/ Attaque:", 3, "/ Défense:", 0, "/ Lvl:", 1, "/ XP:", 0],
        ["Inventaire:", "Gel Hydroalcoolique", "Retour"],
        ["Equipement:"],
        ["Argent:", 0]]
        list_sell = [
        "Articles: ",
        "Gel Hydroalcoolique +5 hp (soin) : 10 ",
        "Masque chirurgical + 1 défense : 100",
        "Blouse de bataille + 3 défense : 100",
        "Seringue en adamantium +3 attaque : 100",
        "Retour"
]
    elif start_var == "load":
        loading = open("save.pickle","rb")
        localisation = load(loading)
        player = load(loading)
        Parking = load(loading)
        Avion = load(loading)
        Hall = load(loading)
        Terminal = load(loading)
        duty_map = load(loading)
        duty = load(loading)
        citoyen3 = load(loading)
        citoyen2 = load(loading)
        citoyen1 = load(loading)
        antivax1 = load(loading)
        antivax2 = load(loading)
        antivax3 = load(loading)
        antivax4 = load(loading)
        antivax5 = load(loading)
        antivax6 = load(loading)
        antivax7 = load(loading)
        avion_loc = load(loading)
        hall_loc = load(loading)
        terminal_loc = load(loading)
        list_sell = load(loading)
        loading.close()

    

    while stop == " ":
        save = " "
        xavitna = [5, 6, 0, "Xavitna"]
        seukitpes = [8, 3, 0, "Seukitpes"]
        direction, stop, save = action(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map, player)
        if save == "save":
            save_game(localisation, player, Parking, Avion, Hall, Terminal, duty_map, duty, citoyen3, citoyen2, citoyen1, antivax1,antivax2, antivax3, antivax4, antivax5, antivax6, antivax7, avion_loc, hall_loc, terminal_loc, list_sell)

        localisation = verif_position(Avion, Terminal, Hall, Parking)
        if localisation == Parking:
            Parking = move(direction, Parking)
        if localisation == Hall:
            if hall_loc == "0":
                hall_print(os)
            hall_loc = "1"
            Hall = move(direction, Hall)
        if localisation == Terminal:
            if terminal_loc == "0":
                terminal_print(os)
            terminal_loc = "1"
            Terminal = move(direction, Terminal)
        if localisation == Avion:
            if avion_loc == "0":
                avion_print(os)
            avion_loc = "1"
            Avion = move(direction, Avion)
        
        # je défini un interupteur pour afficher ou non le duty free
        if Hall[2][0] != user:
            duty_map = "1"
        # Je défini les portes de Parking vers Hall:
        if Parking[0][0] == user:
            direction, stop, save = action(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map, player)
            if save == "save":
                save_game(localisation, player, Parking, Avion, Hall, Terminal, duty_map, duty, citoyen3, citoyen2, citoyen1, antivax1,antivax2, antivax3, antivax4, antivax5, antivax6, antivax7, avion_loc, hall_loc, terminal_loc, list_sell)
            if direction.lower() == "z":
                Parking[0][0] = shape
                localisation = Hall
                if hall_loc == "0":
                    hall_print(os)
                hall_loc = "1"
                Hall[2][3] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
            else:
                Parking = move(direction, Parking)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
        # Je défini les portes de hall vers parking:
        if Hall[2][3] == user:
            direction, stop, save = action(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map, player)
            if save == "save":
                save_game(localisation, player, Parking, Avion, Hall, Terminal, duty_map, duty, citoyen3, citoyen2, citoyen1, antivax1,antivax2, antivax3, antivax4, antivax5, antivax6, antivax7, avion_loc, hall_loc, terminal_loc, list_sell)
            if direction.lower() == "s":
                Hall[2][3] = shape
                localisation = Parking
                Parking[0][0] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
            else:
                Hall = move(direction, Hall)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
        # Je défini les portes de Hall vers Terminal:
        if Hall[0][2] == user:
            direction, stop, save = action(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map, player)
            if save == "save":
                save_game(localisation, player, Parking, Avion, Hall, Terminal, duty_map, duty, citoyen3, citoyen2, citoyen1, antivax1,antivax2, antivax3, antivax4, antivax5, antivax6, antivax7, avion_loc, hall_loc, terminal_loc, list_sell)
            if direction.lower() == "z":
                Hall[0][2] = shape
                localisation = Terminal
                if terminal_loc == "0":
                    terminal_print(os)
                terminal_loc = "1"
                Terminal[3][0] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
            else:
                Hall = move(direction, Hall)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
        if Hall[0][3] == user:
            direction, stop, save = action(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map, player)
            if save == "save":
                save_game(localisation, player, Parking, Avion, Hall, Terminal, duty_map, duty, citoyen3, citoyen2, citoyen1, antivax1,antivax2, antivax3, antivax4, antivax5, antivax6, antivax7, avion_loc, hall_loc, terminal_loc, list_sell)
            if direction.lower() == "z":
                Hall[0][3] = shape
                localisation = Terminal
                if terminal_loc == "0":
                    terminal_print(os)
                terminal_loc = "1"
                Terminal[3][1] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
            else:
                Hall = move(direction, Hall)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
        # Je défini les portes de Terminal vers Hall:
        if Terminal[3][0] == user:
            direction, stop, save = action(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map, player)
            if save == "save":
                save_game(localisation, player, Parking, Avion, Hall, Terminal, duty_map, duty, citoyen3, citoyen2, citoyen1, antivax1,antivax2, antivax3, antivax4, antivax5, antivax6, antivax7, avion_loc, hall_loc, terminal_loc, list_sell)
            if direction.lower() == "s":
                Terminal[3][0] = shape
                localisation = Hall
                Hall[0][2] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
            else:
                Terminal = move(direction, Terminal)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
        if Terminal[3][1] == user:
            direction, stop, save = action(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map, player)
            if save == "save":
                save_game(localisation, player, Parking, Avion, Hall, Terminal, duty_map, duty, citoyen3, citoyen2, citoyen1, antivax1,antivax2, antivax3, antivax4, antivax5, antivax6, antivax7, avion_loc, hall_loc, terminal_loc, list_sell)
            if direction.lower() == "s":
                Terminal[3][1] = shape
                localisation = Hall
                Hall[0][3] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
            else:
                Terminal = move(direction, Terminal)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
        # Je défini les portes de Terminal vers Avion:
        if Terminal[0][0] == user:
            direction, stop, save = action(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map, player)
            if save == "save":
                save_game(localisation, player, Parking, Avion, Hall, Terminal, duty_map, duty, citoyen3, citoyen2, citoyen1, antivax1,antivax2, antivax3, antivax4, antivax5, antivax6, antivax7, avion_loc, hall_loc, terminal_loc, list_sell)
            if direction.lower() == "z":
                Terminal[0][0] = shape
                localisation = Avion
                if avion_loc == "0":
                    avion_print(os)
                avion_loc = "1"
                Avion[4][3] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
            else:
                Terminal = move(direction, Terminal)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
        # Je défini les portes de Avion vers Terminal:
        if Avion[4][3] == user:
            direction, stop, save = action(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map, player)
            if save == "save":
                save_game(localisation, player, Parking, Avion, Hall, Terminal, duty_map, duty, citoyen3, citoyen2, citoyen1, antivax1,antivax2, antivax3, antivax4, antivax5, antivax6, antivax7, avion_loc, hall_loc, terminal_loc, list_sell)
            if direction.lower() == "s":
                Avion[4][3] = shape
                localisation = Terminal
                Terminal[0][0] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
            else:
                Avion = move(direction, Avion)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
        #Je défini les portes de Avion vers le mage:
        if Avion[0][0] == user:
            direction, stop, save = action(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map, player)
            if save == "save":
                save_game(localisation, player, Parking, Avion, Hall, Terminal, duty_map, duty, citoyen3, citoyen2, citoyen1, antivax1,antivax2, antivax3, antivax4, antivax5, antivax6, antivax7, avion_loc, hall_loc, terminal_loc, list_sell)
            if direction.lower() == "z":
                if os == "mac":
                    system("clear")
                elif os == "windows":
                    system("cls")
                beat_the_boss = input("   Voulez-vous affronter le boss? o/n : ")
                while beat_the_boss.lower() != "o" and beat_the_boss != "n":
                    beat_the_boss = input("   Voulez-vous affronter le boss? o/n : ")
                if beat_the_boss.lower() == "o":
                    fight_print(os)
                    battle(player, boss, os)
                    break
            else:
                Avion = move(direction, Avion)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc, duty, duty_map)
        # je défini une zone de combat
        if Parking[0][3] == user:
            if antivax1 == "1":
                fight_print(os)
                battle(player, xavitna, os)
                if player[0][2] <= 0:
                    return
                antivax1 = "0"
        # je défini une zone de combat
        if Parking[1][0] == user:
            if antivax2 == "1":
                fight_print(os)
                battle(player, seukitpes, os)
                if player[0][2] <= 0:
                    return
                antivax2 = "0"
        # je défini une zone de combat
        if Hall[0][0] == user:
            if antivax3 == "1":
                fight_print(os)
                battle(player, xavitna, os)
                if player[0][2] <= 0:
                    return
                antivax3 = "0"
        # je défini une zone de combat
        if Hall[2][2] == user:
            if antivax4 == "1":
                fight_print(os)
                battle(player, seukitpes, os)
                if player[0][2] <= 0:
                    return
                antivax4 = "0"
        # je défini une zone de combat
        if Terminal[0][2] == user:
            if antivax5 == "1":
                fight_print(os)
                battle(player, xavitna, os)
                if player[0][2] <= 0:
                    return
                antivax5 = "0"
        # je défini une zone de combat
        if Avion[1][0] == user:
            if antivax6 == "1":
                fight_print(os)
                battle(player, seukitpes, os)
                if player[0][2] <= 0:
                    return
                antivax6 = "0"
        # je défini une zone de combat
        if Avion[0][3] == user:
            if antivax7 == "1":
                fight_print(os)
                battle(player, xavitna, os)
                if player[0][2] <= 0:
                    return
                antivax7 = "0"
        # je défini le zone de duty freeing
        if Hall[2][0] == user:
            duty_print(os)
            shop_choice = " "
            if os == "mac":
                from menu_nav_mac import menu_nav_mac
                while shop_choice != "Retour":
                    print(player[3])
                    sell_fonction = menu_nav_mac(list_sell)
                    shop_choice = duty_free(player, sell_fonction, list_sell, os)
            elif os == "windows":
                from Menu_nav import menu_nav
                while shop_choice != "Retour":
                    print(player[3])
                    sell_fonction = menu_nav(list_sell)
                    shop_choice = duty_free(player, sell_fonction, list_sell, os)
            duty_map = "0"
            duty = "1"
        # je défini la zone de citoyen
        if Parking[2][3] == user:
            if citoyen1 == "1":
                citoyen_print(os)
                jeux = pierre_feuille_ciseaux(os)
                if jeux == "win":
                    victoir_mini_jeux_print(os)
                    player[3][1] += 100
                    citoyen1 = "0"
                elif jeux == "loose":
                    defaite_mini_jeux_print(os)
        # je défini la zone de citoyen
        if Avion[3][2] == user:
            if citoyen2 == "1":
                citoyen_print(os)
                jeux = lancer_de(os)
                if jeux == "win":
                    victoir_mini_jeux_print(os)
                    player[3][1] += 100
                    citoyen2 = "0"
                elif jeux == "loose":
                    defaite_mini_jeux_print(os)
        # je défini la zone de citoyen
        if Terminal[1][2] == user:
            if citoyen3 == "1":
                citoyen_print(os)
                jeux = just_prix()
                if jeux == "win":
                    victoir_mini_jeux_print(os)
                    player[3][1] += 100
                    citoyen3 = "0"
                elif jeux == "loose":
                    defaite_mini_jeux_print(os)
        # je rallume l'interupteur pour afficher le duty free
        if Hall[2][0] != user:
            duty_map = "1"




def first_localisation():
    user = "[Ï]"
    Parking[4][3] = user
    start_var = "new"
    return localisation_of_door_enemy_item(Avion, Terminal, Hall, Parking, start_var)

def load_localisation():
    start_var = "load"
    return localisation_of_door_enemy_item(Avion, Terminal, Hall, Parking, start_var)