from os import system
from msvcrt import getch
from scenario import plot, press_enter
from liste import start



def menu_nav(menu):
    print("\n")
    printed_menu = "\n".join(menu)
    print(printed_menu)
    i = 0
    moove = ''
    while moove != "\r":
        moove = getch().decode()
        if moove == "P" and i < len(menu) - 1:
            system("cls")
            i = i + 1
            for j in range(0, len(menu)):
                if i == j:
                    print(f"\033[1m-->  {menu[j]}\033[0m")
                else: 
                    print(f"    {menu[j]}")
        elif moove == "H" and i > 1:
            system("cls")
            i = i - 1
            for j in range(0,len(menu)):
                if i == j:
                    print(f"\033[1m-->  {menu[j]}\033[0m")
                else: 
                    print(f"    {menu[j]}")

    if menu[i] == "Nouvelle partie":
        plot()
        press_enter()
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
    elif menu[i] == "Masque chirurgical (defense), Xg":
        return "Masque chirurgical"
    elif menu[i] == "Blouse de bataille (defense) Xg":
        return "Blouse de bataille"
    elif menu[i] == "Seringue en adamantium (attaque) Xg":
        return "Seringue en adamantium"
    elif menu[i] == "Stats":
        return "stats"
    elif menu[i] == "Inventaire":
        return "inv"
    elif menu[i] == "Equipement":
        return "equipment"
    elif menu[i] == "Gold":
        return "gold"
    else:
        menu_nav(start())

# os = wich_os()
# if os == "linux":
#     os = "mac"
# if os == "mac":
#     menu_nav_mac(start())
# if os == "windows":
#     from msvcrt import getch
#     menu_nav(start())
