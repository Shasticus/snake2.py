
"""My attempt at rock paper scissors."""

from random import randint
import pygame
import sys

pygame.init()

print(sys.executable)

#Background setup
choice = ["sword", "axe", "lance"]
ai = choice[randint(0,2)]
player = False

aiwin, pwin = 0, 0

while not player:
    while aiwin < 3 and pwin < 3:
        print(f"\n The score is {pwin} to {aiwin}")
        player = input("Sword, Axe, or Lance? ")

        if player == "q":
            quit()
        if player == ai:
            print("An equal clash of wills!")
        elif player == choice[0]:
            if ai == choice[1]:
                print(f"You've sliced your foe's {ai} with precision.")
                pwin += 1
            else:
                print(f"Your foe's {ai}'s reach has seen to your defeat.")
                aiwin += 1
        elif player == "axe":
            if ai == "lance":
                print(f"Your brutal swing is superior to that wimpy {ai}")
                pwin += 1
            else:
                print(f"{ai} are for bitches. Unfortunately it's faster.")
                aiwin += 1
        elif player == "lance":
            if ai == "sword":
                print(f"Reach beats {ai}'s speed in this battle.")
                pwin += 1
            else:
                print(f"Axes are the perfect weapon. Shoulda known better")
                aiwin += 1
        else:
            print("You shouldn't be here, warrior.")
            print(player)
        ai = choice[randint(0, 2)]

    if pwin > aiwin:
        choice = input("\nYou've won. this time. Again? Y/N")
        if choice == "y":
            player = False
            aiwin, pwin = 0, 0
        else:
            print("Farewell!")
            player = True
    elif pwin < aiwin:
        choice = input("You were slain, but you can rise again.. Y/N")
        if choice == "y":
            player = False
            aiwin, pwin = 0, 0
        else:
            print("Begone!")
            player = True



