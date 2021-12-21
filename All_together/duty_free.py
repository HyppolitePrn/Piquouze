from os import system
from time import sleep

def duty_free(player, choice, sell, os):
    if choice == "Potion":
        if player[3][1] < 10:
            print("Tu n'as pas assez d'argent")
            sleep(2)
        elif player[3][1] >= 10:
            player[1].insert(len(player[1]) - 1, "Gel Hydroalcoolique")
            player[3][1] = player[3][1] - 10
    elif choice ==  "Masque chirurgical":
        if player[3][1] < 100:
            print("Tu n'as pas assez d'argent")
        if player[3][1] >= 100:
            player[2].append("Masque chirurgical")
            player[0][6] += 1
            sell.remove("Masque chirurgical + 1 défense : 100")
            player[3][1] -= 100
    elif choice == "Blouse de bataille":
        if player[3][1] < 100:
            print("Tu n'as pas assez d'argent")
        if player[3][1] >= 100:
            player[2].append("Blouse de bataille")
            player[0][6] += 3 
            sell.remove("Blouse de bataille + 3 défense : 100")
            player[3][1] -= 100
    elif choice == "Seringue en adamantium":
        if player[3][1] < 100:
            print("Tu n'as pas assez d'argent")
        if player[3][1] >= 100:
            player[2].append("Seringue en adamantium")
            player[0][4] += 3
            sell.remove("Seringue en adamantium +3 attaque : 100")
            player[3][1] -= 100
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    return choice