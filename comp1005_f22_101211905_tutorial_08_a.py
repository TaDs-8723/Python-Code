import random

title=input("What should be the name of this tilemap file?")
name=title+".txt"
file=open(name,"w")
height=int(input("What should the height be?"))
width=int(input("What should the width be?"))
file.write("title:"+title+"\n")
listing=[]
for i in range(width):
    pseudo_list=[]
    for j in range(height):
        x=random.randint(0,4)
        pseudo_list.append(str(x))
        if j+1==height:
            file.write(str(x)+"\n")
        else:
            file.write(str(x)+",")
    #listing.append(pseudo_list)

file.close()
