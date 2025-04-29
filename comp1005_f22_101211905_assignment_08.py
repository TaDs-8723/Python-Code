#Trae Smith 101211905
import pygame

def draw_eyes():
    x,y=[150,250] #set coordinates
    pygame.draw.circle(win_sfc,[255,255,255],(x-35,y-50),30) #eyes
    pygame.draw.circle(win_sfc,[255,255,255],(x+35,y-50),30)

    pygame.draw.circle(win_sfc,[0,0,0],(x-35,y-50),5)       #pupils
    pygame.draw.circle(win_sfc,[0,0,0],(x+35,y-50),5)

    pygame.draw.circle(win_sfc,[255,0,0],(x+35,y-50),30,draw_top_right=True,draw_top_left=True) #eyelids
    pygame.draw.circle(win_sfc,[255,0,0],(x-35,y-50),30,draw_top_right=True,draw_top_left=True)

    pygame.draw.arc(win_sfc,[0,0,0],[x-60,y-40,50,30],3.5,6)    #eyelids
    pygame.draw.arc(win_sfc,[0,0,0],[x+10,y-40,50,30],3.5,6)

def draw_hat()->str:
    x,y=[250,350]#set coordinates
    pygame.draw.arc(win_sfc,[255,255,255],[x-90,y-175,180,150],0,3.14159,90) #hat

    pygame.draw.circle(win_sfc,[255,0,0],(x,y-130),5) #logo
    pygame.draw.circle(win_sfc,[255,0,0],(x,y-130),20,5)

    pygame.draw.rect(win_sfc,[255,0,0], [x-90,y-100,180,40]) #brim
    pygame.draw.arc(win_sfc,[255,0,0],[x-91,y-74,80,25],3.14159,0,40)
    pygame.draw.arc(win_sfc,[255,0,0],[x+10,y-74,80,25],3.14159,0,40)

    name="baseball hat" #name of the hat
    return name

def draw_mouth(x:int,y:int):
    pygame.draw.arc(win_sfc,[0,0,0],[x-40,y+45,80,40],0.523599,2.61799,40) #mouth
    pygame.draw.arc(win_sfc,[0,0,0],[x-35,y+50,20,20],2.6,5.75,10)
    pygame.draw.arc(win_sfc,[0,0,0],[x+15,y+50,20,20],3.5,1.1,10)

    pygame.draw.arc(win_sfc,[255,0,0],[x-10,y+57,20,10],6.1,3.3,10) #tongue

    pygame.draw.arc(win_sfc,[255,255,255],[x-20,y+45,40,15],0.523599,2.61799,40)    #teeth
    pygame.draw.line(win_sfc,[0,0,0],(x-10,y+47),(x-10,y+50))
    pygame.draw.line(win_sfc,[0,0,0],(x,y+45),(x,y+50))
    pygame.draw.line(win_sfc,[0,0,0],(x+10,y+47),(x+10,y+50))




