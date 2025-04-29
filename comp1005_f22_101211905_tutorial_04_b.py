import random
guess=0
x=int(random.randint(1,100))
stop=False #signifies if it should stop (True) or not stop (False)
while stop==False:
    go=int(input("What is your the number?"))
    if (go!=x) and (guess>=9):
        print("Sorry, you lost the game. The number is",str(x)+".")
    elif go<x:
        print("Your guess is lower than the actual number.")
        print("You have",(10-(guess+1)),"guesses left.")
    elif go>x:
        print("Your guess is higher than the actual number.")
        print("You have",(10-(guess+1)),"guesses left.",'\n')
    else:
        print("After",guess+1,"times, You got it!")
        guess=9
    if guess==9:
        stop=True
    guess=guess+1
