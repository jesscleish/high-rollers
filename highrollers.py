from matplotlib.pyplot import draw
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
linen = (254, 245, 236)

# storing screen variable values
width = screen.get_width()
height = screen.get_height()

# Defining title font
titleFont = pygame.font.SysFont('rubikbold', 72)

# Defining button font
buttonFont = pygame.font.SysFont('rubik', 46)

# Defining win/loss font
statusFont = pygame.font.SysFont('rubikbold', 96)


# Draws text using parameters passed
def text_on_screen(msg, font, colour, surface, x, y):
    textobject = font.render(msg, True, colour)
    textrect = textobject.get_rect()
    textrect.midtop = (x,y)
    surface.blit(textobject, textrect)

def main_menu():
    pygame.display.set_caption("High Rollers")
    while True:

        # Fill screen with designated background colour
        screen.fill(backgroundC)
        text_on_screen('HIGH ROLLERS', titleFont, black, screen, (width/2), 100)

        mx, my = pygame.mouse.get_pos()

        playButton = pygame.Rect(width/7, (height/2), 200, 100)
        quitButton = pygame.Rect(((width/7)+200+width/7), (height/2), 200, 100)


        # Hover on buttons
        if playButton.collidepoint((mx, my)):
            # Rendering button darker green
            pygame.draw.rect(screen, dGreen, playButton)
            if click:
                gameTime()
        else:
            # Rendering button green
            pygame.draw.rect(screen, green, playButton)
        text_on_screen('play', buttonFont, linen, screen, (width/7)+100, (height/2)+25)

        if quitButton.collidepoint((mx,my)):
            # Rendering button darker red
            pygame.draw.rect(screen, dRed, quitButton)
            if click:
                pygame.quit()
        else:
            # Rendering button light red
            pygame.draw.rect(screen, red, quitButton)
        text_on_screen('quit', buttonFont, linen, screen, ((width/7)+300+width/7), (height/2)+25)

     
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
       

def gameTime():
    running = True
    while running:
        # Fill screen with designated background colour
        screen.fill(backgroundC)

        #render in mr catto and table here


        text_on_screen('LETS ROLL!', titleFont, yellow, screen, (width/2), 30)

        mx, my = pygame.mouse.get_pos()

        rollButton = pygame.Rect(width/3, (height-100), 225, 70)

        # Hover on roll button
        if rollButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, dRed, rollButton)
            if click:
                gameLogic()
        else:
            pygame.draw.rect(screen, red, rollButton)
        text_on_screen('ROLL', buttonFont, linen, screen, (width/3)+115, (height-90))

        click = False
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    running = False
            
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True
    
        pygame.display.update()
        mainClock.tick(60)

# generate rolls and navigate to appropriate screen accordingly
def gameLogic():

    running = True
    while running:
        # render rolly cat and table

        # show dust for rolling and make it wiggle if i can

        # maybe rolling dice sound?

        roll1 = (secrets.randbelow(5)+1) #computer roll
        roll2 = (secrets.randbelow(5)+1) #user roll

        # Dust on screen for 5 seconds
        CLEARDUST = USEREVENT + 1
        pygame.time.set_timer(CLEARDUST, 5000)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    running = False
            if ev.type == CLEARDUST:
                
                # Once dust can clear, navigate to next screen for victory/loss/draw
                if (roll1 > roll2):
                    loseScreen(roll1, roll2)
                    return 0

                elif(roll1 < roll2):
                    winScreen(roll1, roll2)
                    return 1

                elif(roll1 == roll2):
                    drawScreen(roll1)
                    return 2

                else:
                    pygame.quit() #fatal error
                    sys.exit()

        

    pygame.display.update()
    mainClock.tick(60)


def winScreen(compRoll, userRoll):
    running = True
    while running:
        screen.fill(backgroundC)

        #render in mr catto, dice and table here


        text_on_screen('WIN!', titleFont, green, screen, (width/2), 30)

        mx, my = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    running = False

            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True
    
        pygame.display.update()
        mainClock.tick(60)

def loseScreen(compRoll, userRoll):
    running = True
    while running:
        screen.fill(backgroundC)

        #render in mr catto, dice and table here


        text_on_screen('LOSE!', titleFont, red, screen, (width/2), 30)

        mx, my = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    running = False

            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True
    
    
        pygame.display.update()
        mainClock.tick(60)

def drawScreen(roll):
    running = True
    while running:
        screen.fill(backgroundC)

        #render in mr catto, dice, and table here


        text_on_screen('DRAW!', titleFont, red, screen, (width/2), 30)

        mx, my = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    running = False

            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True
    
        pygame.display.update()
        mainClock.tick(60)

main_menu()