#Trae Smith 101211905
def pseudoleet(statement:str)->str: #transforms the words laughing out loud, hacker, newbie, the, and you to LOL, haxor, n00b, teh, and j00, respectively
    acronyms=["LOL", "haxor", "n00b","warez","teh","j00"]
    acronym_translator=["laughing out loud","hacker", "newbie","the","you"]
    for i in range(len(acronym_translator)):
        if acronym_translator[i] in statement.lower():
            find_out=len(acronym_translator[i])
            for j in range(len(statement.lower())):
                if statement[j-1:(j+find_out-1)].lower()==acronym_translator[i]:
                    statement=statement[:j-1]+acronyms[i]+statement[j+find_out-1:]
                    break

    return statement



def leet_speak(y:str)->str:         #transforms all of the vowels (including y) to ^(a),|=-(e),!(i),<>(o), L|(u), and \|/(y)
    homoglyphs=["^","|=-","!","<>","L|","\|/"]
    homoglyph_translator=["a","e","i","o","u","y"]
    acronyms=["LOL", "haxor", "n00b","warez","teh","j00"]
    count=0
    states=[]
    words=""

    for i in y:
        temporary=""
        if i==" ":
            states.append(words)
            words=""
            count+=1
        else:
            words+=i
    if words:
        states.append(words)
    holder=[True]*(count+1)
    for j in range(len(states)):
        for x in range(len(acronyms)):
            if states[j]==acronyms[x]:
                holder[j]=False                 #this prevents the acronyms to change their vowels
    for k in range(len(states)):
        if holder[k]==True:
            temporary=states[k]
            for l in range(len(states[k])-1):
                for m in range(len(homoglyph_translator)):
                    if temporary[l]==homoglyph_translator[m]:
                        temporary=temporary[:l]+homoglyphs[m]+temporary[l+1:]
                    states[k]=temporary

    new_state=""
    for z in range(len(states)):
        placer=str(states[z])
        new_state+=(placer+" ")
    final_count=0
    for i in new_state:
        if ord(i)>=97 and ord(i)<=122:                  #capitalize the lower case letters
            placements=chr(ord(i)-32)
            new_state=new_state[:final_count]+placements+new_state[final_count+1:]
        final_count+=1
    return new_state



#Main Code
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string_added = input("Enter a string")
sentence = ""
for char in string_added:
   if char not in punctuations:
       sentence = sentence + char
print(sentence)
sentence=pseudoleet(sentence)
print(sentence)
sentence=leet_speak(sentence)
print(sentence)





