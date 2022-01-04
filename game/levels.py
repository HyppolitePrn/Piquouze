from time import sleep
from ends import good_ending
from ends import ending
from ends import bad_ending

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

def end(player,os):
    if player[0][10] <= 2:
        good_ending(os)
    elif player[0][10] > 2 and player[0][10] < 5:
        ending(os)
    else:
        bad_ending(os)
