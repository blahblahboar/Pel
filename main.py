
from __future__ import division
import pygame
import time
import random


pygame.init()
global w,h
width, height = 600,900
pygame.display.init()
screen = pygame.display.set_mode((width,height))
black = (0,0,0)
screen.fill(black)
paddle = pygame.image.load("paddle.png")

lives = 3
paddlepos = 1  # position of paddle
screen.fill(black)
pygame.display.flip()
Red = pygame.image.load("red.png")
Blue = pygame.image.load("blue.png")
Green = pygame.image.load("green.png")
Yellow = pygame.image.load("yellow.png")
White = pygame.image.load("white.png")
blobdict = {1:Red, 2: Blue, 3: Green, 4: Yellow, 5: White}







while 1:
    blobs = []  # blobs have attribute (type-> color), (gravity), 
    lasttime = time.time()
    counter = 0
    level = 1
    while 1:
        screen.fill(black)
        screen.blit(paddle, (188*paddlepos-170,870))
        counter+= 1
        Clock = pygame.time.Clock()
        Clock.tick(40)
            
        
        if time.time()- lasttime > (0.5- 0.003*level):
            blobs.append([random.randint(1,5), random.randrange(2,30), [0, random.randrange(25,150)], 0, 0,1])
            #color, gravity, pos, blobgravitytimer, blobset,blobhit
            
            lasttime = time.time()
        blob_counter = 0
        for blob in blobs:
            if blob[4] == 0:
                blob[4] = (2*(870-blob[2][1])/blob[1])**(1/2)
            blob[4] = (94/blob[4])
            blob[3]+= 1
            vely = blob[1]*blob[3]/40
            blob[2][1] += vely
            blob[2][0] += blob[4]/10
            screen.blit(blobdict[blob[0]], blob[2])
            if blob[2][1] == 0:
                blob[2] = random.randrange(2,30)
                blob[4] = (2*(random.randrange(700,850))/blob[1])**(1/2)
                blob[3] = 0
                if blob[5] == 3:
                    blob.pop(blob_counter)
            blob_counter += 1
            
        for event in pygame.event.get():
            
            
            if event.type == pygame.KEYDOWN:
                print paddlepos

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if paddlepos == 1:
                        paddlepos = 1
                    elif paddlepos == 2:
                        paddlepos = 1
                    elif paddlepos == 3:
                        paddlepos = 2
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if paddlepos == 1:
                        paddlepos = 2
                    elif paddlepos == 2:
                        paddlepos = 3
                    elif paddlepos == 3:
                        paddlepos = 3
                        
        pygame.display.flip()

                        



##
##
##
##def start_game():
##    
