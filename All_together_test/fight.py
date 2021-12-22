from os import system
from time import sleep
from levels import lvl_up
from liste import list_fight

def inventory(player, os):
    if os == "mac":
        from menu_nav_mac import menu_nav_mac
        inv_choice = menu_nav_mac(player[1])
    elif os == "windows":
        from Menu_nav import menu_nav
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
        if os == "mac":
            system("clear")
        elif os == "windows":
            system("cls")
        return player, True
    elif inv_choice == "Retour":
        if os == "mac":
            system("clear")
        elif os == "windows":
            system("cls")
        return player, False



def monster_attack(player, monster, os):
    print(f"Le {monster[3]} attaque !")
    sleep(1)
    monsterDamage = monster[1] - player[0][6]
    if monsterDamage > 0:
        player[0][2] = player[0][2] - monsterDamage
        print("Il vous inflige", monsterDamage, "dégats")
    else:
        print("Tu n'as subi aucun dégat")
    sleep(1)
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    return player, monster

def check(player, monster):
    if monster[0] <= 0:
        print("Vous avez gagné le combat !")
        sleep(1)
        print("Vous gagnez 10 points d'expérience !")
        player[0][10] += 10
        return True
    elif player[0][2] <= 0:
        print("Vous êtes morts...")
        return True

def vaccine(monster, os):
    if monster[0] <= 3:
        print("Vous avez sauvé le", monster[3])
        sleep(1)
        print("Vous avez gagné 2 points d'expérience !")
        sleep(1)
        if os == "mac":
            system("clear")
        elif os == "windows":
            system("cls")
        return True
    else:
        if os == "mac":
            system("clear")
        elif os == "windows":
            system("cls")
        print("Vous devez d'abord affaiblir le", monster[3], "avant de pouvoir le vacciner")
        sleep(2)
        if os == "mac":
            system("clear")
        elif os == "windows":
            system("cls")
        return False


def player_atk(player, monster, os):
    playerDamage = player[0][4] - monster[2]
    if playerDamage > 0:    
        monster[0] = monster[0] - playerDamage
        if monster[0] < 0:
            monster[0] = 0
        print("Tu infliges", playerDamage, "dégats")
        sleep(1)
        print(f"{monster[3]} HPs=", monster[0], "Player HPs=", player[0][2])
        sleep(2)
        if os == "mac":
            system("clear")
        if os == "windows":
            system("cls")
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

def sanity(player):
    if player[0][8] >= 2 and player[0][8] < 4:
        print("Vous sentez quelque chose...")
    elif player[0][8] >= 4 and player[0][8] < 5:
        print("Quelque chose ne va pas...")
    elif player[0][8] >= 5:
        print("Que la chasse commence !")

def battle(player, monster, os):
    vax = False
    print("Vous engagez le combat contre", monster[3])
    sleep(1)
    sanity(player)
    sleep(2)
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    while (player[0][2] > 0 and monster[0] > 0):
        sleep(0.3)
        print(f"PVs du ", monster[3], ":", monster[0], "\nVos PVs :", player[0][2])
        if os == "mac":
            from menu_nav_mac import menu_nav_mac
            choice = menu_nav_mac(list_fight(player))
        elif os == "windows":
            from Menu_nav import menu_nav
            choice = menu_nav(list_fight(player))
        if os == "mac":
            system("clear")
        elif os == "windows":
            system("cls")
        while choice == "inv":
            if os == "mac":
                system("clear")
            elif os == "windows":
                system("cls")
            player, action = inventory(player, os)
            if action !=True:
                if os == "mac":
                    system("clear")
                    choice = menu_nav_mac(list_fight(player))
                elif os == "windows":
                    system("cls")
                    choice = menu_nav(list_fight(player))
            else:
                break
        while choice == "vax":
            vax = vaccine(monster, os)
            if vax == True:
                player[3][1] += 10
                print("Pour vous remercier, la personne vous donne 10 d'argent")
                return player
            else:
                if os == "mac":
                    choice = menu_nav_mac(list_fight(player))
                    while choice == "inv":
                        system("clear")
                        player, action = inventory(player, os)
                        if action !=True:
                            choice = menu_nav(list_fight(player))
                            system("clear")
                elif os == "windows":
                    choice = menu_nav(list_fight(player))
                    while choice == "inv":
                        system("cls")
                        player, action = inventory(player, os)
                        if action !=True:
                            choice = menu_nav(list_fight(player))
                            system("cls")
        if choice == "atk":
            player, monster = player_atk(player, monster, os)
            if check(player, monster) == True:
                lvl_up(player)
                player[3][1] += 10
                print("Vous récupérez 10 d'argent")
                sleep(2)
                break
        if vax != True:
            player, monster = monster_attack(player, monster, os)
        if check(player, monster) == True:
            lvl_up(player)
            player[3][1] += 10
            print("Vous récupérez 10 d'argent")
            sleep(2)
            break
    return player