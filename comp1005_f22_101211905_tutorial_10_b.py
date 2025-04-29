#Trae Smith-101211905
def non_recursive_captial(listed:list)->list:
    vowels=['a','e','i','o','u']
    for i in range(len(listed)):
        if listed[i] in vowels:
            listed[i]=listed[i].upper()
    return listed

def recursive_captial(listed:list,count=0)->list:
    if count+1<=len(listed):
        vowels=['a','e','i','o','u']
        if listed[count] in vowels:
            listed[count]=listed[count].upper()
        return recursive_captial(listed,count+1)

    else:
        return listed


x=recursive_captial(['a','b','c','R','E','i'])
y=non_recursive_captial(['a','b','c','R','E','i'])
print(recursive_captial(['a','b','c','R','E','i']))
print(non_recursive_captial(['a','b','c','R','E','i']))
if x==y:
    print('Test Passed')
else:
    print('Test Failed')


