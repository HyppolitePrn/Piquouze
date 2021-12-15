from time import sleep
#player = [["Stats", "Pv:", 10, "Attaque:", 2, "Défense:", 0, "Lvl:", 1, "XP:", 10, "/10"], ["Inventaire:", "Gel Hydroalcoolique"], ["Equipement:"]]
player = [["Stats:", "Pv:", 10, "Attaque:", 4, "Défense:", 0, "Lvl:", 1, "XP:", 0], ["Inventaire:", "Gel Hydroalcoolique"], ["Equipement:"]]


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
"""
def end(player):
    if player[0][8] <= 2:
        good_ending()
    elif player[0][8] > 2 and player[0][8] < 5:
        ending()
    else
        bad_ending()
""" 
