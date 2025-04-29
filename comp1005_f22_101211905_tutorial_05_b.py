#Trae Smith 101211905
import random

def rock_paper_scissors(): #Runs rock, paper, scissors
    print("This game is called 'Rock, Paper, Scissors'.")
    pc=input("What do you choose? [Rock, paper, or scissors]").upper()
    choices=["ROCK","PAPER", "SCISSORS"]
    cc=random.choice(choices)
    if pc in choices:
        if cc==pc:
            print("We both said "+comp_choice+". Let's try again!")
        else:
            if (cc=="ROCK" and pc== "PAPER") or (cc== "PAPER" and pc=="SCISSORS") or (cc=="SCISSORS" and pc=="ROCK"):
                print("You said",pc,"and I said",cc,". You won, Good Game!")
            else:
                print("You said",pc,"and I said",cc,". I won, Good Game!")
    else:
        print("That was not a valid response, and as such you lost. Sorry")


def tic_tac_toe(): #Runs tic-tac-toe
    X=[]
    O=[]
    print("This is a game called Tic-Tac-Toe.")
    print("The grid represented by numbers; 1 being the left top corner and it counts up from left to right, then up to down")
    choices=[1,2,3,4,5,6,7,8,9]         #sets the possible choices
    wins=[[1,4,7],[2,5,8],[3,6,9],[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7]]      #sets the possible wins
    finished=False                          #runs until the game is finished, either the computer wins or the player wins
    while finished==False:
        place=int(input("where do you want to place it?[between 1 and 9]"))     #prompts the user to pick a number between 1 and 9
        if place not in choices:
            print("That is not a valid response, and as such you lost. Sorry")  #if user picks a different number, stops the game
            break
        else:
            X.append(place)
            choices.remove(place)
        cc=random.choice(choices)
        O.append(cc)
        choices.remove(cc)
        print("X [you] have the following spaces",X,"while O [me] have the following spaces",O,".")
        print("The following spaces are still available",choices)
        for i in range(len(wins)):
            if all(item in X for item in wins[i])==True:
                print("Congrats! you won!")
                finished=True
                break
            elif all(item in O for item in wins[i])==True:
                print("I won! Good Game!")
                finished=True
                break
        if len(choices)==0 and X not in wins and O not in wins:
            print("Board is filled and neither one of us won. Good game though!")






#Main Code
print("Welcome to 'Simple Games', where you can choose between Tic-Tac-Toe or Rock, Paper, Scissors")
ini_cho=input("Which one would you choose? [Tic for Tic-Tac-Toe or Rock for Rock,Paper, Scissors]").upper()
if ini_cho=="TIC":
    tic_tac_toe()
elif ini_cho=="ROCK":
    rock_paper_scissors()
else:
    print("That is not a valid option.")











