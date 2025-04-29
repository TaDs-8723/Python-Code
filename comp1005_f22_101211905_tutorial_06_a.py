run=True
the_list=[]
num=0
while run:
    answer=input("Do you want to add an integer to the list[ADD], remove the final element from the list[REMOVE], or quit[QUIT]?").upper()
    if answer=="ADD":
        add_ins=int(input("Which integer do you want to add in?"))
        if num==0:
            the_list.append(add_ins)
            num+=1
        else:
            placing=int(input("Where do you want to place your integer?"))
            if placing>num:
                print("That is not a valid position to place it at. Please try again.")
            else:
                num+=1
                the_list.insert(placing-1,add_ins)

    elif answer=="REMOVE":
        if len(the_list)>0:
            num-=1
            the_list.pop()
        else:
            print("The list is empty. Please add in at least one integer to the list to use this feature.")


    elif answer=="QUIT":
        run=False
        print(num)
        print(the_list)
    else:
        print("That is not a valid answer, please try again.")
