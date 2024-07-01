import random

def main():
    print("Hi! Let's play a game of rock, paper, scissors!")

    currentlyPlaying = [True]

    while(currentlyPlaying[0]):
        compChoice = computerChoice()
        uChoice = userChoice()

        showComputerChoice(compChoice)
        showUserChoice(uChoice)

        findWinner(compChoice, uChoice, currentlyPlaying)


#decides the computer's choice
def computerChoice() -> int:
    return random.randint(1,3)

#user decides their choice
def userChoice() -> int:
    isValid = False

    while(not isValid):
        try:
            uChoice = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))

            if(uChoice < 1 or uChoice > 3):
                print("=======Invalid Input=======")
            else:
                isValid = True
        except:
            print("=======Please enter an integer=======")
    return uChoice


#show computer's choice
def showComputerChoice(compChoice: int):
    print("\nThe Computer Chose: ", end="")

    if(compChoice == 1): print("Rock")
    elif(compChoice == 2): print("Paper")
    else: print("Scissors")

#show user's choice
def showUserChoice(uChoice: int):
    print("\nYou Chose: ", end="")

    if(uChoice == 1): print("Rock")
    elif(uChoice == 2): print("Paper")
    else: print("Scissors")


#determine the winner
def findWinner(compChoice: int, uChoice: int, play: list):
    #computer picked rock
    if(compChoice == 1):
        if(uChoice == 1): #tie
            print("\nIt's a tie! You both picked rock. Play again.")
            return
        elif(uChoice == 2): #user picked paper
            print("\nPaper beats rock! You won!")
            play[0] = False
            return
        else: #user picked scissors
            print("\nRock beats scissors. You lost.")
            play[0] = False
            return
    elif(compChoice == 2): #computer picked paper
        if(uChoice == 1): #user picked rock
            print("\nPaper beats rock. You lost.")
            play[0] = False
            return
        elif(uChoice == 2): #tie
            print("\nIt's a tie! You both picked paper. Play again.")
            return
        else: #user picked scissors
            print("\nScissors beats paper! You won!")
            play[0] = False
            return
    elif(compChoice == 3): #computer picked scissors
        if(uChoice == 1): #user picked rock
            print("\nRock beats scissors! You won!")
            play[0] = False
            return
        elif(uChoice == 2): #user picked paper
            print("\nScissors beats paper. You lost.")
            play[0] = False
            return
        else: #tie
            print("\nIt's a tie! You both picked scissors. Play again.")
            return


main()