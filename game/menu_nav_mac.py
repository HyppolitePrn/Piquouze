from os import system
from scenario import plot, press_enter_mac, skip_scenario
from getch_on_mac import *
from liste import start
from about import info

def menu_nav_mac(menu):
    print("\n")
    i = 1
    for k in range (0,len(menu)):
        if i == k:
            print(f"\033[1m-->  {menu[k]}\033[0m")
        else: 
            print(f"    {menu[k]}")
    moove = ''
    while moove != "\r":
        moove = getch_mac()
        if moove == "s" and i < len(menu) - 1:
            system("clear")
            print("\n")
            i = i + 1
            for j in range(0, len(menu)):
                if i == j:
                    print(f"\033[1m-->  {menu[j]}\033[0m")
                else: 
                    print(f"    {menu[j]}")
        elif moove == "z" and i > 1:
            system("clear")
            print("\n")
            i = i - 1
            for j in range(0,len(menu)):
                if i == j:
                    print(f"\033[1m-->  {menu[j]}\033[0m")
                else: 
                    print(f"    {menu[j]}")

    if menu[i] == "Nouvelle partie":
        plot()
        press_enter_mac()
    elif menu[i] == "Charger une partie":
        skip_scenario()
    elif menu[i] == "Info sur le jeu":
        info()
    elif menu[i] == "Quitter":
        return
    elif menu[i] == "Attaquer":
        return "atk"
    elif menu[i] == "Inventaire":
        return "inv"
    elif menu[i] == "Vacciner":
        return "vax"
    elif menu[i] == "Gel Hydroalcoolique":
        return "Potion"
    elif menu[i] == "Retour":
        return "Retour"
    elif menu[i] == "Gel Hydroalcoolique +5 hp (soin) : 10 ":
        return "Potion"
    elif menu[i] == "Masque chirurgical + 1 défense : 100":
        return "Masque chirurgical"
    elif menu[i] == "Blouse de bataille + 3 défense : 100":
        return "Blouse de bataille"
    elif menu[i] == "Seringue en adamantium +3 attaque : 100":
        return "Seringue en adamantium"
    elif menu[i] == "Stats":
        return "stats"
    elif menu[i] == "Inventaire":
        return "inv"
    elif menu[i] == "Equipement":
        return "equipment"
    elif menu[i] == "Argent":
        return "argent"
    elif menu[i] == "Quitter le jeu":
        return "stop"
    elif menu[i] == "Sauvegarder":
        return "save"
    else:
        menu_nav_mac(menu)