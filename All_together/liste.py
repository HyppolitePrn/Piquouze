from time import sleep
from os import system

def start():
    menu = [
        "Main menu:",
        "Nouvelle partie",
        "Info sur le jeu",
        "Quitter",
        ]
    return menu


def list_fight():
    liste_fight =["Que voulez-vous faire ?","attaquer","inventaire","vacciner"]
    return liste_fight



list_sell = [
    "Articles:",
    "Gel Hydro (soin) X g",
    "Masque chirurgical (defense), Xg",
    "Blouse de bataille (defense) Xg",
    "Seringue en adamantium (attaque) Xg",
    "Retour"
]

menu_ig = ["Menu:", 
    "Stats", 
    "Inventaire",
    "Equipement"
    "Gold",
    "Retour"
]

player = [["Stats:", "Pv:", 10, "Attaque:", 3, "Défense:", 0, "Lvl:", 1, "XP:", 0], 
    ["Inventaire:", "Gel Hydroalcoolique", "Retour"], 
    ["Equipement:"], 
    ["Argent:", 0]]