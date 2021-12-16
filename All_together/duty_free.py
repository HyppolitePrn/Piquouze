def duty_free(player, sell_fonction, sell):
    choice = sell_fonction
    if choice == "Potion":
        if player[3][1] >= 10:
            player[1].insert(len(player) - 2, "Gel Hydroalcoolique")
            player[3][1] = player[3][1] - 10
        else:
            print("Tu n'as pas assez d'argent")
        return sell, player
    elif choice ==  "Masque chirurgical":
        if player[3][1] >= 100:
            player[2].append("Masque chirurgical")
            player[0][6] += 1
            sell.remove("Masque chirurgical + 1 défense : 100")
            player[3][1] -= 100
        else:
            print("Tu n'as pas assez d'argent")
        return sell, player
    elif choice == "Blouse de bataille":
        if player[3][1] >= 100:
            player[2].append("Blouse de bataille")
            player[0][6] += 3 
            sell.remove("Blouse de bataille + 3 défense : 100")
            player[3][1] -= 100
        else:
            print("Tu n'as pas assez d'argent")

        return sell, player
    elif choice == "Seringue en adamantium":
        if player[3][1] >= 100:
            player[2].append("Seringue en adamantium")
            player[0][4] += 3
            sell.remove("Seringue en adamantium +3 attaque : 100")
            player[3][1] -= 100
        else:
            print("Tu n'as pas assez d'argent")
        return sell, player
    else:
        return 