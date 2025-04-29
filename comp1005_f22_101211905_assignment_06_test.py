#Trae Smith 101211905

import pygame
import random
def moving_pieces(moves, x,y)->(float, float): #moves the player based on the amount of moves rolled
    reverse_moves=0
    if ((moves*120)+x)>960:
        if y-77.14<38.57:
            print("You didn't land exactly on the final space. You gotta reverse!")
            for i in range(moves):
                if ((i*120)+x)==900:
                    reverse_moves=moves-i
                    if (900-(reverse_moves*120))<60:
                        y+=77.14
                        for j in range(reverse_moves):
                            if (900-(j*120))==60:
                              reverse_moves=reverse_moves-j
                    x=(900-(reverse_moves*120))
        else:
            y-=77.14
            for i in range(moves):
                if ((i*120)+x)==900:
                    moves=moves-i
            x=(((moves-1)*120)+60)
    else:
        x=(((moves)*120)+x)
    return x,y

def check_for_collisons(a,b,c,d)->(float,float): #checks if one player landed on the same spot as another player
    if a==c and b==d:
       print("You got to go all the way back to the front!")
       a,b=60,501.5
    return a,b

def win(a,b)->bool: #checks if a player landed on the final spot, a.k.a. has won
    if a==900 and b==int(38.57):
        finished=True
    else:
        finished=False
    return finished

def board_game_updater(a,b,c,d): #updates the board every time a player makes a move
    width=960
    length=540
    game_board=pygame.display.set_mode([width,length])
    game_board.fill([255,0,0])
    for i in range(8):
        for j in range(7):
            if ((i+j)%2)==1:
                pygame.draw.rect(game_board, (0,0,0), [(width/8)*i,int((length/7)*j), width/8, length/7])
    pygame.draw.circle(game_board,[0,255,0],(a,b),30)
    pygame.draw.polygon(game_board,[0,0,255],[(c,d-30),(c-25,d+20),(c+25,d+20)])
    pygame.display.update()
    pygame.time.delay(10000)
    pygame.display.quit()


#Main Code
print("Welcome to the Colliding Chaotic Competition.")
print("Player 1 is the green circle, and Player 2 is the blue triangle")
done=False
(x_1,y_1)=(60,501.5)
(x_2,y_2)=(60,501.5)
board_game_updater(x_1,y_1,x_2,y_2)
P1_turn=True
while done==False:
   if P1_turn==True:
       pygame.time.delay(5000)
       d1=random.randint(1,6)
       d2=random.randint(1,6)
       P1_moves=d1+d2
       print("Player 1 got a",d1,"and",d2,"for a total of",P1_moves)
       x_1,y_1=moving_pieces(P1_moves, x_1, y_1)
       x_1,y_1=check_for_collisons(x_1,y_1,x_2,y_2)
       complete=win(x_1,y_1)
       if complete==True:
           print("Congrats! Player 1 won!")
           done=True
           break
       board_game_updater(x_1,y_1,x_2,y_2)
       P1_turn=False


   elif P1_turn==False:
       pygame.time.delay(5000)
       d1=random.randint(1,6)
       d2=random.randint(1,6)
       P2_moves=d1+d2
       print("Player 2 got a",d1,"and",d2,"for a total of",P2_moves)
       x_2,y_2=moving_pieces(P2_moves, x_2, y_2)
       x_2,y_2=check_for_collisons(x_2,y_2,x_1,y_1)
       complete=win(x_2,y_2)
       if complete==True:
           print("Congrats! Player 2 won!")
           done=True
           break
       board_game_updater(x_1,y_1,x_2,y_2)
       P1_turn=True

