import pygame

drawing_screen=pygame.display.set_mode([480, 640])
drawing_screen.fill([255, 255, 255])
pygame.draw.rect(drawing_screen, (68, 80, 140), [0,0,160, 106])
pygame.draw.polygon(drawing_screen, (68, 80, 140), [(160,0), (160, 105), (240, 105)])
pygame.draw.rect(drawing_screen, (93, 70, 50), [80, 320, 160, 107])
pygame.draw.polygon(drawing_screen, (93, 70, 50), [(80, 320), (160, 320), (80, 213)])
pygame.draw.polygon(drawing_screen, (93, 70, 50), [(80, 427), (160, 427), (160, 533)])
pygame.display.update()
pygame.time.delay(10000)
pygame.image.save(drawing_screen, "assigned_image_for_101211905.png")
pygame.display.quit()
