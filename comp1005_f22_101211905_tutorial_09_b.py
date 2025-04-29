#Trae Smith-101211905
import random
import time

def check_sort(nums:list)->bool:    #Checks if the list is sorted in ascending order
    sort=True
    for j in range(len(nums)-1):
        k=j+1
        while k<len(nums):
            if nums[j]>nums[k]:
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


#Main Code
average1=0
average2=0
i=2
while i<=10:                                #The length of the list
    count=0
    x=10                                    #The amount of trials for each length of different lists
    while count<x:
        total1=0
        total2=0
        lists1=[random.randint(0,100)]
        for j in range(i):
            lists1.append(random.randint(0,100))
        lists2=lists1
        stop=False
        while stop==False:
           time_begin=time.time()
           stop,lists1=Bogosort(lists1)     #find the time between each Bogosort trial for a total of x trials
           time_end=time.time()
           total1+=time_end-time_begin
        stop2=False
        while stop2==False:                 #find the time between each Bozosort trial for a total of x trials
           time_begin=time.time()
           stop2,lists2=Bozosort(lists2)
           time_end=time.time()
           total2+=time_end-time_begin
        count+=1
    average1=total1/x                       #The total time of Bogosort divided by the number of trials
    average2=total2/x                       #The total time of Bozosort divided by the number of trials
    print("for trial",i-1,"\tBogosort:",average1,"\tBozosort:",average2)
    i+=1



