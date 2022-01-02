from time import sleep
from Move import first_localisation
from Move import load_localisation
from getch_on_mac import getch_mac
from os import system
from Mac_or_wind import os

def plot():
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print("An 20XX,")
    sleep(1)
    print("Le Divoc 91 s'est propagé dans le monde, réveillant les pulsions les plus sombres de chaque individu")
    sleep(2)
    print("Tous? Non! Un petit laboratoire a réussi à résister à l'épidémie.")
    sleep(2)
    print("Seul problème, la zone de déploiement, l'aéroport de ***, est submergé d'infectés.")
    sleep(2)
    print("Vous vous êtes porté volontaire pour ouvrir le passage afin de transmettre le vaccin au monde.")
    sleep(2)
    print("Accéder à la piste de lancement ne sera pas chose facile.")
    sleep(2)
    print("Appuyez sur Entrée pour commencer le jeu...")
    return

def press_enter():
    from msvcrt import getch
    key = getch().decode()
    if key == "o":
        key = getch().decode()
    else :
        return first_localisation()

def press_enter_mac():
    press = getch_mac()
    if press != "[":
        return first_localisation()

def skip_scenario():
    return load_localisation()
