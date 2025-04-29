x=input("What is your name?")
y=int(input("What year were you born on?"))
z=int(input("What is the current year?"))
age=z-y
leap_age=age//4
print(x,", Your age is",age,".")
print("If your birthday have not passed yet, you are", age-1,".")
print("If you were born on February 29, you are",leap_age,".")



