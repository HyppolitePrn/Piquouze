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
    "Gel Hydroalcoolique +5 hp (soin) : 10 ",
    "Masque chirurgical +1 défense : 100",
    "Blouse de bataille +3 défense : 100",
    "Seringue en adamantium +3 attaque : 100",
    "Retour"
]

menu_ig = ["Menu:", 
    "Stats", 
    "Inventaire",
    "Equipement",
    "Argent",
    "Retour"
]

player = [["Stats:", "Pv:", 10, "Attaque:", 3, "Défense:", 0, "Lvl:", 1, "XP:", 0], 
    ["Inventaire:", "Gel Hydroalcoolique", "Retour"], 
    ["Equipement:"], 
    ["Argent:", 0]]