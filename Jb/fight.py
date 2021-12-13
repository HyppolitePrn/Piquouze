from os import system
from time import sleep

xavitna = [5, 6, 0, "Xavitna"]
seukitpes = [8, 3, 0, "Seukitpes"]
boss = [50, 30, 0, "Boss"]
player = [10, 2, 0, ["Inventaire:", "Gel Hydroalcoolique"]]

def check(player, monster):
    if monster[0] <= 0:
        print("Vous avez gagné le combat !")
        return True
    elif player[0] <= 0:
        print("Vous êtes morts, unlucky happens")
        return True

def inventory(player):
    for i in range(len(player[3])):
        print(player[3][i])
    print("Retour\n")
    inv_choice = input("Que voulez-vous faire ?:\n")
    if inv_choice == "Potion":
        player[0] = player[0] + 5
        if player[0] > 10:
            player[0] = 10
        player[3].remove("Gel Hydroalcoolique")
        print(player)
        system('cls')
        return player, True
    elif inv_choice == "Retour":
        system('cls')
        return player, False

def player_atk(player, monster):
    playerDamage = player[1] - monster[2]
    if playerDamage > 0:    
        monster[0] = monster[0] - playerDamage
        print("Tu infliges", playerDamage, "dégats")
        print("Monster HPs=", monster[0], "Player HPs=", player[0])
        sleep(2)
        system('cls')
    else:
        print("Tu as infligé 0 dégats")
        sleep(1)
    return player, monster

def monster_attack(player, monster):
    print("Le monstre attaque !")
    sleep(1)
    monsterDamage = monster[1] - player[2]
    if monsterDamage > 0:
        player[0] = player[0] - monsterDamage
        print("Il vous inflige", monsterDamage, "dégats")
    else:
        print("Tu n'as subi aucun dégat")
    sleep(1)
    return player, monster

def fight(player, monster):
    #print("Vous engagez le combat contre", monster[3])
    while (player[0] > 0 and monster[0] > 0):
        sleep(0.3)
        print("Monster HPs=", monster[0], "Player HPs=", player[0])
        choice = input("Que voulez-vous faire ?:\n -atk\n -inv\n -vax\n")
        while choice != "atk" and choice != "inv" and choice != "vax":
            choice = input()
        system('cls')
        while choice == "inv":
            player, action = inventory(player)
            if action !=True:
                fight(player, monster)
            break
        if choice == "vax":
            if monster[0] <= 3:
                print("Vous avez sauvé le", monster[3])
                sleep(1)
                system('cls')
                break
            else:
                print("Vous devez d'abord affaiblir le", monster[3], "avant de pouvoir le vacciner")
                sleep(1.5)
                system('cls')
                fight(player, monster)
        if choice == "atk":
            player, monster = player_atk(player, monster)
            if check(player, monster) == True:
                break
        player, monster = monster_attack(player, monster)
        if check(player, monster) == True:
            break
    return player

fight(player, xavitna)