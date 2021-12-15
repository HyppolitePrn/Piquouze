from os import system
from time import sleep
from Mac_or_wind import *
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
    if os == "windows":
        system("cls")
    print(RED, '''

                            ███████╗██╗ ██████╗ ██╗  ██╗████████╗
                            ██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝
                            █████╗  ██║██║  ███╗███████║   ██║   
                            ██╔══╝  ██║██║   ██║██╔══██║   ██║   
                            ██║     ██║╚██████╔╝██║  ██║   ██║   
                            ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                     

    ''', RESET)
    sleep(3)
    if os == "mac":
        system("clear")
    if os == "windows":
        system("cls")
    return

def duty_print(os):
    if os == "mac":
        system("clear")
    if os == "windows":
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
    sleep(3)
    if os == "mac":
        system("clear")
    if os == "windows":
        system("cls")
    return

def citoyen_print(os):
    if os == "mac":
        system("clear")
    if os == "windows":
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
    sleep(3)
    if os == "mac":
        system("clear")
    if os == "windows":
        system("cls")
    return

def hall_print(os):
    if os == "mac":
        system("clear")
    if os == "windows":
        system("cls")
    print(GREEN,'''
                                ██╗  ██╗ █████╗ ██╗     ██╗     
                                ██║  ██║██╔══██╗██║     ██║     
                                ███████║███████║██║     ██║     
                                ██╔══██║██╔══██║██║     ██║     
                                ██║  ██║██║  ██║███████╗███████╗
                                ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
                                
''', RESET)
    sleep(3)
    if os == "mac":
        system("clear")
    if os == "windows":
        system("cls")
    return

def terminal_print(os):
    if os == "mac":
        system("clear")
    if os == "windows":
        system("cls")
    print(GREEN,'''
                     ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     
                     ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     
                        ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     
                        ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     
                        ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
                        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
                                                                 
''', RESET)
    sleep(3)
    if os == "mac":
        system("clear")
    if os == "windows":
        system("cls")
    return

def avion_print(os):
    if os == "mac":
        system("clear")
    if os == "windows":
        system("cls")
    print(GREEN,'''
                             █████╗ ██╗   ██╗██╗ ██████╗ ███╗   ██╗
                            ██╔══██╗██║   ██║██║██╔═══██╗████╗  ██║
                            ███████║██║   ██║██║██║   ██║██╔██╗ ██║
                            ██╔══██║╚██╗ ██╔╝██║██║   ██║██║╚██╗██║
                            ██║  ██║ ╚████╔╝ ██║╚██████╔╝██║ ╚████║
                            ╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                
''', RESET)
    sleep(3)
    if os == "mac":
        system("clear")
    if os == "windows":
        system("cls")
    return

def description_hall():
    pass
