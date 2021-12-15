from os import system
from time import sleep
from levels import lvl_up
from levels import player

xavitna = [5, 6, 0, "Xavitna"]
seukitpes = [8, 3, 0, "Seukitpes"]
boss = [50, 30, 0, "Boss"]



def inventory(player):
    for i in range(len(player[1])):
        print(player[1][i])
    print("Retour\n")
    inv_choice = menu_nav(player[1])
    if inv_choice == "Potion":
        player[0][2] = player[0][2] + 5
        if player[0][2] > 10:
            player[0][2] = 10
            print("Vous récupérez toute votre vie")
        else:
            print("Vous récupérez 5 pvs")
        player[1].remove("Gel Hydroalcoolique")
        sleep(2)
        system('cls')
        return player, True
    elif inv_choice == "Retour":
        system('cls')
        return player, False



def monster_attack(player, monster):
    print(f"Le {monster[3]} attaque !")
    sleep(1)
    monsterDamage = monster[1] - player[0][6]
    if monsterDamage > 0:
        player[0][2] = player[0][2] - monsterDamage
        print("Il vous inflige", monsterDamage, "dégats")
    else:
        print("Tu n'as subi aucun dégat")
    sleep(1)
    system('cls')
    return player, monster

def check(player, monster):
    if monster[0] <= 0:
        print("Vous avez gagné le combat !")
        sleep(1)
        print("Vous gagnez 10 points d'expérience")
        player[0][10] += 10
        return True
    elif player[0][2] <= 0:
        print("Vous êtes morts...")
        return True

def vaccine(monster):
    if monster[0] <= 3:
        print("Vous avez sauvé le", monster[3])
        sleep(1)
        print("Vous avez gagné 2 points d'expérience")
        sleep(1)
        system('cls')
        return True
    else:
        print("Vous devez d'abord affaiblir le", monster[3], "avant de pouvoir le vacciner")
        sleep(2)
        system('cls')
        return False


def player_atk(player, monster):
    playerDamage = player[0][4] - monster[2]
    if playerDamage > 0:    
        monster[0] = monster[0] - playerDamage
        if monster[0] < 0:
            monster[0] = 0
        print("Tu infliges", playerDamage, "dégats")
        sleep(1)
        print(f"{monster[3]} HPs=", monster[0], "Player HPs=", player[0][2])
        sleep(2)
        system('cls')
    else:
        print("Tu as infligé 0 dégats")
        sleep(1)
    return player, monster


def lvl_up(player):
    if player[0][10] == 10:
        player[0][8] += 1
        player[0][2] += 3
        player[0][4] += 1
        player[0][10] = 0
        print("Lvl up!")
        sleep(1)
        print("Vous gagnez +3 Pvs, +1 Attaque")
        sleep(1)
    return player


def battle(player, monster):
    vax = False
    print("Vous engagez le combat contre", monster[3])
    sleep(1)
    system("cls")
    while (player[0][2] > 0 and monster[0] > 0):
        sleep(0.3)
        print(f"{monster[3]} HPs=", monster[0], "Player HPs=", player[0][2])
        choice = menu_nav(list_fight())
        system('cls')
        while choice == "inv":
            system('cls')
            player, action = inventory(player)
            if action !=True:
                system('cls')
                choice = menu_nav(list_fight())
            else:
                break
        while choice == "vax":
            vax = vaccine(monster)
            if vax == True:
                return player
            else:
                choice = menu_nav(list_fight())
                system('cls')
        if choice == "atk":
            player, monster = player_atk(player, monster)
            if check(player, monster) == True:
                lvl_up(player)
                break
        if vax != True:
            player, monster = monster_attack(player, monster)
        if check(player, monster) == True:
            lvl_up(player)
            break
    return player


battle(player, xavitna)