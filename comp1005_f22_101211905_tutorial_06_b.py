import random


the_list=[]
length=int(input("How many random integers do you want in the list?"))
for i in range(length):
    the_list.append(random.randint(0,length))
print(the_list)
running=True
while running:
    ask1=input("Do you want to quit and count the amount of words?").upper()
    if ask1=="NO":
        ask_num=int(input("Which number do you want to replace?"))
        ask_replace=input("And what is the word do you want to replace it with?")
        for i in range(length):
            if type(the_list[i])==int:
                if int(the_list[i])==ask_num:
                    the_list[i]=ask_replace
    elif ask1=="YES":
        running=False
    else:
        print("That is not a valid statement. Please try again.")

desired=input("Which word do you want to see the number of times that would pop up in this list?")
count=0
for j in range(length):
    if the_list[j]==desired:
        count+=1
print(count)
