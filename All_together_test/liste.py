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


menu_ig = ["Menu:",
    "Stats",
    "Inventaire",
    "Equipement",
    "Argent",
    "Sauvegarder",
    "Quitter le jeux",
    "Retour"
]


def list_fight(player):
    if player[0][8] >= 5:
        liste_fight =["Que voulez-vous faire ?","Attaquer","Inventaire"]
    else:
        liste_fight =["Que voulez-vous faire ?","Attaquer","Inventaire","Vacciner"]
    return liste_fight