from random import randint
from os import system

def pierre_feuille_ciseaux(os):
  print("Début du programme")
  victoire_ordi=0
  nul=0
  victoire_player=0
  while True:
    print("Vous avez", victoire_player,"points et l'ordinateur a", victoire_ordi,"points")
    joueur=input("Entrez votre coup: (p)ierre, (f)euille, (c)iseaux ou (q)uitter: " )
    while joueur!="p" and joueur!="f" and joueur!="c" and joueur!="q":
      joueur=input("Entrez votre coup: (p)ierre, (f)euille, (c)iseaux ou (q)uitter: " )
    if joueur=="q":
      print("Vous avez quitté le jeu")
      print("Fin du programme")
      return

    if joueur=="p":
      print("PIERRE contre...", end=" ")
    if joueur=="f":
      print("FEUILLE contre...", end=" ") 
    if joueur=="c":
      print("CISEAUX contre...", end=" ")   

    randomOrdi=randint(1,3)
    if randomOrdi==1:
      ordi="p"
      print("PIERRE")
    if randomOrdi==2:
      ordi="f"
      print("FEUILLE")
    if randomOrdi==3:
      ordi="c"
      print("CISEAUX")

    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")

    if joueur==ordi:
      print("Partie nulle !")
    elif joueur=="p" and ordi=="c":
      print("Vous avez gagné ?")
      victoire_player=  victoire_player+1  
    elif joueur=="f" and ordi=="p":
      print("Vous avez gagné ?")
      victoire_player=  victoire_player+1
    elif joueur=="c" and ordi=="f":
      print("Vous avez gagné ?")
      victoire_player=  victoire_player+1 
    elif joueur=="p" and ordi=="f":
      print("Vous avez perdu ?")
      victoire_ordi=victoire_ordi+1 
    elif joueur=="f" and ordi=="c":
      print("Vous avez perdu ?")
      victoire_ordi=victoire_ordi+1
    elif joueur=="c" and ordi=="p":
      print("Vous avez perdu ?")
      victoire_ordi=victoire_ordi+1
    if victoire_player==3:
      return "win"
    if victoire_ordi==3:
      return "loose"     


def lancer_de(os):
  i = 1
  find_me = randint(1, 6)
  while i < 4:
    print("Lancez le dé et essayez de trouver la valeur cachée. Vous avez trois essais.")
    print("Manche", i)
    lance = input("Pour lancer votre dé faites espace puis entrée: ")
    while lance != " ":
      lance = input("Pour lancer votre dé faites espace puis entrée: ")
    values = randint(1, 6)
    if values == find_me:
      print("Vous avez trouvé le bon chiffre !!")
      return "win"
    if os == "mac":
        system("clear")
    elif os == "windows":
        system("cls")
    print("La valeur de votre dé est: ", values)
    i = i + 1
  print("Vous avez perdu !!")
  return "loose"

def just_prix():
  print("Bonne Chance !")
  values=randint(1,500) 
  i=0
  while i<10:
    number_1=int(input("Devinez un nombre entre 1 et 500, vous avez 10 essais : "))
    if number_1>values:
      print("Trop grand")
    elif number_1<values:
      print("Trop petit")
    if number_1!=values:
      i= i+1
    if number_1==values:
      return "win"
  return "loose" 
