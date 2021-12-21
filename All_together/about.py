from time import sleep
from os import system
from Mac_or_wind import os

def info():
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print("Toute ressemblance avec un quelconque fait réel est fortuite")
    sleep(1.5)
    print("Tous les événements ne sont que pure fiction")
    sleep(1.5)
    print("Projet RPG Hetic W1 réalisé par:")
    sleep(0.5)
    print("Abdoulaye Diallo")
    sleep(0.5)
    print("Adrien Quimbre")
    sleep (0.5)
    print("Hyppolite Pernot")
    sleep(0.5)
    print("Jean-Baptiste Migone")
    sleep(0.5)
    return