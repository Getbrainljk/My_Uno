#!/bin/python
# -*- coding: utf-8-

##        Projet Uno
##
##      Made by nadir arbia
##  for Epitech (Paris)
##

import random
import time
import sys

VALID_CHOICE    = ("\n\tPlease enter a valid choice.\n")
NO_CARD_TO_PLAY = ("\n\tThere is no card to play.\n")
DRAW_EFFECT     = ("DRAW EFFECT !")

# method verifiant si une IA gagne
def     check_winner():
    z = 0
    while (z < 3):
        z += 1
        if len(players[z]) == 0:
            print ("PLAYER", z + 1, " WINS!")
            exit(0)

# Tours des 3 IA
def     computurn(players, currentCard, stack, colour, skipper, reverse):
    
    # Mise en place des statuts nécessaires à l'effet reverse
    player = 1
    if reverse == True:
        player = 3

    while player > 0 and player < 4:
        
       # Actualisation de l'effet reverse
        direction = 1
        if reverse == True:
            direction = -1
        
        played = False
        if skipper == player:
            print (DRAW_EFFECT)
            print ("> Player %i has been forced to pass his turn." % (player + 1))
            time.sleep(1)
            played = True
        for card in range(0, len(players[player])):
            # En excluant le multi, cherche une correspondance avec la carte actuelle à jouer
            if played == False and players[player][card][0] != '(Multicolor)'\
            and (players[player][card][0] == currentCard[0] or players[player][card][1] == currentCard[1]
                 or (currentCard[0] == '(Multicolor)' and colour in players[player][card][0])):
            
                # Remplacement de la carte actuelle et retrait de la main
                print ("Player %i has played %s." % (player + 1, players[player][card]))
                currentCard = players[player][card]
                players[player].remove(players[player][card])
                
                # Gestion des +2
                if currentCard[1] == '+2':
                    player_reset = 0
                    print ("EFFECT +2 !")
                    if player == len(players) - 1 or player + direction == 0:
                        print ("> You have picked a card.")
                        time.sleep(1)
                        print ("> You have picked a card.")
                        time.sleep(1)
                        player_reset = 4
                    else :
                        print ("> Player %i has picked a card." % (player + 1 + direction))
                        time.sleep(1)
                        print ("> Player %i has picked a card." % (player + 1 + direction))
                        time.sleep(1)
                    players[player + 1 - player_reset].append(stack.pop())
                    players[player + 1 - player_reset].append(stack.pop())

                # Gestion des draw
                elif currentCard[1] == 'draw':
                    skipper = player + direction
                    if skipper > 3:
                        skipper = 0

                # Gestion des reverse
                elif currentCard[1] == 'reverse':
                    reverse = not reverse
                
                # Fin de la recherche par break et fin du tour par played
                played = True
                break
            
        # Si aucune correspondance, utilisation des multi ou pioche    
        if played == False:
            if any('(Multicolor)' in s for s in players[player]):
                colour = list[random.randint(0, 3)]
                # Recherche du multi à utiliser
                for card in range(0, len(players[player])):
                    if players[player][card][0] == '(Multicolor)':
                        currentCard = players[player][card]  
                        players[player].remove(players[player][card])
                        break

                # Gestion du +4
                if currentCard[1] != '+4':
                    print ("Player %i has played Multicolor for %s." % (player + 1 + direction, colour))
                else:
                    print ("Player %i has played Multicolor +4 for %s." % (player + 1 + direction, colour))
                    print ("EFFECT +4 !")
                    player_reset = 0
                    if player == len(players) - 1:
                        print ("> You have picked a card.")
                        time.sleep(1)
                        print ("> You have picked a card.")
                        time.sleep(1)
                        print ("> You have picked a card.")
                        time.sleep(1)
                        print ("> You have picked a card.")
                        time.sleep(1)
                        player_reset = 4
                    else :
                        print ("> Player %i has picked a card." % (player + 1 + direction))
                        time.sleep(1)
                        print ("> Player %i has picked a card." % (player + 1 + direction))
                        time.sleep(1)
                        print ("> Player %i has picked a card." % (player + 1 + direction))
                        time.sleep(1)
                        print ("> Player %i has picked a card." % (player + 1 + direction))
                        time.sleep(1)
                    players[player + 1 - player_reset].append(stack.pop())
                    players[player + 1 - player_reset].append(stack.pop())
                    players[player + 1 - player_reset].append(stack.pop())
                    players[player + 1 - player_reset].append(stack.pop())
            else:
                players[player].append(stack.pop())
                print ("Player %i has picked a card." % (player + 1))
 
        time.sleep(1)
                
        if reverse == False:
            player = player + 1
        else:
            player = player - 1
    return (players, currentCard, stack, colour, skipper, reverse)


#####################################################################################################


# Création de la pioche
list = ('Blue', 'Green', 'Red', 'Yellow')
values = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "draw", "reverse")
stack = [];

for i in range(0, 4):
    stack.append((list[i], "0"))
    for value in range(0, len(values)):
        stack.append((list[i], values[value]))
        stack.append((list[i], values[value]))


# 2 exceptions gérées  de facons distinctes : les Multicolor et Multicolor +4
for i in range (0, 4):    
    stack.append(('(Multicolor)', 'simple'))
    stack.append(('(Multicolor)', '+4'))

# Shuffle de la pioche
for i in range(0, len(stack) - 1):
    rand = random.randint(0, len(stack) - 1)
    stack[i], stack[rand] = stack[rand], stack[i]

    

print ("\nWELCOME TO UNO!\n4 players.\n")

players = [[], [], [], []]

# Distribution des cartes
for card in range(0, 28):
    players[card % 4].append(stack.pop())

currentCard = stack.pop()

print ("Current card is", currentCard)

# Initialisation des statuts
start = True
colour = ""
skipper = -1
reverse = False


# Gestion des effets de cartes de départ
if '+2' in currentCard[1]:
    print ("EFFECT +2 !")
    print ("> You picked a card.")
    print ("> You picked a card.\n")
    players[0].append(stack.pop())
    players[0].append(stack.pop())

elif '+4' in currentCard[1]:
    print ("EFFECT +4 at START !")
    print ("> You have picked a card.")
    time.sleep(1)
    print ("> You have picked a card.")
    time.sleep(1)
    print ("> You have picked a card.")
    time.sleep(1)
    print ("> You have picked a card.")
    time.sleep(1)
    players[0].append(stack.pop())
    players[0].append(stack.pop())
    players[0].append(stack.pop())
    players[0].append(stack.pop())
    
elif 'draw' in currentCard[1]:
    skipper = 0

elif 'reverse' in currentCard[1]:
    reverse = not reverse


# Démarrage de la boucle de tour du joueur jusqu'à victoire ou défaite
while (True):
    check_winner()

    # Application de l'effet draw sur le joueur, réinitialisation de l'effet draw
    if skipper == 0:
        print ("DRAW EFFECT !")
        print ("You have been forced to pass your turn.")
        time.sleep(1)
        players, currentCard, stack, colour, skipper, reverse = computurn(players, currentCard, stack, colour, skipper, reverse)
    skipper = -1

    # Affichage de votre main
    print ("\nYour hand :\n")
    for i in range(0, len(players[0])):
        print ("Card %i : %s" % (i + 1, players[0][i]))

  
    # Choix unique entre 1 ou 2, vérifie qu'une carte puisse être jouée
    choice = input("\nEnter your choice : ")
    if (choice == '1' and (any(currentCard[0] in s for s in players[0]) or any(currentCard[1] in s for s in players[0])
                           or any('(Multicolor)' in s for s in players[0])
                           or (currentCard[0] == '(Multicolor)' and start == True)
                           or (currentCard[0] == '(Multicolor)' and any(colour in s for s in players[0])))):

        # Demande le choix de la carte à jouer, vérifie ce choix si valide ET jouable, break si ok
        while True:
            card = input("Select the number of the card you intend to play : ")
            if card.isdigit() == False:
                print ("\n\tInvalid value.\n")
            else:
                card = int(card) - 1
                if card < 0 or card >= len(players[0]):
                    print ("\n\tInvalid value.\n")
                elif (players[0][card][0] != '(Multicolor)' and currentCard[0] == '(Multicolor)'
                      and colour != players[0][card][0] and start == False):
                    print ("\n\tYou cannot play that.\n")
                elif (currentCard[0] != '(Multicolor)' and players[0][card][0] != '(Multicolor)'
                      and currentCard[0] not in players[0][card][0] and currentCard[1] not in players[0][card][1]):
                    print ("\n\tYou cannot play that.\n")
                else:
                    print ("You have played", players[0][card])
                    break

        # Remplacement de la carte actuelle, retrait de la carte +2, multi ou autre, détection d'une possible victoire
        currentCard = players[0][card]
        players[0].remove(players[0][card])
        if len(players[0]) == 0:
            exit ("YOU WIN !")

        # Actualisation de l'effet reverse
        player = 1
        direction = 1
        if reverse == True:
            player = 3
            direction = -1
            
        # Gestion d'un multi, demande le choix de la couleur à jouer, break si ok
        if currentCard[0] == '(Multicolor)':
            if currentCard[1] == '+4':
                  print ("EFFECT +4 !")
                  print ("> Player %i has picked a card." % (player + 1))
                  time.sleep(1)
                  print ("> Player %i has picked a card." % (player + 1))
                  time.sleep(1)
                  print ("> Player %i has picked a card." % (player + 1))
                  time.sleep(1)
                  print ("> Player %i has picked a card." % (player + 1))
                  time.sleep(1)
                  players[player].append(stack.pop())
                  players[player].append(stack.pop())
                  players[player].append(stack.pop())
                  players[player].append(stack.pop())
            while True:
                colour = input("1 : Blue\n2 : Green\n3 : Red\n4 : Yellow\nChoose a colour : ")
                if colour.isdigit() == False:
                    print ("Invalid value")
                else:
                    colour = int(colour)
                    if colour <= 0 or colour > 4:
                        print ("Invalid value")
                    else:
                        colour = list[colour - 1]
                        print ("Simple Multicolor used for :", colour)
                        break
                    
        # Gestion d'un +2, 
        elif currentCard[1] == '+2':
             print ("EFFECT +2 !")
             print ("> Player %i has picked a card." % (player + 1))
             time.sleep(1)
             print ("> Player %i has picked a card." % (player + 1))
             time.sleep(1)
             players[player].append(stack.pop())
             players[player].append(stack.pop())

        # Gestion d'un draw
        elif currentCard[1] == 'draw':
            skipper = 1

        # Gestion d'un reverse
        elif currentCard[1] == 'reverse':
            reverse = not reverse
            
        # Tour des ia
        start = False
        players, currentCard, stack, colour, skipper, reverse = computurn(players, currentCard, stack, colour, skipper, reverse)

    elif (choice == '1'):
        print (NO_CARD_TO_PLAY)
    elif (choice == '2'):
        print ("You have picked a card.")
        players, currentCard, stack, colour, skipper, reverse = computurn(players, currentCard, stack, colour, skipper, reverse)

        # Pioche vide
        if (len(stack) == 0):
            for i in range(0, 4):
                stack.append((list[i], "0"))
                for value in range(0, len(values)):
                    stack.append((list[i], values[value]))
                    stack.append((list[i], values[value]))
        else:
            players[0].append(stack.pop())

    else:
        print (VALID_CHOICE)

