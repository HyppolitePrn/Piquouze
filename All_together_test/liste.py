from time import sleep
from os import system

def start():
    menu = [
        "Main menu:",
        "Nouvelle partie",
        "Info sur le jeu",
        "Charger une partie",
        "Quitter",
        ]
    return menu

list_sell = [
    "Articles:",
    "Gel Hydroalcoolique +5 hp (soin) : 10 ",
    "Masque chirurgical + 1 défense : 100",
    "Blouse de bataille + 3 défense : 100",
    "Seringue en adamantium +3 attaque : 100",
    "Retour"
]

menu_ig = ["Menu:",
    "Stats",
    "Inventaire",
    "Equipement",
    "Argent",
    "Quitter le jeux",
    "Sauvegarder",
    "Retour"
]


def list_fight(player):
    if player[0][8] >= 5:
        liste_fight =["Que voulez-vous faire ?","Attaquer","Inventaire"]
    else:
        liste_fight =["Que voulez-vous faire ?","Attaquer","Inventaire","Vacciner"]
    return liste_fight