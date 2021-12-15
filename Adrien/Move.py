from Map import *
from Affichage import *
from Mac_or_wind import *
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


def localisation_of_door_enemy_item(Avion, Terminal, Hall, Parking,localisation):
    stop = " "
    user = "[Ï]"
    shape = "[ ]"
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
    

    while stop == " ":
        map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
        print("   Tapez 'inventaire' 'menu' pour accéder aux contenues associé.")
        print("   Pour vous déplacer")
        direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
        if direction.lower() == "stop":
                stop = "stop"

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

        # Je défini les portes de Parking vers Hall:
        if Parking[0][0] == user:
            map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            print("   Tapez 'inventaire' 'vie' 'competence' 'niveau' pour accéder aux contenues")
            print("   Pour vous déplacer")
            direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
            if direction.lower() == "stop":
                stop = "stop"
            if direction.lower() == "z":
                Parking[0][0] = shape
                localisation = Hall
                if hall_loc == "0":
                    hall_print(os)
                hall_loc = "1"
                position = Hall[2][3]
                Hall[2][3] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            else:
                Parking = move(direction, Parking)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
        # Je défini les portes de hall vers parking:
        if Hall[2][3] == user:
            map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            print("   Tapez 'inventaire' 'vie' 'competence' 'niveau' pour accéder aux contenues")
            print("   Pour vous déplacer")
            direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
            if direction.lower() == "stop":
                stop = "stop"
            if direction.lower() == "s":
                Hall[2][3] = shape
                localisation = Parking
                position = Parking[0][0]
                Parking[0][0] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            else:
                Hall = move(direction, Hall)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
        # Je défini les portes de Hall vers Terminal:
        if Hall[0][2] == user:
            map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            print("   Tapez 'inventaire' 'vie' 'competence' 'niveau' pour accéder aux contenues")
            print("   Pour vous déplacer")
            direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
            if direction.lower() == "stop":
                stop = "stop"
            if direction.lower() == "z":
                Hall[0][2] = shape
                localisation = Terminal
                if terminal_loc == "0":
                    terminal_print(os)
                terminal_loc = "1"
                position = Terminal[3][0]
                Terminal[3][0] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            else:
                Hall = move(direction, Hall)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
        if Hall[0][3] == user:
            map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            print("   Tapez 'inventaire' 'vie' 'competence' 'niveau' pour accéder aux contenues")
            print("   Pour vous déplacer")
            direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
            if direction.lower() == "stop":
                stop = "stop"
            if direction.lower() == "z":
                Hall[0][3] = shape
                localisation = Terminal
                if terminal_loc == "0":
                    terminal_print(os)
                terminal_loc = "1"
                position = Terminal[3][1]
                Terminal[3][1] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            else:
                Hall = move(direction, Hall)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
        # Je défini les portes de Terminal vers Hall:
        if Terminal[3][0] == user:
            map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            print("   Tapez 'inventaire' 'vie' 'competence' 'niveau' pour accéder aux contenues")
            print("   Pour vous déplacer")
            direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
            if direction.lower() == "stop":
                stop = "stop"
            if direction.lower() == "s":
                Terminal[3][0] = shape
                localisation = Hall
                position = Hall[0][2]
                Hall[0][2] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            else:
                Terminal = move(direction, Terminal)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
        if Terminal[3][1] == user:
            map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            print("   Tapez 'inventaire' 'vie' 'competence' 'niveau' pour accéder aux contenues")
            print("   Pour vous déplacer")
            direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
            if direction.lower() == "stop":
                stop = "stop"
            if direction.lower() == "s":
                Terminal[3][1] = shape
                localisation = Hall
                position = Hall[0][3]
                Hall[0][3] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            else:
                Terminal = move(direction, Terminal)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
        # Je défini les portes de Terminal vers Avion:
        if Terminal[0][0] == user:
            map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            print("   Tapez 'inventaire' 'vie' 'competence' 'niveau' pour accéder aux contenues")
            print("   Pour vous déplacer")
            direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
            if direction.lower() == "stop":
                stop = "stop"
            if direction.lower() == "z":
                Terminal[0][0] = shape
                localisation = Avion
                if avion_loc == "0":
                    avion_print(os)
                avion_loc = "1"
                position = Avion[4][3]
                Avion[4][3] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            else:
                Terminal = move(direction, Terminal)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
        # Je défini les portes de Avion vers Terminal:
        if Avion[4][3] == user:
            map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            print("   Tapez 'inventaire' 'vie' 'competence' 'niveau' pour accéder aux contenues")
            print("   Pour vous déplacer")
            direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
            if direction.lower() == "stop":
                stop = "stop"
            if direction.lower() == "s":
                Avion[4][3] = shape
                localisation = Terminal
                position = Terminal[0][0]
                Terminal[0][0] = user
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            else:
                Avion = move(direction, Avion)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
        #Je défini les portes de Avion vers le mage:
        if Avion[0][0] == user:
            map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
            print("   Tapez 'inventaire' 'vie' 'competence' 'niveau' pour accéder aux contenues")
            print("   Pour vous déplacer")
            direction = input("   Ecrivez 'q' pour gauche, 'z' pour haut, 'd' pour droite, 's' pour bas: ")
            if direction.lower() == "stop":
                stop = "stop"
            if direction.lower() == "z":
                beat_the_boss = input("   Voulez-vous affronter le boss? o/n : ")
                while beat_the_boss.lower() != "o" and beat_the_boss != "n":
                    beat_the_boss = input("   Voulez-vous affronter le boss? o/n : ")
                if beat_the_boss.lower() == "o":
                    break
            else:
                Avion = move(direction, Avion)
                map_print(Avion, Terminal, Hall, Parking, os, hall_loc, terminal_loc, avion_loc)
        # je défini une zone de combat
        if Parking[0][3] == user:
            if antivax1 == "1":
                fight_print(os)
                antivax1 = "0"
        # je défini une zone de combat
        if Parking[1][0] == user:
            if antivax2 == "1":
                fight_print(os)
                antivax2 = "0"
        # je défini une zone de combat
        if Hall[0][0] == user:
            if antivax3 == "1":
                fight_print(os)
                antivax3 = "0"
        # je défini une zone de combat
        if Hall[2][2] == user:
            if antivax4 == "1":
                fight_print(os)
                antivax4 = "0"
        # je défini une zone de combat
        if Terminal[0][2] == user:
            if antivax5 == "1":
                fight_print(os)
                antivax5 = "0"
        # je défini une zone de combat
        if Avion[1][0] == user:
            if antivax6 == "1":
                fight_print(os)
                antivax6 = "0"
        # je défini une zone de combat
        if Avion[0][3] == user:
            if antivax7 == "1":
                fight_print(os)
                antivax7 = "0"
        # je défini le zone de duty freeing
        if Parking[4][0] == user:
            duty_print(os)
        # je défini la zone de citoyen
        if Parking[2][3] == user:
            if citoyen1 == "1":
                citoyen_print(os)
                citoyen1 = "0"
        # je défini la zone de citoyen
        if Avion[3][2] == user:
            if citoyen2 == "1":
                citoyen_print(os)
                citoyen2 = "0"
        # je défini la zone de citoyen
        if Terminal[1][2] == user:
            if citoyen3 == "1":
                citoyen_print(os)
                citoyen3 = "0"




def first_localisation():
    user = "[Ï]"
    localisation = Parking
    position = Parking[4][3]
    if position == Parking[4][3]:
        Parking[4][3] = user
    return localisation_of_door_enemy_item(Avion, Terminal, Hall, Parking, localisation)

os = wich_os()
first_localisation()