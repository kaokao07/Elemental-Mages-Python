'''
Kao Vue
This game is based on Rock Paper Scissors. However, instead of using those objects, it's based on the magical elements:
fire, ice, and thunder.
User will input which object they would like as an element and the computer will randomly pick an element.
Whichever Mage (player or computer) that reaches 0 health points first is defeated. Both can be tie the battle!
Try to win the most battles to achieve victory and be the best Elemental Mage!
This game can be played repeatedly without rerunning PyCharm. Game will need to be rerun if you end game.
The reward gif will present based on user's and computer's outcome.
'''

import random
from namesDef import *
import webbrowser

# This sets the player wins and losses, their overall score, and both the Player and Computer health points.
player_win = 0
player_loss = 0
player_draw = 0
ultimate_player_win = 0
ultimate_player_loss = 0
ultimate_player_draw = 0
player_health = 100
computer_health = 100

names = {'f': "Fire", 'i': "Ice", 't': "Thunder"}  # Each Elements is assigned to a letter.

def instructions():
    print("Let's play some Elemental Magic!")
    ruleInput = input("Press Enter to Begin your battle or press i for game rules!")
    if ruleInput == "i":
        info()


def TheBattle(): # This is where battle takes place.
    global player_draw, player_loss, player_win
    global computer_health, player_health
    while True:
        player_element = input("Fire, Ice, or Thunder? (f, i, t):  ")
        if player_element not in ["f", "i", "t", "q"]:
            print("Incorrect Element. Cast a correct Element!\n")

        else:
            break

    computer_element = ['f', 'i', 't'][random.randrange(0, 3)]
    print("The element you chose is: ", player_element)
    print("The element computer chose is: ", computer_element, "\n")
    winning_combos = (('f', 'i'), ('i', 't'), ('t', 'f'))
    losing_combos = (('i', 'f'), ('f', 't'), ('t', 'i'))

    player_victory = (player_element, computer_element) in winning_combos
    computer_victory = (player_element, computer_element) in losing_combos

    if player_victory:
        print(names.get(player_element, "???") + " beats " + names.get(computer_element, "???"), "!")
        print("Damage dealt! Computer loses 10 HP!\n")
        player_win = player_win + 1
        computer_health = computer_health - 10
        print("Player Health: ", player_health)
        print("Computer Health: ", computer_health)

    elif computer_victory:
        print(names.get(computer_element, "???") + " beats " + names.get(player_element, "???."), "!")
        print("Took damage! Player loses 10 HP!\n")
        player_loss = player_loss + 1
        player_health = player_health - 10
        print("Player Health: ", player_health)
        print("Computer Health: ", computer_health)

    else:
        print("Both Mages cast", names.get(computer_element, "???") + " and " + names.get(player_element, "???."), "!")
        print("Whoa! Both Player and Computer take 10 damage!\n")
        player_draw = player_draw + 1
        player_health = player_health - 10
        computer_health = computer_health - 10
        print("Player Health: ", player_health)
        print("Computer Health: ", computer_health)

    if player_health and computer_health >= 10:
        print("Next Round! Fight on!\n")
        TheBattle()

    else:
        print("\nThat's game!")
        scoreResults()

def scoreResults():
    if player_win > player_loss:
        input("Press Enter to proceed...")
        print("\nCongrats. Now, fight more Mages and be the best Elemental Mage!\n")
        global ultimate_player_win
        ultimate_player_win = ultimate_player_win + 1

    if player_win < player_loss:
        input("Press Enter to proceed...")
        print("\nYou lost, but you should never give up! Always strive to be the better Elemental Mage!\n")
        global ultimate_player_loss
        ultimate_player_loss = ultimate_player_loss + 1

    if player_win == player_loss:
        input("Press Enter to proceed...")
        print("\nDraw! May the better Mage wins next time!\n")
        global ultimate_player_draw
        ultimate_player_draw = ultimate_player_draw + 1

def play_game():
    while TheBattle():
        scoreResults()
    while True:
        once_more = str(input("Do you wish to fight another battle? (y/n): "))
        if once_more == "y":
            global player_health, computer_health, player_win, player_loss, player_draw
            if player_health or computer_health >= 0:
                player_health = 100
                computer_health = 100
            if player_win or player_loss or player_draw > 0:
                player_win = 0
                player_loss = 0
                player_draw = 0
            TheBattle()
        else:
            if once_more == "n":
                return


def print_final_results():
    print("Player Final Health: ", player_health)
    print("Computer Final Health: ", computer_health, "\n")
    print("Total Magic Victories: ", ultimate_player_win)
    print("Total Magic Defeats: ", ultimate_player_loss)
    print("Total Magic Ties: ", ultimate_player_draw, "\n")

    if ultimate_player_win > ultimate_player_loss:
        input("Press Enter to proceed...")
        print("\nCongrats, you are the superior Elemental Mage! Now, hold that title proudly!\n")
        input("Press Enter to view your fate...")
        webbrowser.open('Victorous Vivi.gif')

    if ultimate_player_win < ultimate_player_loss:
        input("Press Enter to proceed...")
        print("\nYou lost, but you should never give up! Always strive to be the better Elemental Mage!\n")
        input("Press Enter to view your fate...")
        webbrowser.open('Defeated Vivi.gif')

    if ultimate_player_win == ultimate_player_loss:
        input("Press Enter to proceed...")
        print("\nLooks like you're just an average Mage. Always strive to be the best Elemental Mage.\n")
        input("Press Enter to view your fate...")
        webbrowser.open('Tie Vivi.gif')

def main():
    instructions()
    play_game()
    print_final_results()

main()
