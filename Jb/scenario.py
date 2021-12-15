from time import sleep
from msvcrt import getch
from os import system

def plot():
    sleep(1)
    print("An 20XX,")
    sleep(1)
    print("Le Divoc 19 s'est propagé dans le monde, réveillant les pulsions les plus sombres de chaque individu")
    sleep(2)
    print("Tous? Non! Un petit laboratoire a réussi à résister à l'épidémie.")
    sleep(2)
    print("Seul problème, la zone de déploiement, l'aéroport de ***, est submergé d'infectés.")
    sleep(2)
    print("Vous vous êtes porté volontaire pour d'ouvrir le passage afin de transmettre le vaccin au monde.")
    sleep(2)
    print("Accéder à la piste de lancement ne sera pas chose facile.")
    sleep(2)
    print("Appuyez sur Entrée pour commencer le jeu...")
    return

def press_enter():
    key = getch().decode()
    if key == "o":
        key = getch().decode()
    else :
        return True

plot()
press_enter()
system('cls')