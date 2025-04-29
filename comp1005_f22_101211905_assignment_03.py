import sys
C=int(sys.argv[3])==1
D=int(sys.argv[4])==1
E=int(sys.argv[5])==1
F=int(sys.argv[6])==1
G=int(sys.argv[7])==1
H=int(sys.argv[8])==1
L=int(sys.argv[12])==1
state1= ((not D and C)and E) or (not F)
state2= ((not G and H) and L) and (not G)
print("<",state1,",",state2,">")

