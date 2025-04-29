#Trae Smith 101211905

def prime_nums(x:int)->bool: #looks at the given number to see if it is a prime number or not
    prime=True
    for i in range(x-2):
        if x%(i+2)==0:
            prime=False

    return prime

#Main Code
finished=False
while finished==False:
    num=int(input("Pick a number to see if it is a prime number or not."))
    check=prime_nums(num)
    if check==True:
        print("Your number is a prime number.")
    else:
        print("Your number is not a prime number.")

    end=input("Do you want to leave?[yes or no]").upper()
    if end=="YES":
        finished=True

