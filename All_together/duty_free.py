from liste import list_sell

def duty_free(player, menu_nav):
    choice = menu_nav(list_sell)
    if choice == "Potion":
        player[1].insert(len(player) - 2, "Gel Hydroalcoolique")
        player[4][1] = player[4][1] - 10

        return list_sell, player
    elif choice ==  "Masque chirurgical":
        player[2].append("Masque chirurgical")
        player[0][6] = player[0][6] + 3
        list_sell.remove("Masque chirurgical (defense), Xg")
        player[4][1] -= 100

        return list_sell, player
    elif choice == "Blouse de bataille":
        player[2].append("Blouse de bataille")
        player[0][6] += 3 
        list_sell.remove("Blouse de bataille (defense) Xg")
        player[4][1] -= 100

        return list_sell, player
    elif choice == "Seringue en adamantium":
        player[2].append("Seringue en adamantium")
        player[0][4] += 3
        list_sell.remove("Seringue en adamantium (attaque) Xg")
        player[4][1] -= 100

        return list_sell, player
    else:
        return 