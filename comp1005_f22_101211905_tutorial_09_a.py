#Trae Smith-101211905
import random

def check_sort(x:list)->bool:
    sort=True
    for j in range(len(x)-1):
            k=j+1
            while k<len(x):
                if x[j]>x[k]:
                    sort=False
                k+=1
    return sort


def Bogosort(nums:list):
    for i in range(len(nums)):
        x=random.randint(0,len(nums)-1)
        temp=nums[x]
        nums[x]=nums[i]
        nums[i]=temp
    sort=check_sort(nums)
    return sort,nums

def Bozosort(nums:list):
    pick=False
    while pick==False:
        j=random.randint(0,len(nums)-1)
        k=random.randint(0,len(nums)-1)
        if k!=j:
            pick=True
    temp=nums[k]
    nums[k]=nums[j]
    nums[j]=temp
    sort=check_sort(nums)
    return sort,nums



def Main():
    x1=False
    x2=False
    numbers1=[1,2,5,3,4,5,7,8,9,6]
    numbers2=numbers1
    num1=0
    num2=0
    while x1==False:
        x1,numbers1=Bogosort(numbers1)
        num1+=1
    while x2==False:
        x2,numbers2=Bozosort(numbers2)
        num2+=1
    print("It took",num1,"trials to put Bogosort in order.")
    print("It took",num2,"trials to put Bozosort in order.")

Main()






