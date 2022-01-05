from os import system
from time import sleep
from liste import list_fight

#Fonction qui gère l'inventaire en appelant le menu de navigation
def inventory(player, os):
    if os == "mac":
        from menu_nav_mac import menu_nav_mac
        inv_choice = menu_nav_mac(player[1])
    elif os == "windows":
        from Menu_nav import menu_nav
        inv_choice = menu_nav(player[1])
    if inv_choice == "Potion":              #Seul objet du jeu, pour soigner, donc j'incrémente la valeur "hp" du joueur quand le choix est appelé
        player[0][2] = player[0][2] + 5
        if player[0][2] > player[0][4]:
            player[0][2] = player[0][4]
            print("Vous récupérez toute votre vie")
        else:
            print("Vous récupérez 5 pvs")
        player[1].remove("Gel Hydroalcoolique") #On supprime l'item de l'inventaire
        sleep(2)
        if os == "mac":
            system("clear")
        elif os == "windows":   #Je renvoie True pour indiquer qu'une action a été effectuée, et que mon "tour" est terminé
            system("cls")
        return player, True
    elif inv_choice == "Retour": #Je renvoie False pour que le joueur puisse seulement consulter son inventaire sans pour autant passer son tour
        if os == "mac":
            system("clear")
        elif os == "windows":
            system("cls")
        return player, False


#Calcul des dégats d'une attaque du monstre, on pourrait rendre ça + complet en donnant des attaques différentes, mais un randint a peu d'utilité pour ce projet
def monster_attack(player, monster, os):
    print(f"Le {monster[3]} attaque !")
    sleep(1)
    monsterDamage = monster[1] - player[0][8] #Dégats subits = Attaque du monstre - Défense du joueur
    if monsterDamage > 0:
        player[0][2] = player[0][2] - monsterDamage
        print("Il vous inflige", monsterDamage, "dégats")
    else:
        print("Tu n'as subi aucun dégat")
    sleep(2)
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    return player, monster

#On vérifie l'état des participants au combat
def check(player, monster):
    if monster[0] <= 0:
        print("Vous avez gagné le combat !")
        sleep(1)
        print("Vous gagnez 10 points d'expérience !")
        player[0][12] += 10
        return True     #En cas de victoire, on renvoie True pour dire que le joueur est en vie, et le programme continue
    elif player[0][2] <= 0:
        print("Vous êtes morts...")
        return False        #En cas de défaites, False pour couper le programme

#Fonction pour vacciner l'ennemi
def vaccine(monster, os, player):
    if monster[0] <= 3:
        print("Vous avez sauvé le", monster[3])
        sleep(1)
        player[0][12] += 2
        print("Vous avez gagné 2 points d'expérience !")
        sleep(1)
        if os == "mac":
            system("clear")
        elif os == "windows":
            system("cls")
        return True         #En cas de réussite, on renvoie un True pour mettre fin au combat 
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
        return False        #En cas d'échec car les conditions ne sont pas remplies, on renvoie False pour que le joueur ne perde pas son tour

#Fonction du calcul de dégats du joueur
def player_atk(player, monster, os):
    playerDamage = player[0][6] - monster[2]    #Dégats = Attaque du joueur - Défense du monstre (qui ne bouge pas de 0 par soucis de complexité d'équilibrage)
    if playerDamage > 0:    
        monster[0] = monster[0] - playerDamage
        if monster[0] < 0:
            monster[0] = 0
        print("Tu infliges", playerDamage, "dégats")
        sleep(1)
    else:
        print("Tu as infligé 0 dégats")
        sleep(1)
    return player, monster

#Fonction pour faire gagner un niveau et augmenter les stats du joueur
def lvl_up(player):
    if player[0][12] >= 10: #xp
        player[0][10] += 1  #lvl
        player[0][2] += 3   #pvs actuels
        player[0][4] += 3   #pvs max
        player[0][6] += 1   #atq
        player[0][12] = player[0][12] - 10 #reset de l'xp pour le niveau suivant
        print("Lvl up!")
        sleep(1)
        print("Vous gagnez +3 Pvs, +1 Attaque")
        sleep(1)
    return player

#Fonction qui envoie des messages indiquant que nos actions ont eu une conséquence à chaque début de combat en fonction du niveau
def sanity(player):
    if player[0][10] >= 2 and player[0][10] < 4:
        print("Vous sentez quelque chose...")
    elif player[0][10] >= 4 and player[0][10] < 5:
        print("Quelque chose ne va pas...")
    elif player[0][10] >= 5:
        print("Que la chasse commence !")

#Fonction globale du combat
def battle(player, monster, os):
    vax = False
    print("Vous engagez le combat contre", monster[3]) #Nom du monstre
    sleep(1)
    sanity(player)  #Indication des conséquences
    sleep(2)
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    while (player[0][2] > 0 and monster[0] > 0):
        sleep(0.3)
        print(f"PVs du ", monster[3], ":", monster[0], "\nVos PVs :", player[0][2], player[0][3], player[0][4])
        if os == "mac":         #On récupère l'OS pour appeler le bon menu de navigation et les clears (on verra ces vérifications plein de fois plus bas)
            from menu_nav_mac import menu_nav_mac       
            choice = menu_nav_mac(list_fight(player))
        elif os == "windows":
            from Menu_nav import menu_nav
            choice = menu_nav(list_fight(player))
        if os == "mac":
            system("clear")
        elif os == "windows":
            system("cls")
        while choice == "inv":  #Boucle qui permet d'utiliser l'inventaire
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
        while choice == "vax": #Boucle qui permet d'essayer de vacciner
            vax = vaccine(monster, os, player)
            if vax == True:
                player[3][1] += 10
                print("Pour vous remercier, la personne vous donne 10 d'argent")
                return player
            else:       #En cas d'échec, on rappelle le menu de combat
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
        if choice == "atk": #On lance l'attaque
            player, monster = player_atk(player, monster, os)
            if check(player, monster) == True:      #On vérifie que le monstre est encore en vie
                lvl_up(player)
                player[3][1] += 10  #Argent
                print("Vous récupérez 10 d'argent")
                sleep(2)
                break
        if vax != True: #Si le monstre n'est pas mort ou vacciné, il attaque
            player, monster = monster_attack(player, monster, os)
        if check(player, monster) == True:
            lvl_up(player)
            player[3][1] += 10 #Argent
            print("Vous récupérez 10 d'argent")
            sleep(2)
            break
    return player #On retourne le joueur pour que tous les changements soient pris en compte