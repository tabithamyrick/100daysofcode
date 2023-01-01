import random as rand

#vars 
playagain = True
playerWins = False
choiceImgArray = [
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
,

# Paper
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
,

# Scissors
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

]

choiceStrArry = [
    "Rock", 
    "Paper",
    "Scissors"
]

def pickwinner(player, computer):
    youWon = (player == 0 and computer == 2) or (player == 2 and computer == 1) or (player == 1 and computer == 0)
    if(youWon):
        print(choiceImgArray[player])
        print("\nYou Picked " + choiceStrArry[player])
        print(choiceImgArray[computer])
        print("\nThe computer played " + choiceStrArry[computer])
        print("\n " + choiceStrArry[computer] + "Beats" + choiceStrArry[computer])
    else:
        print(choiceImgArray[player])
        print("\nYou Picked " + choiceStrArry[player])
        print(choiceImgArray[computer])
        print("\nThe computer played " + choiceStrArry[computer])
        print("\n " + choiceStrArry[computer] + "Beats" + choiceStrArry[computer])
    return youWon

while(playagain):
#accept player input
    playerChoice = input("Let's Play a game of rock(0), paper(1), scissors(2)\nWhat is your choice: ")
    #select computer choice
    computerChoice = rand.randint(0,2)
    #compare and declaire a winner
    if(int(playerChoice) < 3):
        playerWins = pickwinner(int(playerChoice), int(computerChoice))
    else:
        playagain = True
        continue
    if(playerWins):
        print("You Won!!!!!!")
    else:
        print("You Lost.....")

    replay = input("Play Again y/n?\n")

    if(replay == "y"):
        playagain = True
        continue
    else:
        playagain = False
        break


#prompt to play again