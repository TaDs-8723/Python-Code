#Trae Smith-101211905
def non_recursive(listing:list)->list:
    for i in range(len(listing)):
        if listing[i]%2==1:
            listing[i]+=10
    return listing

def recursive(listing:list, count=0):
    final_list=listing
    if count+1<=len(listing):
        final_list[count]=final_list[count]+(10*(final_list[count]%2))
        return recursive(final_list,count+1)
    else:
        return final_list


x=non_recursive([5,4,5,6,3,6,8])
y=recursive([5,4,5,6,3,6,8])
print(non_recursive([5,4,5,6,3,6,8]))
print(recursive([5,4,5,6,3,6,8]))
if x==y:
    print('Test Passed')
else:
    print('Test Failed')


