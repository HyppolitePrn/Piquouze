from os import system
from scenario import plot, press_enter_mac
from getch_on_mac import *
from liste import start


def menu_nav_mac(menu):
    print("\n")
    printed_menu = "\n".join(menu)
    print(printed_menu)
    i = 0
    moove = ''
    while moove != "\r":
        moove = getch_mac()
        if moove == "s" and i < len(menu) - 1:
            system("clear")
            i = i + 1
            for j in range(0, len(menu)):
                if i == j:
                    print(f"\033[1m-->  {menu[j]}\033[0m")
                else: 
                    print(f"    {menu[j]}")
        elif moove == "z" and i > 1:
            system("clear")
            i = i - 1
            for j in range(0,len(menu)):
                if i == j:
                    print(f"\033[1m-->  {menu[j]}\033[0m")
                else: 
                    print(f"    {menu[j]}")

    if menu[i] == "Nouvelle partie":
        plot()
        press_enter_mac()
    elif menu[i] == "Info sur le jeu":
        print("bn")
    elif menu[i] == "Quitter":
        return
    elif menu[i] == "attaquer":
        return "atk"
    elif menu[i] == "inventaire":
        return "inv"
    elif menu[i] == "vacciner":
        return "vax"
    elif menu[i] == "Gel Hydroalcoolique":
        return "Potion"
    elif menu[i] == "Retour":
        return "Retour"
    elif menu[i] == "Masque chirurgical":
        return "Masque chirurgical"
    elif menu[i] == "Blouse de bataille":
        return "Blouse de bataille"
    elif menu[i] == "Seringue en adamantium":
        return "Seringue en adamantium"
    else:
        menu_nav_mac(start())