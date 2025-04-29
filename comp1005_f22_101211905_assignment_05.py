import sys
import random
import pygame

def image_to_surface(picture:pygame.image)->pygame.surface:
    #creates the surface based on the height and width scale by a factor of 6
    height=picture.get_height()
    width=picture.get_width()
    drawing_board=pygame.display.set_mode([width*6, height*6])
    return drawing_board

def k_chooser(r, g, b)->int:
    #Takes the rgb for each pixel, calculates the average, and return a number of black circles based on the average
    black=0
    if((r+g+b)/3)<=51:
        black=3
    elif 51<((r+g+b)/3)<=102:
        black=2
    elif 102<((r+g+b)/3)<=153:
        black=1

    return black

def rgb_chooser(color)->int:
    #Takes the r,g,or b for each pixel and return a number of red, green, or blue circles based on the average, respectively
    pixels=0
    if color<=51:
        pixels=1
    if color<=102:
        pixels=2
    elif color<=153:
        pixels=3
    elif color<=204:
        pixels=4
    elif color<=255:
        pixels=5

    return pixels

def rgb_placer(k:int,r:int,g:int,b:int, new_pic:pygame.surface,a:int,z:int,x:int,y:int)->pygame.surface:
    #uses a small area within (a and x) as x-bounds, and (z and y) as y-bounds
    #Then, randomize within those bounds and draw a small circle for the amount of black, red, green, and blue circles
    for i in range(k):
        c=random.randint(a,x)
        d=random.randint(z,y)
        pygame.draw.circle(new_pic,[0,0,0],(c,d),1)
    for i in range(r):
        c=random.randint(a,x)
        d=random.randint(z,y)
        pygame.draw.circle(new_pic,[255,0,0],(c,d),1)
    for i in range(g):
        c=random.randint(a,x)
        d=random.randint(z,y)
        pygame.draw.circle(new_pic,[0,255,0],(c,d),1)
    for i in range(b):
        c=random.randint(a,x)
        d=random.randint(z,y)
        pygame.draw.circle(new_pic,[0,0,255],(c,d),1)
    return new_pic

def rgb_finder(picture:pygame.image,drawing_board:pygame.surface)->pygame.surface: #find and prints each pixel's color, then calls the

    x=int(picture.get_width())
    y=int(picture.get_height())
    for i in range(x):
        for j in range(y):
            (r,g,b)= picture.get_at((i,j))[:3]
            black=k_chooser(r,g,b)
            red=rgb_chooser(r)
            green=rgb_chooser(g)
            blue=rgb_chooser(b)
            rgb_placer(black, red, green, blue, drawing_board,6*(i-1),6*(j-1),6*i,6*j)
    return drawing_board


filename="Aur_.jpg"
picture=pygame.image.load(filename)
drawing_board=image_to_surface(picture)
final=rgb_finder(picture,drawing_board)
pygame.display.update()
pygame.time.delay(5000)
pygame.image.save(final, "Updated_Version_Of_"+filename)
pygame.display.quit()
