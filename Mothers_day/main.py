#import pgzrun 
import pygame
import os 
x = 50
y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"
pygame.init() 

WIDTH = 1000

HEIGHT = 1000 
oia = pygame.image.load('Mothers_day\images\oia.jpg') 
boy = 
screen = pygame.display.set_mode((1000,1000)) 
isrunning = True
while isrunning :
    screen.fill('magenta') 
    screen.blit(oia,(0,0))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrunning = False 
    pygame.display.update() 

pygame.quit()

    













#pgzrun.go()