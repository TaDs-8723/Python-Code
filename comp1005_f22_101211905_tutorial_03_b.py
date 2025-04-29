print("Good day, player, and welcome to the Oregon Trail!")
print("Starting with the professions, there are three professions that will grant you an initial balance of money")
print("You may choose from:", '\n',"1.)Be a banker from Boston",'\n',"2.)Be a carpenter from Ohio",'\n',"3.)Be a farmer from Illnois")
cash=0
initial_choice=int(input("What is your choice? [Choose the number associated with it]"))
if initial_choice>3 or initial_choice<1:
    print("That is not an option.")
if initial_choice==1:
    print("You are now a banker from Boston, moving onto the Oregon Trail. But before you go, you have obtained $1600.")
    cash=1600
if initial_choice==2:
    print("You are now a carpenter from Ohio, moving onto the Oregon Trail. But before you go, you have obtained $800.")
    cash=800
if initial_choice==3:
    print("You are now a farmer from Illnois, moving onto the Oregon Trail. But before you go, you have obtained $400.")
    cash=400
print("As you are travelling on the Oregon Trail, you arrived at a supply shop")
print("There are a number of objects that the shop sell, which are as follows: ")
print("1.) Oxen to help with your travels",'\n',"2.)Food to eat during your travels")
print("3.)Clothing to wear throughout all of the seasons",'\n',"4.)Extra ammo for your weapons (for self-defense)")
print("5.) Spare parts of your carriage, in case anything goes south")
checkout=0
leaving=False
while leaving==False:

    second_choice=int(input("which supply would you order? [Choose the number associated with it]"))

    if second_choice==1:
        print("An ox is $250")
        ox_number=int(input("How many ox/oxen do you want to order?"))
        checkout=checkout+(250*ox_number)

    if second_choice==2:
        print("A pound of food is $25")
        food_pound=int(input("How many pounds of food do you want to order?"))
        checkout=checkout+(25*food_pound)

    if second_choice==3:
        print("A piece of clothing is $5")
        clothing_piece=int(input("How many pieces of clothing do you want to order?"))
        checkout=checkout+(5*clothing_piece)

    if second_choice==4:
        print("A box of ammo is $75")
        ammo_box=int(input("How many boxes of ammo do you want to order?"))
        checkout=checkout+(75*ammo_box)

    if second_choice==5:
        print("A spare part is $50")
        spare_parts=int(input("How many spare parts do you want to order?"))
        checkout=checkout+(50*spare_parts)

    if second_choice>5 or second_choice<1:
        print("That is not an option here. Please try again")

    final_choice=input("Would you like to order something else [type order] or go to checkout [type checkout]?").upper()

    if final_choice=="CHECKOUT":
        if(checkout>cash):
            print("You do not have enough cash. Please try again.")
        else:
            leaving=True
            print("You have",cash-checkout,"dollars left. Come again soon!")












