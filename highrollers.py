import pygame
import sys
import secrets

# Setup pygame window
mainClock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

# set screen resolution
resolution = (725,725)

# open a screen of above resolution
screen = pygame.display.set_mode(resolution)


# defining palette colours
backgroundC = (252, 222, 190)
green = (101, 155, 94)
dGreen = (73, 113, 69)
red = (200, 70,48)
dRed = (135, 47, 31)
yellow = (255, 188, 66)
black = (35, 32, 32)
brown = (90, 53, 42)
indigo = (28, 31, 51)

# storing screen variable values
width = screen.get_width()
height = screen.get_height()

# Defining title font
titleFont = pygame.font.SysFont('',)

# Defining button font
buttonFont = pygame.font.SysFont('',)

# Defining win/loss font
statusFont = pygame.font.SysFont('',)

# Render title font
#titleText = titleFont.render('HIGH ROLLERS', True, indigo)

# Render nav button font
#playBtn = buttonFont.render('PLAY', True, black)
#quitBtn = buttonFont.render('QUIT', True, black)

# Draws text using parameters passed
def text_on_screen(msg, font, colour, surface, x, y):
    textobject = font.render(msg, True, colour)
    textrect = textobject.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobject, textrect)

def main_menu():
    while True:

        # Fill screen with designated background colour
        screen.fill(backgroundC)
        text_on_screen('HIGH ROLLERS', titleFont, indigo, screen, (width/2), 30)

        mx, my = pygame.mouse.get_pos()

        playButton = pygame.Rect(width/2, (height/2)-150, 200, 100)
        quitButton = pygame.Rect(width/2, (height/2)+150, 200, 100)

        # Hover on buttons
        if playButton.collidepoint((mx, my)):
            # Rendering button darker green
            pygame.draw.rect(screen, dGreen, playButton)
            if click:
                gameTime()
        else:
            # Rendering button green
            pygame.draw.rect(screen, green, playButton)

        if quitButton.collidepoint((mx,my)):
            # Rendering button darker red
            pygame.draw.rect(screen, dRed, quitButton)
            if click:
                pygame.quit()
        else:
            # Rendering button light red
            pygame.draw.rect(screen, red, quitButton)

     
        click = False
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
       

        # superimpose play text onto play button
        #screen.blit(playBtn, )

        # superimpose quit text onto quit button
        #screen.blit(quitBtn, )

# get random number
roll1 = (secrets.randbelow(5)+1)
roll2 = (secrets.randbelow(5)+1)

def gameTime():
    running = True
    while running:
        # Fill screen with designated background colour
        screen.fill(backgroundC)
        text_on_screen('LETS ROLL!', titleFont, yellow, screen, (width/2), 30)

        mx, my = pygame.mouse.get_pos()

        rollButton = pygame.Rect(width/2, (height-30), 200, 100)

        # Hover on roll button
        if rollButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, dRed, rollButton)
        else:
            pygame.draw.rect(screen, red, rollButton)


        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    running = False
    
        pygame.display.update()
        mainClock.tick(60)

def winScreen():
    running = True
    while running:
        screen.fill(backgroundC)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    running = False
    
        pygame.display.update()
        mainClock.tick(60)

def loseScreen():
    running = True
    while running:
        screen.fill(backgroundC)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    running = False
    
        pygame.display.update()
        mainClock.tick(60)

def drawScreen():
    running = True
    while running:
        screen.fill(backgroundC)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    running = False
    
        pygame.display.update()
        mainClock.tick(60)
