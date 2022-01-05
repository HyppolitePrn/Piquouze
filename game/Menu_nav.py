from os import system
from msvcrt import getch
from scenario import plot, press_enter, skip_scenario
from about import info

'''
Fonction qui permet ne naviguer dans un menu a l'aide des fleches directionnelles pour eviter les input
on met une liste en parametre dont pourra naviguer .(on exclu l'indice 0 car dans nos listes la premiere valeur est une "description de la liste")
'''

def menu_nav(menu):
    print("\n")
    #i est le curseur du menu cest lui que l'utilisateur va faire varier avec getch
    i = 1
    #boucle qui gere laffichage de la liste
    for k in range (0,len(menu)):
        if i == k:
            print(f"\033[1m-->  {menu[k]}\033[0m")
        else: 
            print(f"    {menu[k]}")
    moove = ''
    while moove != "\r":#\r représente entrer
        moove = getch().decode()
        if moove == "P" and i < len(menu) - 1:
            system("cls")
            print("\n")
            i = i + 1
            for j in range(0, len(menu)):
                if i == j:
                    print(f"\033[1m-->  {menu[j]}\033[0m")
                else: 
                    print(f"    {menu[j]}")
        elif moove == "H" and i > 1:
            system("cls")
            print("\n")
            i = i - 1
            for j in range(0,len(menu)):
                if i == j:
                    print(f"\033[1m-->  {menu[j]}\033[0m")
                else: 
                    print(f"    {menu[j]}")

    #tous les return pour toute les listes (en general on return le str et c'est dans le code qu'il se passe des chose en fonction du choix)

    if menu[i] == "Nouvelle partie":
        plot()
        press_enter()
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
        menu_nav(menu)
