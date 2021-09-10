import random
import time
import pdb

player_score = 0
comp_score = 0
options = ["Rock", "Paper", "Scissors"]

def nicetype(self):
    for letter in self:
        print(letter, end = "")
        time.sleep(.04)
     
welcome = """WeLcOmE tO pEtE's MaGnIfIcEnT rOcK pApEr ScIsSoRs GaMe!!!!1!! <3 <3 <3
How many games would you like to play a \"best of\"?: 
"""
nicetype(welcome)

best_of = int(input(""))

while (best_of / 2) >= player_score and (best_of / 2) >= comp_score:
    player = input("Rock, Paper, or Scissors? ").capitalize()
    comp = options[random.randint(0, 2)]

    while True:
        if player in options:
            break
        else:
            pa_message = "Nah mate you've got to spell it right otherwise it won't work :(\nPick again: "
            nicetype(pa_message)
            player = input("").capitalize()
            
    print("You chose " + player)
    print("The computer chose " + comp)

    lose = "You lose this round."
    win = "YOU WIN THIS ROUND!"

    if player == comp:
        print("IT'S A DRAW!!! Let's play again.")
    elif player == "Rock":
        if comp == "Paper":
            print(lose)
            comp_score += 1
        else:
            print(win)
            player_score += 1
    elif player == "Paper":
        if comp == "Rock":
            print(win)
            player_score += 1
        else:
            print(lose)
            comp_score += 1
    elif player == "Scissors":
        if comp == "Rock":
            print(lose)
            comp_score += 1
        else:
            print(win)
            player_score += 1
    print("The score is now:\nYou: " + str(player_score) + "\nComputer: " + str(comp_score) + "\n")

input("Press Enter to exit")