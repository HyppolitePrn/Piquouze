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


def player():
    player = [10, 2, 0, ["Inventaire:", "Gel Hydroalcoolique"]]
    return player 


def xavitna():
    xavitna = [5, 6, 0, "Xavitna"]
    return xavitna
def seukitpes():
    seukitpes = [8, 3, 0, "Seukitpes"]
    return seukitpes
def boss():
    boss = [50, 30, 0, "Boss"]
    return boss
def vacciner(monster):
    if monster[0] <= 3:
        print("Vous avez sauvé le", monster[3])
        sleep(1)
        system('cls')

list_sell = ["Gel Hydro (soin) X g",
    "Masque chirurgical (defense), Xg",
    "Blouse de bataille (defense) Xg",
    "Seringue en adamantium (attaque) Xg"
]
