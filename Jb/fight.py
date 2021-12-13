from os import system
from time import sleep

xavitna = [5, 6, 0, "Xavitna"]
seukitpes = [8, 3, 0, "Seukitpes"]
boss = [50, 30, 0, "Boss"]
player = [10, 2, 0, ["Inventaire:", "Gel Hydroalcoolique"]]

def check(player, monster):
    if monster[0] <= 0:
        print("gg")
        return True
    elif player[0] <= 0:
        print("ptdr")
        return False

def fight(player, monster):
    i = 0
    print("Vous engagez le combat contre", monster[3])
    while (player[0] > 0 and monster[0] > 0):
        sleep(1)
        print("Monster HPs =", monster[0], "Player HPs=", player[0])
        choice = input("player choice:\n -atk\n -inv\n")
        while choice != "atk" and choice != "inv":
            choice = input()
        system('cls')

        if choice == "atk":
            pDmg = player[1] - monster[2]
            if pDmg > 0:    
                monster[0] = monster[0] - pDmg
            else:
                print("Tu as infligé 0 dégats")
            sleep(1)
            print("mHP=", monster[0], "pHP=", player[0])
            if check(player, monster) == True:
                return player
        
        if choice == "inv":
            for i in range(len(player[3])):
                print(player[3][i])
            print("Retour\n")
            inv_choice = input("Que voulez-vous faire ?:\n")
            if inv_choice == "Potion":
                player[0] = player[0] + 5
            elif inv_choice == "Retour":
                 choice = input("player choice:\n -atk\n -inv\n")   
        print("monster atk")
        mDmg = monster[1] - player[2]
        if mDmg > 0:
            player[0] = player[0] - mDmg
        else:
            print("Tu n'as subi aucun dégat")
            sleep(1)
            #system('cls')
        check(player, monster)
    return player

fight(player, xavitna)