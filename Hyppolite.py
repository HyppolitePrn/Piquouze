from msvcrt import getch
from os import system
from liste import start

printed_menu = '\n'.join(start())
print(printed_menu)


def menu_nav(menu):
    i = 0
    moove = ''
    while moove != "\r":
        moove = getch().decode()
        if moove == "P" and i < len(menu) - 1:
            system("cls")
            i = i + 1
            for j in range(0, len(menu)):
                if i == j:
                    print(f"\033[1m-->  {menu[j]}\033[0m")
                else: 
                    print(f"    {menu[j]}")
        elif moove == "H" and i > 1:
            system("cls")
            i = i - 1
            for j in range(0,len(menu)):
                if i == j:
                    print(f"\033[1m-->  {menu[j]}\033[0m")
                else: 
                    print(f"    {menu[j]}")

menu_nav(start())


    
