#Trae Smith-101211905
import pygame
def from_beginning(file:list)->int:     #runs each line of the text one line at a time
    running=True                   #turns off the function once the user presses X
    count=0                     #counts for it to run resuming
    pygame.display.init()       #initializes the display and font
    pygame.font.init()
    while running:
        end_time=0              #for the first running segement
        for i in file:
            name=i[:len(i)-1]
            height=100
            while (height-40)>0:        #repeats when height reaches a certain threshold (when it becomes 40, as the text disappears from the screen at that time)
                background=pygame.display.set_mode((960, 540))      #replaces a new background each loop
                background.fill([0,0,0])
                time=(pygame.time.get_ticks()/1000)-end_time #time in seconds minus the time from the previous loop
                height=(100-(2*time))                           #get the height based on time
                font=pygame.font.SysFont('franklingothicheavy',int(height),bold=True)   #similar font and color from Star Wars credits
                text=font.render(name, True, [255,255,0])
                width=text.get_width()
                starting_point=480-(width/2)                            #makes sure the text will be in the middle of the screen; even if it comes off of the screen
                background.blit(text,(starting_point,(height*10)-460))
                pygame.display.update()
                pygame.time.delay(50)                                   #delays for 50 milliseconds then repeats
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:   #turns off the display once they press X
                        running=False
                        pygame.display.quit()
                        return count
                        break
            count+=1
            end_time=pygame.time.get_ticks()/1000       #resets the height based on each line
        if count==len(file):                    #if they finished all of the lines, it would stop running
            running=False

def resume(counting:int, file:list)->int: #ths is similar from the code above, but it starts at where it left off
    i=counting
    running=True
    while running:
        end_time=0
        while i<len(file):
            name=i[:len(i)-1]
            height=100
            while (height-40)>0:
                background=pygame.display.set_mode((960, 540))
                background.fill([0,0,0])
                time=(pygame.time.get_ticks()/1000)-end_time
                height=(100-(2*time))
                font=pygame.font.SysFont('franklingothicheavy',int(height),bold=True)
                text=font.render(name, True, [255,255,0])
                width=text.get_width()
                starting_point=480-(width/2)
                background.blit(text,(starting_point,(height*10)-460))
                pygame.display.update()
                pygame.time.delay(50)
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        running=False
                        pygame.display.quit()
                        return count
                        break
            count+=1
            end_time=pygame.time.get_ticks()/1000
        if count==len(file):
            running=False

name=input("What is the name of your text file?")
files=[]
count=0
try:
    file=open(name,"r")
    for i in file:
        files.append(i)
    if count==0:
        count=from_beginning(files)
    else:
        count=resuming(count,files)

except:
    print("That is not a valid name")
