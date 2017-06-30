
from __future__ import division
from __main__ import *
from pel_ai import start_ai
import pygame
import time
import random
import math

pygame.init()
pygame.font.init()
global w,h, game_running
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
game_running = 1
font = pygame.font.Font(None, 30)
global white
white =(255,255,255)

def game_over(blobs):
    game_done = 1
    font = pygame.font.Font(None, 30)
    text = font.render('Press Enter to Restart Game.', True, white)
    blobs = []
    while game_done:
        screen.blit(text, (150, 400))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_done = 0
        
def restart_game(game_running):
    game_running = 1

def start_ai(lives, blobs, paddlepos, xd):
    if lives > 0:
        if score < xd:
            for blob in blobs:
                 if 830< blob[2][1] and 851 > blob[2][1]:
                      print 'we are changing to:' +str(paddlepos)
                      paddlepos= blob[5]
        


while 1:
    blobs = []  # blobs have attribute (type-> color), (gravity), 
    lasttime = time.time()
    counter = 0
    level = 1
    paddlepos = 1
    score = 0
    lives = 3
    streak = 0
    xd = input('Want an AI to play for you?: ')
    if xd == 'y':
        print 'This AI is in god mode!'
        endscore = input('What score should the AI stop at?: ')
    while game_running:
        if xd == 'y':
            start_ai(lives, blobs, paddlepos, xd)
        screen.fill(black)
        screen.blit(paddle, (188*paddlepos-170,870))
        text1 = font.render('Score:'+ ' ' +str(score), True, white)
        text2 = font.render('Streak:'+ ' '+str(streak), True, white)
        text3 = font.render('Multiplier:'+ ' '+str(streak)+'X', True, white)
        text4 = font.render('Lives:'+ ' '+str(lives), True, white)
        screen.blit(text1, (0,0))
        screen.blit(text2, (500,0))
        screen.blit(text3, (230,0))
        screen.blit(text4, (255,30))
        counter+= 1
        Clock = pygame.time.Clock()
        Clock.tick(40)
            
        if lives <= 0:
            game_over(blobs)
        if time.time()- lasttime > (5-0.001*counter):
            blobs.append([random.randint(1,5), random.randrange(5,6), [0, random.randrange(25,150)], 0, 0,1])
            #color, gravity, pos, blobgravitytimer, blobsettime,blobhit
            #0       1        2   3                 4           5
            lasttime = time.time()
        blob_counter = 0
        n = math.floor(len(blobs)/10)
        multiplier = int(2**(n))
        for blob in blobs:
        
            if blob[5] == 1:
                if blob[4] == 0:
                        blob[4] = (2*(870-blob[2][1])/blob[1])**(1/2)
                blob[4] = (94/blob[4])
                blob[3]+= 1
                vely = blob[1]*blob[3]/40
                blob[2][1] += vely
                blob[2][0] += blob[4]/11
                screen.blit(blobdict[blob[0]], blob[2])
                if blob[2][1] >= 858:
                    if paddlepos == 1:
                        bounce_velocity = random.randrange(-12,-10)
                        blob[4] = (2*(random.randrange(700,850))/blob[1])**(1/2)
                        blob[3] = 0
                        blob[5] = 2
                        blob[2][1] = 857
                        streak += 1
                        score += multiplier
                    else:
                        lives -= 1
                        streak = 0
                        print 'a'
                        
                        
            if blob[5] == 2:
                blob[3] += 1
                vely = (bounce_velocity +blob[1]*blob[3]/40)
                t= 2*(bounce_velocity/blob[1])
                velx = 2*94/blob[4]
                blob[2][1] += vely
                blob[2][0] += velx/10
                screen.blit(blobdict[blob[0]], blob[2])
                if blob[2][1] >= 858: 
                    if paddlepos == 2:
                        bounce_velocity = random.randrange(-30,-20)
                        blob[4] = (2*(random.randrange(700,850))/blob[1])**(1/2)
                        blob[3] = 0
                        blob[5] = 3
                        blob[2][1] = 857
                        streak += 1
                        score += multiplier
                    else:
                        lives -= 1
                        streak = 0
                        print 'b'
                        print paddlepos
                        
            if blob[5] == 3:
                blob[3] += 1
                vely = (bounce_velocity +blob[1]*blob[3]/40)
                t= 2*(bounce_velocity/blob[1])
                velx = 2*94/blob[4]
                blob[2][1] += vely
                blob[2][0] += velx/11
                screen.blit(blobdict[blob[0]], blob[2])
                if blob[2][1] >= 858: 
                    if paddlepos == 3:
                        
                        bounce_velocity = random.randrange(-30,-20)
                        blob[4] = (2*(random.randrange(700,850))/blob[1])**(1/2)
                        blob[3] = 0
                        blob[5] = 4
                        blob[2][1] = 857
                        streak += 1
                        score += multipler
                    else:
                        lives -= 1
                        streak = 0
                        
            if blob[5] == 4:
                blob[3] += 1
                vely = (bounce_velocity +blob[1]*blob[3]/40)
                t= 2*(bounce_velocity/blob[1])
                velx = 2*94/blob[4]
                blob[2][1] += vely
                blob[2][0] += velx/9
                screen.blit(blobdict[blob[0]], blob[2])
                if blob[2][0] >= 550:
                    blobs.pop(blob_counter)
                    
            blob_counter += 1
            
        for event in pygame.event.get():
            
            
            if event.type == pygame.KEYDOWN:
        

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if paddlepos == 1:
                        paddlepos = 3
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
                        paddlepos = 1
                        
        pygame.display.flip()

    restart_game(game_running)                        



##
##
##
##def start_game():
##    
