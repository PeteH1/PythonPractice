import random
import time

def nicetype(text, time_gap = 0.04):
    for letter in text:
        print(letter, end = "")
        time.sleep(time_gap)
     
welcome = """WeLcOmE tO pEtE's MaGnIfIcEnT rOcK pApEr ScIsSoRs GaMe!!!!1!! <3 <3 <3
How many games would you like to play a \"best of\"?: 
"""
nicetype(welcome)

best_of = int(input(""))

player_score = 0
comp_score = 0
options = ["Rock", "Paper", "Scissors"]

while (best_of / 2) >= player_score and (best_of / 2) >= comp_score:
    player = input("Rock, Paper, or Scissors? ").capitalize()
    comp = options[random.randint(0, 2)]

    while True:
        if player in options:
            break
        else:
            pa_message = "Nah mate you've got to spell it right otherwise it won't work :(\nPick again: "
            nicetype(pa_message, 0.02)
            player = input("").capitalize()

    countdown = "3...\n2...\n1...\n"
    nicetype(countdown, 0.15) 
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

if player_score > (best_of / 2):
    win_message = """CONGRATULATIONS, YOU HAVE WON!!!1!!
Bask in your victory or press Enter to exit.
"""
    nicetype(win_message)
    input("")
else:
    lose_message = """Unfortunately you have lost :'(
Sit and come to terms with the misery of your defeat or press Enter to exit.
"""
