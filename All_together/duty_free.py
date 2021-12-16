list_sell = ["Gel Hydro (soin) X g",
    "Masque chirurgical (defense), Xg",
    "Blouse de bataille (defense) Xg",
    "Seringue en adamantium (attaque) Xg",
    "Retour"

]
def duty_free(gold,player):
    choice = menu_nav(list_sell)
    if choice == "Potion":
        player[1].insert(len(player) - 2, "Gel Hydroalcoolique")
        gold = gold - heal_price 

        return gold, list_sell, player
    elif choice ==  "Masque chirurgical":
        player[2].append("Masque chirurgical")
        player[0][6] = player[0][6] + 3
        list_sell.remove("Masque chirurgical (defense), Xg")
        gold -= masque_price

        return gold, list_sell, player
    elif choice == "Blouse de bataille":
        player[2].append("Blouse de bataille")
        player[0][6] += 3 
        list_sell.remove("Blouse de bataille (defense) Xg")
        gold -= blouse_price

        return gold, list_sell, player
    elif choice == "Seringue en adamantium":
        player[2].append("Seringue en adamantium")
        player[0][4] += 3
        list_sell.remove("Seringue en adamantium (attaque) Xg")
        gold -= seringue_price

        return gold, list_sell, player
    else:
        return 