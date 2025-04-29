#Trae Smith 101211905
import pygame
import sys

def transform(x:int,y:int,image_surface:pygame.surface):
    #transforms the surrounding area of where you clicked, with the place you clicked in the middle
    for i in range(x-20,x+20):
        for j in range(y-20,y+20):
            (r,g,b)= image_surface.get_at((i,j))[:3]
            reverse_color=(255-r,255-g,255-b)
            image_surface.set_at((i,j),reverse_color)
    pygame.display.update()
running = True
filename="
picture=pygame.image.load(filename) #loads the image, then get the height and width
height=picture.get_height()
width=picture.get_width()
drawing_board=pygame.display.set_mode([width, height]) #creates a surface and blit the image onto the surface
drawing_board.blit(picture,(0,0))
pygame.display.update() #shows the image to the viewer
finished=False
while running:
    pygame.init()
    for e in pygame.event.get():
        if pygame.mouse.get_pressed()==(1,0,0):
            x,y=pygame.mouse.get_pos()
            transform(x,y,drawing_board)
        if e.type == pygame.QUIT:
            running = False #need help; if player types quit, then it will stop the loop and quit the display
            pygame.display.quit()
