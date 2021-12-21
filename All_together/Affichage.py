from os import system
from time import sleep
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

def fight_print(os):
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print(RED, '''

                            ███████╗██╗ ██████╗ ██╗  ██╗████████╗
                            ██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝
                            █████╗  ██║██║  ███╗███████║   ██║   
                            ██╔══╝  ██║██║   ██║██╔══██║   ██║   
                            ██║     ██║╚██████╔╝██║  ██║   ██║   
                            ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                     

    ''', RESET)
    sleep(2)
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    return

def duty_print(os):
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print(YELLOW, '''
                            ██████╗ ██╗   ██╗████████╗██╗   ██╗
                            ██╔══██╗██║   ██║╚══██╔══╝╚██╗ ██╔╝
                            ██║  ██║██║   ██║   ██║    ╚████╔╝ 
                            ██║  ██║██║   ██║   ██║     ╚██╔╝  
                            ██████╔╝╚██████╔╝   ██║      ██║   
                            ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   
                                                            
                            ███████╗██████╗ ███████╗███████╗   
                            ██╔════╝██╔══██╗██╔════╝██╔════╝   
                            █████╗  ██████╔╝█████╗  █████╗     
                            ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝     
                            ██║     ██║  ██║███████╗███████╗   
                            ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝   
                                   
    ''', RESET)
    sleep(2)
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    return

def citoyen_print(os):
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print(BLUE,'''
                     ██████╗██╗████████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗
                    ██╔════╝██║╚══██╔══╝██╔═══██╗╚██╗ ██╔╝██╔════╝████╗  ██║
                    ██║     ██║   ██║   ██║   ██║ ╚████╔╝ █████╗  ██╔██╗ ██║
                    ██║     ██║   ██║   ██║   ██║  ╚██╔╝  ██╔══╝  ██║╚██╗██║
                    ╚██████╗██║   ██║   ╚██████╔╝   ██║   ███████╗██║ ╚████║
                    ╚═════╝╚═╝   ╚═╝    ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═══╝
                                                                            
                            ██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗       
                            ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║   ██║       
                            ██████╔╝█████╗  ██████╔╝██║  ██║██║   ██║       
                            ██╔═══╝ ██╔══╝  ██╔══██╗██║  ██║██║   ██║       
                            ██║     ███████╗██║  ██║██████╔╝╚██████╔╝       
                            ╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝        
                                                        
    ''', RESET)
    sleep(2)
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    return

def hall_print(os):
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print(GREEN,'''
                                ██╗  ██╗ █████╗ ██╗     ██╗     
                                ██║  ██║██╔══██╗██║     ██║     
                                ███████║███████║██║     ██║     
                                ██╔══██║██╔══██║██║     ██║     
                                ██║  ██║██║  ██║███████╗███████╗
                                ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
                                
''', RESET)
    sleep(2)
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    return

def terminal_print(os):
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print(GREEN,'''
                     ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     
                     ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     
                        ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     
                        ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     
                        ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
                        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
                                                                 
''', RESET)
    sleep(2)
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    return

def avion_print(os):
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print(GREEN,'''
                             █████╗ ██╗   ██╗██╗ ██████╗ ███╗   ██╗
                            ██╔══██╗██║   ██║██║██╔═══██╗████╗  ██║
                            ███████║██║   ██║██║██║   ██║██╔██╗ ██║
                            ██╔══██║╚██╗ ██╔╝██║██║   ██║██║╚██╗██║
                            ██║  ██║ ╚████╔╝ ██║╚██████╔╝██║ ╚████║
                            ╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                
''', RESET)
    sleep(2)
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    return

def stat_print(player, os):
    next = "["
    while next == "[":
        if os == "mac":
            from getch_on_mac import getch_mac
            system("clear")
            print(("________")* 11)
            print("\n")
            print("   ", *player[0])
            print("    appuyez sur une touche pour continuer")
            next = getch_mac()
        elif os == "windows":
            from msvcrt import getch
            system("cls")
            print(("________")* 11)
            print("\n")
            print("   ", *player[0])
            print("    appuyez sur une touche pour continuer")
            next = getch()
    return
        
def equipement_print(player, os):
    next = "["
    while next == "[":
        if os == "mac":
            from getch_on_mac import getch_mac
            system("clear")
            print(("________")* 11)
            print("\n")
            print("   ", *player[2])
            print("    appuyez sur une touche pour continuer")
            next = getch_mac()
        elif os == "windows":
            from msvcrt import getch
            system("cls")
            print(("________")* 11)
            print("\n")
            print("   ", *player[2])
            print("    appuyez sur une touche pour continuer")
            next = getch()
    return

def argent_print(player, os):
    next = "["
    while next == "[":
        if os == "mac":
            from getch_on_mac import getch_mac
            system("clear")
            print(("________")* 11)
            print("\n")
            print("   ", *player[3])
            print("    appuyez sur une touche pour continuer")
            next = getch_mac()
        elif os == "windows":
            from msvcrt import getch
            system("cls")
            print(("________")* 11)
            print("\n")
            print("   ", *player[3])
            print("    appuyez sur une touche pour continuer")
            next = getch()
    return


def victoir_mini_jeux_print(os):
    next = "["
    while next == "[":
        if os == "mac":
            from getch_on_mac import getch_mac
            system("clear")
            print(("________")* 11)
            print("\n")
            print("   ", "Vous avez gagné, vous remporter 100 d'argent")
            print("    appuyez sur une touche pour continuer")
            next = getch_mac()
        elif os == "windows":
            from msvcrt import getch
            system("cls")
            print(("________")* 11)
            print("\n")
            print("   ", "Vous avez gagné, vous remporter 100 d'argent")
            print("    appuyez sur une touche pour continuer")
            next = getch()
    return

def defaite_mini_jeux_print(os):
    next = "["
    while next == "[":
        if os == "mac":
            from getch_on_mac import getch_mac
            system("clear")
            print(("________")* 11)
            print("\n")
            print("   ", "Vous avez perdu, revenez pour retenter votre chance")
            print("    appuyez sur une touche pour continuer")
            next = getch_mac()
        elif os == "windows":
            from msvcrt import getch
            system("cls")
            print(("________")* 11)
            print("\n")
            print("   ", "Vous avez perdu, revenez pour retenter votre chance")
            print("    appuyez sur une touche pour continuer")
            next = getch()
    return

