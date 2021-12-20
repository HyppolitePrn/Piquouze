from liste import start
from Mac_or_wind import os
from os import system

def start_with_os(os):
    if os.lower() == "linux":
        os = "mac"
    elif os.lower() == "mac":
        from menu_nav_mac import menu_nav_mac
        system('clear')
        menu_nav_mac(start())
    elif os.lower() == "windows":
        from Menu_nav import menu_nav
        system('cls')
        menu_nav(start())

start_with_os(os)