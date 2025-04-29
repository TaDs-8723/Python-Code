x=0
total=0
stop=False
while stop==False:
    total=int(input("What is the maximum number between 1 and 9 (which can include those numbers)?"))
    if total<=0 or total>9: #verifies if the number given is between 0 and 10 (not inclusive)
        print("That is not allowed. Please try again.")
    else:
        stop=True

for i in range(total+1):
    for j in range(i):
        print(j*str(j))
