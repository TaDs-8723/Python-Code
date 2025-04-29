import sys
y=float(sys.argv[1])
w=float(input("What would the second number be? : "))
x=w**7
print(x)
x=x//5
print(x)
x=x+y
print(x)
x=x+(x+1)
print(x)
x=x*0.002622
print(x)
x=int(x)
print(x)
if x<=1000000:
    chara=chr(x)
    print("<",chara,">")
else:
    print("There is no character that can be converted with this number. Please try a smaller set of number.")
