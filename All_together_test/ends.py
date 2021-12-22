from time import sleep
from getch_on_mac import getch_mac
from os import system
from Mac_or_wind import os

def good_ending():
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print("Grâce à vos actions, le déploiement du vaccin a pu se faire aussi vite que possible.")
    sleep(2)
    print("Les personnes que vous avez sauvées sur votre chemin se sont révélées essentielles à votre mission.")
    sleep(2)
    print("Désormais, le monde est de nouveau en paix et peut se reconstruire sans problèmes.")
    sleep(2)
    print("\nAppuyez sur Entrée pour quitter...")
    return

def ending():
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print("C'est tant bien que mal que vous réussissez à accomplir votre mission.")
    sleep(2)
    print("Les pertes engendrées par ce virus ont fortement ralenties l'acheminement du vaccin.")
    sleep(2)
    print("Le monde est sauvé, mais il faudra du temps pour qu'il se relève...")
    sleep(2)
    print("\nAppuyez sur Entrée pour quitter...")
    return

def bad_ending():
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print("Désormais, plus personne ne peut se mettre en travers de votre route.")
    sleep(2)
    print("Vous possédez le seul endroit pouvant sauver le monde, qu'ils viennent vous chercher s'ils l'osent.")
    sleep(2)
    print("Votre soif de sang est intarissable, vous affronterez quiconque ose s'approcher de cet endroit jusqu'à votre dernière heure.")
    sleep(2)
    print("\nAppuyez sur Entrée pour quitter...")
    return

def press_enter():
    from msvcrt import getch
    key = getch().decode()
    if key == "o":
        key = getch().decode()
    else :
        return

def press_enter_mac():
    press = getch_mac()
    if press != "[":
        return