#This is between the swashbuckler and esponiage subgenres mentioned in the subgenre website (both under adventure)
print("Welcome to the mini Akinator: Adventure Edition")
instructions_check=input("Would you like some instructions?").upper()
if (instructions_check=="YES"):
    print("You can choose a movie. I will ask you a set of questions, and you will answer yes if it is correct and no if it is incorrect.")
    print("I will then try to guess the movie based on the questions you answered based on a small list. If it is not there, you have stumped me.")
    print("If it is, however, I win.")

#These strings are to prevent repetitive strings throughout the code
correct="Yes, I am correct! Have a nice day."
incorrect="Damn, i have been stumped. Good job!"
failure="That is not a valid response. Please restart and try again."

answer_1=input("does it have calm and cool spies in their movies?").upper()#seperates between either swashbuckler or esponiage
if answer_1=="YES":
    answer_2=input("does it have a character named James Bond?").upper()#seperates all of the James bond films
    if answer_2=="YES":
        answer_3=input("did they gamble in the movie?").upper()#seperates between the 2 casino royales and no time to die
        if answer_3=="YES":
            answer_4=input("Did they play a game of Texas Hold 'Em?").upper() #differentiates the 2; baccarat is 1967 film and texas hold 'em is 2006
            if answer_4=="YES":
                potential_result=input("Was it the 2006 film Casino Royale?").upper() #confirms if it is correct
                if potential_result=="YES":
                    print(correct)
                elif potential_result=="NO":
                    print(incorrect)
                else:
                    print(failure)
            elif answer_4=="NO":
                potential_result=input("Was it the 1967 film Casino Royale?").upper() #confirms that this is correct
                if potential_result=="YES":
                    print(correct)
                elif potential_result=="NO":
                    print(incorrect)
                else:
                    print(failure)
        elif answer_3=="NO":
            potential_result=input("Was it the film No Time To Die?").upper()
            if potential_result=="YES":
                print(correct)
            elif potential_result=="NO":
                print(incorrect)
            else:
                print(failure)

    elif answer_2=="NO":
        answer_3=input("What about a character named Ethan Hunt?").upper() #seperates all of the Mission Impossible films
        if answer_3=="YES":
            answer_4=input("Was Ethan Hunt framed as a mole in the movie?").upper() #checks if it is the first Mission Impossible
            if answer_4=="YES":
                potential_result=input("Is this movie the original Mission Impossible?").upper() #verify if it is the correct film
                if potential_result=="YES":
                    print(correct)
                elif potential_result=="NO":
                    print(incorrect)
                else:
                    print(failure)
            elif answer_4=="NO":
                answer_5=input("Did the government disavows the IMF?").upper() #checks if it is Mission Impossible:Ghost Protocol
                if answer_5=="YES":
                    potential_result=input("Is the film Mission Impossible: Ghost Protocol?").upper() #verify if this is the answer
                    if potential_result=="YES":
                        print(correct)
                    elif potential_result=="NO":
                        print(incorrect)
                    else:
                        print(failure)
                elif answer_5=="NO":                                            #If not, then it would assume it is Mission Impossible: Fallout
                    potential_result=input("Is the film Mission Impossible: Fallout?")
                    if potential_result=="YES":
                        print(correct)
                    elif potential_result=="NO":
                        print(incorrect)
                    else:
                        print(failure)
            else:
                print(failure)
        elif answer_3=="NO":
            answer_4=input("Is this film also a comedy?").upper()#Seperates all of the Austin Powers films, if not then it will ask if it is the film "Face/Off"
            if answer_4=="YES":
                answer_5=input("Was Austin Powers and Dr.Evil revealed as twin brothers?").upper()#Checks if it is the film Austin Powers in Goldmember
                if answer_5=="YES":
                    potential_result=input("Is it the film Austin Powers in Goldmember?").upper() #verification
                    if potential_result=="YES":
                        print(correct)
                    elif potential_result=="NO":
                        print(incorrect)
                    else:
                        print(failure)
                elif answer_5=="NO":
                    answer_6=input("Did Austin Powers and Dr.Evil go back in time?").upper() #Checks if it is Austin Powers: The Spy Who Shagged Me
                    if answer_6=="YES":
                        potential_result=input("Is this film Austin Powers: The Spy Who Shagged Me?").upper() #verification
                        if potential_result=="YES":
                            print(correct)
                        elif potential_result=="NO":
                            print(incorrect)
                        else:
                            print(failure)
                    elif answer_6=="NO":       #If it isn't either, it will assume it is Austin Powers: International Man of Mystery
                        potential_result=input("Is this film Austin Powers: International Man of Mystery?").upper()
                        if potential_result=="YES":
                            print(correct)
                        elif potential_result=="NO":
                            print(incorrect)
                        else:
                            print(failure)
                    else:
                        print(failure)
                else:
                    print(failure)

            elif answer_4=="NO":
                potential_result=input("Is this movie named 'Face/Off'?").upper() #Will reply to your answer to this statement
                if potential_result=="YES":
                    print(correct)

                elif potential_result=="NO":
                    print(incorrect)
                else:
                    print(failure)
            else:
                print(failure)
        else:
            print(failure)
    else:
        print(failure)

elif answer_1=="NO":
    answer_2=input("Is it a well-known story?").upper() #seperates between 2 sets
    if answer_2=="YES": #either the franchises 3 musketeers, robin hood, pirates of the caribbean, and the legend of Zorro
        answer_3=input("Does the franchise have a sequel?").upper() #seperates the franchise Robin Hood from the other franchises
        if answer_3=="YES":
            answer_4=input("Is it a sequel?").upper() #seperates the 3 sequels with the 3 prequels
            if answer_4=="YES":
                answer_5=input("Is there multiple main characters?").upper() #seperates the 4 musketeers (3 musketeers sequel) from the others
                if answer_5=="YES":
                    potential_result=input("Is it the 4 Musketeers?") #verification
                    if potential_result=="YES":
                        print(correct)
                    elif potential_result=="NO":
                        print(incorrect)
                    else:
                        print(failure)
                elif answer_5=="NO":
                    answer_6=input("Does the main character have a crew?").upper() #differentiates between the P.O.T.C and The Legend of Zorro
                    if answer_6=="YES":
                        potential_result=input("Is it The Pirates of the Caribbean: Dead Man's Chest?").upper() #verification
                        if potential_result=="YES":
                            print(correct)
                        elif potential_result=="NO":
                            print(incorrect)
                        else:
                            print(failure)
                    elif answer_6=="NO":
                        potential_result=input("Is it The Legend of Zorro?").upper() #verification
                        if potential_result=="YES":
                            print(correct)
                        elif potential_result=="NO":
                            print(incorrect)
                        else:
                            print(failure)
                    else:
                        print(failure)
                else:
                    print(failure)
            elif answer_4=="NO":
                answer_5=input("Is there multiple main characters?").upper() #seperates the 3 musketeers sequel from the others
                if answer_5=="YES":
                    potential_result=input("Is it the 3 Musketeers?").upper() #verification
                    if potential_result=="YES":
                        print(correct)
                    elif potential_result=="NO":
                        print(incorrect)
                    else:
                        print(failure)
                elif answer_5=="NO":
                    answer_6=input("Does the main character have a crew?").upper() #differentiates between the P.O.T.C and The Mask of Zorro
                    if answer_6=="YES":
                        potential_result=input("Is it The Pirates of the Caribbean: The Curse of The Black Pearl?").upper() #verification
                        if potential_result=="YES":
                            print(correct)
                        elif potential_result=="NO":
                            print(incorrect)
                        else:
                            print(failure)
                    elif answer_6=="NO":
                        potential_result=input("Is it The Mask of Zorro?").upper() #verification
                        if potential_result=="YES":
                            print(correct)
                        elif potential_result=="NO":
                            print(incorrect)
                        else:
                            print(failure)
                    else:
                        print(failure)
                else:
                    print(failure)
            else:
                print(failure)
        elif answer_3=="NO":
            answer_4=input("Does it take place in the year 1194?").upper() #differentiates between the adventures of Robing Hood, and Robin Hood: Prince of Thieves
            if answer_4=="YES":
                potential_result=input("Is it Robin Hood: Prince of Thieves?").upper() #verification
                if potential_result=="YES":
                    print(correct)
                elif potential_result=="NO":
                    print(incorrect)
                else:
                    print(failure)
            elif answer_4=="NO":
                potential_result=input("Is it The Adventures of Robin Hood?").upper() #verification
                if potential_result=="YES":
                    print(correct)
                elif potential_result=="NO":
                    print(incorrect)
                else:
                    print(failure)
            else:
                print(failure)
    elif answer_2=="NO": #either The Golden Blade or The Crimson Pirate
        answer_3=input("Did the movie begin with a battle between 2 cities?").upper() #seperates between The Golden Blade and The Crimson Pirate
        if  answer_3=="YES":
            potential_result=input("Is the movie The Golden Blade?").upper() #verification
            if potential_result=="YES":
                print(correct)
            elif potential_result=="NO":
                print(incorrect)
            else:
                print(failure)
        elif answer_3=="NO":
            potential_result=input("Is the movie The Crimson Pirate?").upper() #verification
            if potential_result=="YES":
                print(correct)
            elif potential_result=="NO":
                print(incorrect)
            else:
                print(failure)
        else:
            print(failure)
    else:
        print(failure)
else:
    print(failure)
