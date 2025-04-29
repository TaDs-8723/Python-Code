import pygame
drawing_screen=pygame.display.set_mode([500, 500])
drawing_screen.fill([255,255,255])

#face
pygame.draw.circle(drawing_screen, [0,0,0], [240,105], 45)
pygame.draw.circle(drawing_screen, [0,0,0], [285,105], 10, draw_top_right=True, draw_bottom_right=True)
pygame.draw.circle(drawing_screen, [255,255,255], [262,125], 10)
pygame.draw.circle(drawing_screen, [255,255,255], [260, 95],4)
pygame.draw.circle(drawing_screen, [0,0,0], [288,88],4)

#body
pygame.draw.circle(drawing_screen, [0,0,0], [240, 190], 30, draw_top_right=True, draw_top_left=True)
pygame.draw.polygon(drawing_screen, [0,0,0], [(210, 190), (270, 190), (210, 290), (270, 290)])
pygame.draw.polygon(drawing_screen, [0,0,0], [(210, 190), (210, 290), (240,240)])
pygame.draw.polygon(drawing_screen, [0,0,0], [(270,190), (270, 290), (240,240)])

#legs and feet
pygame.draw.arc(drawing_screen, [0,0,0], [200, 280, 80, 200], 0, 1.5708, 5 )
pygame.draw.arc(drawing_screen, [0,0,0], [125, 240, 100, 100], 4, 0, 5)
pygame.draw.line(drawing_screen, [0,0,0], [143,327], [129, 346], 5)
pygame.draw.line(drawing_screen, [0,0,0], [279, 380], [303,380],5)

#arms and hands
pygame.draw.arc(drawing_screen, [0,0,0], [155,200,80, 60],0, 2,5)
pygame.draw.arc(drawing_screen, [0,0,0], [215,160,80,60],4,6,5)
pygame.draw.circle(drawing_screen, [0,0,0], [290,200],7)
pygame.draw.circle(drawing_screen, [0,0,0], [180,205], 7)

#misc (air and prop)
pygame.draw.line(drawing_screen, [135, 206, 235], [288,127], [295,127],2)
pygame.draw.line(drawing_screen, [135, 206, 235], [288, 130], [293, 135],2)
pygame.draw.line(drawing_screen, [135,206,235], [288, 124], [293, 119],2)
pygame.draw.line(drawing_screen, [255, 215,0], [300, 170], [290,230], 5)
pygame.draw.polygon(drawing_screen, [75,0,130], [(290,173),(298,180),(290,183)])
pygame.draw.polygon(drawing_screen, [75,0,130],[(305,178), (305,188), (298,180)])
pygame.draw.circle(drawing_screen, [255,0,0],[300,170],4)

pygame.display.update()
pygame.time.delay(5000)
pygame.display.quit()
