import pygame

def map_1(place:int):
    indoor=(0,255,255)
    outdoors=(0,128,0)
    halls=(255,255,0)
    stairs=(255,255,255)
    map_screen=pygame.display.set_mode([480, 640])
    map_screen.fill([0, 0, 0])
    #First Floor of the map
    pygame.draw.rect(map_screen,(0, 255, 0), [190,590,100, 50]) #Entrance-1 (will be green)
    #Halls/Connectors (note: all halls will be yellow, they're not rooms)
    pygame.draw.rect(map_screen,halls,[230,540,20,50])
    pygame.draw.rect(map_screen,halls,[120,500,60,20])
    pygame.draw.rect(map_screen,halls,[300,500,10,20])
    pygame.draw.rect(map_screen,halls,[310,460,20,60])
    pygame.draw.rect(map_screen,halls,[210,470,20,10])
    pygame.draw.rect(map_screen,halls,[90,450,140,20])
    pygame.draw.rect(map_screen,halls,[30,560,20,30])
    pygame.draw.rect(map_screen,halls,[305,360,10,30])
    pygame.draw.rect(map_screen,halls,[385,360,20,10])
    pygame.draw.rect(map_screen,halls,[405,330,20,40])
    pygame.draw.rect(map_screen,halls,[365,370,20,30])
    pygame.draw.rect(map_screen,halls,[330,425,35,20])
    pygame.draw.rect(map_screen,halls,[375,470,20,30])
    pygame.draw.rect(map_screen,halls,[405,230,20,30])
    pygame.draw.rect(map_screen,halls,[250,10,150,20])
    pygame.draw.rect(map_screen,halls,[230,10,20,45])
    pygame.draw.rect(map_screen,halls,[400,10,20,40])
    pygame.draw.rect(map_screen,halls,[315,320,20,20])
    pygame.draw.rect(map_screen,halls, [255,320,60,10])
    pygame.draw.rect(map_screen,halls,[205,265,20,30])
    pygame.draw.rect(map_screen,halls,[240,165,20,60])
    pygame.draw.rect(map_screen,halls,[275,250,20,10])
    pygame.draw.rect(map_screen,halls,[395,550,10,40])
    pygame.draw.rect(map_screen,halls,[290,605,95,15])
    pygame.draw.rect(map_screen,halls,[55,600,135,10])


    #Indoor area (all indoors would be light blue, while outdoors would be dark green) except for stairs which would be white
    pygame.draw.rect(map_screen,indoor,[180,480,120,60]) # main lobby-2
    pygame.draw.rect(map_screen,indoor,[30,410,60,60]) #Office-4
    pygame.draw.rect(map_screen,indoor,[30,500,90,60]) #Visual Arts-3
    pygame.draw.rect(map_screen,indoor,[300,390,30,70])#Chemistry-6
    pygame.draw.rect(map_screen,indoor,[315,340,70,30])#Science-8
    pygame.draw.rect(map_screen,indoor,[400,260,30,70])#Biology-9
    pygame.draw.rect(map_screen,indoor,[365,400,30,70])#Physics-7
    pygame.draw.rect(map_screen,indoor,[375,500,50,50])#Lab-5
    pygame.draw.rect(map_screen,outdoors,[385,200,60,30])#Playground-10
    pygame.draw.polygon(map_screen,outdoors,[(445,200),(480,200),(445,230)])
    pygame.draw.polygon(map_screen,outdoors,[(385,200),(350,200),(385,230)])
    pygame.draw.polygon(map_screen,outdoors,[(385,50),(385,80),(350,80)])
    pygame.draw.polygon(map_screen,outdoors,[(445,80),(480,80),(445,50)])
    pygame.draw.rect(map_screen,outdoors,[385,50,60,30])
    pygame.draw.rect(map_screen,outdoors,[350,80,130,120])
    pygame.draw.circle(map_screen,outdoors,(240,110),60) #Garden-13
    pygame.draw.rect(map_screen,indoor,[235,305,20,40])#Gym-11
    pygame.draw.polygon(map_screen,indoor,[(255,345),(235,355),(235,345)])
    pygame.draw.polygon(map_screen,indoor,[(255,305),(235,295),(235,305)])
    pygame.draw.rect(map_screen,indoor,[175,295,60,60])
    pygame.draw.rect(map_screen,indoor,[225,225,50,50])#Janitor-12
    pygame.draw.rect(map_screen,stairs,[25,590,30,30])#StairsA-15
    pygame.draw.rect(map_screen,stairs,[295,240,30,30])#StairsB-14
    pygame.draw.rect(map_screen,stairs,[385,590,30,30])#StairsC-16

    center=[
    (0,0),
    (240,615),
    (240,510),
    (75,530),
    (60,440),
    (400,525),
    (315,425),
    (380,435),
    (350,355),
    (415,295),
    (415,140),
    (205,325),
    (250,250),
    (240,110),
    (310,255),
    (40,605),
    (400,605)
    ]
    places=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    for i in range(len(places)):
        if place==places[i]:
            pygame.draw.circle(map_screen,(255,0,0),center[i],5)


    pygame.display.update()
    pygame.time.delay(10000)
    pygame.display.quit()

def map_2(place:int):
    indoor=(0,255,255)
    halls=(255,255,0)
    outdoors=(0,128,0)
    stairs=(255,255,255)
    map_screen=pygame.display.set_mode([480, 640])
    map_screen.fill([0, 0, 0])
    #Second Floor of the map
    #Halls/Connectors (note: all halls will be yellow, they're not rooms)
    pygame.draw.rect(map_screen,halls,[35,490,10,100])
    pygame.draw.rect(map_screen,halls,[55,600,60,10])
    pygame.draw.rect(map_screen,halls,[250,600,135,10])
    pygame.draw.rect(map_screen,halls,[395,520,10,70])
    pygame.draw.rect(map_screen,halls,[275,250,20,10])
    pygame.draw.rect(map_screen,halls,[30,350,20,65])
    pygame.draw.rect(map_screen,halls,[60,445,40,10])
    pygame.draw.rect(map_screen,halls,[190,380,20,180])
    pygame.draw.rect(map_screen,halls,[225,350,30,10])
    pygame.draw.rect(map_screen,halls,[180,310,10,20])
    pygame.draw.rect(map_screen,halls,[305,350,70,15])
    pygame.draw.rect(map_screen,halls,[375,320,15,45])
    pygame.draw.rect(map_screen,halls,[190,240,35,20])
    pygame.draw.rect(map_screen,halls,[295,250,80,10])

    #Indoor area (all indoors would be light blue, while outdoors would be dark green) except for stairs which would be white
    pygame.draw.rect(map_screen,indoor,[110,560,140,60])#English-17
    pygame.draw.rect(map_screen,stairs,[25,590,30,30])#StairsA-15
    pygame.draw.rect(map_screen,stairs,[295,240,30,30])#StairsB-14
    pygame.draw.rect(map_screen,stairs,[385,590,30,30])#StairsC-16
    pygame.draw.rect(map_screen,indoor,[380,400,80,140])#Library-18
    pygame.draw.rect(map_screen,outdoors,[460,400,20,140])#Balcony-26
    pygame.draw.rect(map_screen,indoor,[225,225,50,50])#Janitor-12
    pygame.draw.rect(map_screen,indoor,[20,415,40,80])#Computer Science-20
    pygame.draw.rect(map_screen,indoor,[0,270,80,80])#Computer Lab-21
    pygame.draw.rect(map_screen,indoor,[100,425,50,50])#Mathematics-19
    pygame.draw.rect(map_screen,indoor,[175,330,50,50])#Drama-23
    pygame.draw.rect(map_screen,indoor,[255,330,50,50])#Music-24
    pygame.draw.rect(map_screen,indoor,[115,235,75,75])#Theatre-22
    pygame.draw.circle(map_screen,indoor,(152.5,235),37.5,draw_top_left=True,draw_top_right=True)
    pygame.draw.rect(map_screen,indoor,[375,240,80,80])#Band Area-25

    center=[
    (180,590),
    (40,605),
    (310,255),
    (400,605),
    (420,470),
    (470,470),
    (250,250),
    (40,455),
    (40,310),
    (125,450),
    (200,355),
    (280,355),
    (152.5,272.5),
    (415,280)
    ]
    places=[17,15,14,16,18,26,12,20,21,19,23,24,22,25]
    for j in range(len(places)):
        if place==places[j]:
            pygame.draw.circle(map_screen,(255,0,0),center[j],5)


    pygame.display.update()
    pygame.time.delay(10000)
    pygame.display.quit()

def moving_to_places(place:int,want:str,upper:bool):
    #[north,west,east,south,up,down]
    lower_potential_areas=[
    [0], #0 (there is no room 0;it will also be an error sign)
    [2,15,16], #1-Entrance
    [3,4,6,1], #2- Main Lobby
    [2], #3-Visual Arts
    [2,15], #4-Office
    [7,16], #5-Lab
    [8,7,2], #6-Chemistry
    [8,6,5], #7-Physics
    [11,6,9,7], #8-Science
    [10,8], #9-Biology
    [13,9], #10-Playground Area
    [12,8], #11-Gym
    [13,11,14,12], #12-Janitor_lower
    [10,12], #13-Garden
    [12,14], #14-StairsB_lower
    [4,1,15], #15-StairsA_lower
    [5,1,16], #16-StairsC_lower
    ]
    directions_for_LPA=[
    ["WEST"], #0
    ["NORTH","WEST","EAST"], #1
    ["NORTH","WEST","EAST","SOUTH"], #2
    ["EAST"], #3
    ["EAST","SOUTH"], #4
    ["NORTH","SOUTH"], #5
    ["NORTH","EAST","SOUTH"], #6
    ["NORTH","WEST","SOUTH"], #7
    ["NORTH","WEST","EAST","SOUTH"], #8
    ["NORTH","SOUTH"], #9
    ["NORTH", "SOUTH"], #10
    ["NORTH","EAST"], #11
    ["NORTH","WEST","EAST","UP"], #12
    ["NORTH","SOUTH"], #13
    ["WEST","UP"], #14
    ["NORTH","EAST","UP"], #15
    ["NORTH","WEST","UP"], #16
    ]
    higher_potential_areas=[
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [22,14,12],#12-Janitor_upper
    [],
    [12,25,14], #14-StairsB_upper
    [20,17,15], #15-StairsA_upper
    [18,17,16], #16-StairsC_upper
    [23,15,16], #17-English
    [26,16], #18-Library
    [20], #19-Mathematics
    [21,19,15], #20-Computer Science
    [20], #21-Computer Lab
    [23,12], #22-Theatre
    [17,22,24], #23-Drama
    [23,25],#24-Music
    [14,24], #25-Band Area
    [18] #26-Balcony
    ]
    directions_for_HPA=[
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    ["WEST","EAST","DOWN"], #12
    [],
    ["WEST","EAST","DOWN"], #14
    ["NORTH","EAST","DOWN"], #15
    ["NORTH","WEST","DOWN"], #16
    ["NORTH","WEST","EAST"], #17
    ["EAST","SOUTH"], #18
    ["WEST"], #19
    ["NORTH","EAST","SOUTH"], #20
    ["SOUTH"], #21
    ["SOUTH","EAST"], #22
    ["SOUTH","NORTH","EAST"], #23
    ["WEST","EAST"], #24
    ["WEST","SOUTH"], #25
    ["WEST"], #26
    ]
    if upper==False:
        if want.upper() in directions_for_LPA[place]:
            if want.upper()=="UP":
                upper=True
            for i in range(len(directions_for_LPA[place])):
                if directions_for_LPA[place][i].upper()==want.upper():
                    temp=place
                    place=lower_potential_areas[temp][i]
                    break
        else:
            print("That is not a valid path")
    else:
        if want.upper() in directions_for_HPA[place]:
            if want.upper()=="DOWN":
                upper=False
            for i in range(len(directions_for_HPA[place])+1):
                if directions_for_HPA[place][i].upper()==want.upper():
                    temp=place
                    place=higher_potential_areas[temp][i]
                    break
        else:
            print("That is not a valid path")
    return place,upper

def place_description(place:int,upper:bool):
    places_lower=[
    ["There is nothing here."],
    ["This is the entrance. Unless you have the key, you're not going to find anything here."],
    ["This is the Main Lobby. Usually have a lot of students in this area, but it's completely empty."],
    ["This is the Visual Arts. There is some paint and a paintbrush on the table."],
    ["This was the office, but it seems like a large part was blocked off; nothing to find here."],
    ["This is the Lab for all science students, there are some mysterious acid on the table."],
    ["This is the Chemistry class. nothing to find here."],
    ["This is the Physics class. nothing to find here."],
    ["This is the Science class. nothing to find here."],
    ["This is the Biology class. nothing to find here."],
    ["The large area of the playground have a lot of things, but you wouldn't be able to take anything but a soccer ball."],
    ["This is the gymnasium, where you found a pair of gloves."],
    ["This is the janitor's closet, seems you can go up a pair of stairs"],
    ["This is the garden. It used to be a beautiful sight, but now all of the plants and butterflies have died."],
    ["This is a pair of stairs, with a large letter 'B' on the side. Can only go up."],
    ["This is a pair of stairs, with a large letter 'A' on the side. Can only go up."],
    ["This is a pair of stairs, with a large letter 'C' on the side. Can only go up."]
    ]
    places_higher=[
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    ["This is the janitor's closet, seems you can go down a pair of stairs. There is also a pair of keys."],
    [],
    ["This is a pair of stairs, with a large letter 'B' on the side. Can only go down."],
    ["This is a pair of stairs, with a large letter 'A' on the side. Can only go down."],
    ["This is a pair of stairs, with a large letter 'C' on the side. Can only go down."],
    ["This is the English Classroom. A novel named 'Hamlet' is sitting on a desk."],
    ["This is the library, with many dusty books. None of them seem interesting."],
    ["This is the mathematics class. A geometry kit is lying down on the professor's desk."],
    ["This is the computer science class. Nothing is here."],
    ["This is the computer lab. A sheet of paper with a name 'Prof. C. Hillen' is written on it"],
    ["This is the theatre, where lots of performances are kept. A rose is on the stage."],
    ["This is the drama classroom, but it's barren. "],
    ["This is the music class. Usually it would be loud due to the music room close by, but not anymore. Nothing is here."],
    ["This is the band area. Only a trumpet is in this room that you can take."],
    ["This is the balcony by the library. It has a nice view, and there is another novel, 'Macbeth', on one of the desk."]
    ]
    if upper==False:
        print(places_lower[place])
    else:
        print(places_higher[place])


def taking_objects(pos:int,upper:bool,items:list,areas:list):
    objects=""
    if pos in areas:
        for i in range(len(areas)):
            if pos==areas[i]:
                objects=items[i]
                items.remove(objects)
                areas.remove(pos)
                print("You have received "+objects)
                break
    else:
        print("You are not at an area to take anything.")

    return items,areas,objects







#Main Code
upper_level=False
finished=False
current_pos=1
print("You ended up in an abandoned prestigious school, with the entrance locked. You do not know where the entrance key is, but you found a map.")
inventory=[]
potential_items=["key","paintbrush and paint","chemical","soccer ball","gloves","Hamlet","geometry kit","sheet of paper","rose","trumpet","Macbeth"]
area_to_look=[12,3,5,10,11,17,19,21,22,25,26]
while finished==False:
    action=input("What do you want to do?[move, examine, take, use, map, inventory]").upper()
    if action=="MOVE":
        direction= input("Which direction do you want to move? [North, South, East, West, Up, or Down]")
        current_pos,upper_level=moving_to_places(current_pos,direction,upper_level)
        place_description(current_pos,upper_level)
    elif action=="EXAMINE":
        place_description(current_pos,upper_level)
    elif action=="TAKE":
        potential_items,area_to_look,add_to_inven=taking_objects(current_pos,upper_level, potential_items,area_to_look)
        inventory.append(add_to_inven)
    elif action=="USE":
        if "key" in inventory:
            if current_pos==1:
                print("You used the key on the entrance lock, opening it. You leave wondering on what happened to the school that caused it to be abandoned.")
                finished=True
            else:
                print("You are not at the entrance.")
        else:
            print("You don't have the key. Get it so that you can use it.")
    elif action=="MAP":
        if upper_level==False:
            map_1(current_pos)
        else:
            map_2(current_pos)
    elif action=="INVENTORY":
        print(inventory)
    else:
        print("That is not a valid command")





