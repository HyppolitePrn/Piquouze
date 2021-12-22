from time import sleep
from os import system
from Mac_or_wind import os
from liste import start

def info():
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print("Toute ressemblance avec un quelconque fait réel est fortuite")
    sleep(1.5)
    print("Tous les événements ne sont que pure fiction")
    sleep(2)
    print("\nProjet RPG Hetic W1 réalisé par:")
    sleep(0.5)
    print("Abdoulaye Diallo")
    sleep(0.5)
    print("Adrien Quimbre")
    sleep (0.5)
    print("Hyppolite Pernot")
    sleep(0.5)
    print("Jean-Baptiste Migone")
    sleep(3)
    if os == "mac":
        from menu_nav_mac import menu_nav_mac
        system('clear')
        menu_nav_mac(start())
    elif os == "windows":
        from Menu_nav import menu_nav
        system('cls')
        menu_nav(start())
    return