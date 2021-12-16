def duty_free(player, sell_fonction, sell):
    choice = sell_fonction
    if choice == "Potion":
        player[1].insert(len(player) - 2, "Gel Hydroalcoolique")
        player[3][1] = player[3][1] - 10

        return sell, player
    elif choice ==  "Masque chirurgical":
        player[2].append("Masque chirurgical")
        player[0][6] = player[0][6] + 3
        sell.remove("Masque chirurgical (defense), Xg")
        player[3][1] -= 100

        return sell, player
    elif choice == "Blouse de bataille":
        player[2].append("Blouse de bataille")
        player[0][6] += 3 
        sell.remove("Blouse de bataille (defense) Xg")
        player[3][1] -= 100

        return sell, player
    elif choice == "Seringue en adamantium":
        player[2].append("Seringue en adamantium")
        player[0][4] += 3
        sell.remove("Seringue en adamantium (attaque) Xg")
        player[3][1] -= 100

        return sell, player
    else:
        return 