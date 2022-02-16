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

# importing assets
beforecat = pygame.image.load("assets/preroll.png")
rollcat = pygame.image.load("assets/rollcat.png")




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
       
# Generates the rectangle across the bottom of the screen
def tableGen():
    table = pygame.Rect(0, height-300, width, 400)
    pygame.draw.rect(screen, brown, table)


def gameTime():
    running = True
    while running:
        # Fill screen with designated background colour
        screen.fill(backgroundC)

        #render in mr catto and table here
        pregame = pygame.image.load("assets/preroll.png").convert_alpha()
        screen.blit(pregame , (25, 30))
        tableGen()
        pygame.display.flip()

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


def checkWinner(roll1, roll2):
    if (roll1 > roll2): # Computer wins
        return 0

    elif(roll1 < roll2):    # User wins
        return 1

    elif(roll1 == roll2): #Draw
        return 2

    else:
        pygame.quit() #fatal error
        sys.exit()


def displayDice(die1, die2):
    if die1 == 1:
        compRoll = pygame.image.load("assets/b1.png").convert_alpha()
    elif die1 == 2:
        compRoll = pygame.image.load("assets/b2.png").convert_alpha()
    elif die1 == 3:
        compRoll = pygame.image.load("assets/b3.png").convert_alpha()
    elif die1 == 4:
        compRoll = pygame.image.load("assets/b4.png").convert_alpha()
    elif die1 == 5:
        compRoll = pygame.image.load("assets/b5.png").convert_alpha()
    elif die1 == 6:
        compRoll = pygame.image.load("assets/b6.png").convert_alpha()

                
    if die2 == 1:
        userRoll = pygame.image.load("assets/r1.png").convert_alpha()
    elif die2 == 2:
        userRoll = pygame.image.load("assets/r2.png").convert_alpha()
    elif die2 == 3:
        userRoll = pygame.image.load("assets/r3.png").convert_alpha()
    elif die2 == 4:
        userRoll = pygame.image.load("assets/r4.png").convert_alpha()  
    elif die2 == 5:
        userRoll = pygame.image.load("assets/r5.png").convert_alpha()
    elif die2 == 6:
        userRoll = pygame.image.load("assets/r6.png").convert_alpha()
    
    # display user and computer dice
    screen.blit(compRoll, ((width/5)+8, (height/2)-60))
    screen.blit(userRoll, ((width/4)+95, (height/2)-10))
    pygame.display.flip()


# generate rolls, next screen navigation
def gameLogic():

    running = True
    die1 = (secrets.randbelow(5)+1) #computer roll
    die2 = (secrets.randbelow(5)+1) #user roll

    while running:
        # render rolly cat and table
        rollcat = pygame.image.load("assets/rollcat.png").convert_alpha()
        screen.blit(rollcat , ((width/2), (height/2)))
        tableGen()

        # show dust for rolling and make it wiggle if i can
        dust = pygame.image.load("assets/dust.png").convert_alpha()
        screen.blit(dust, ((width/2), (height/2)))

        # maybe rolling dice sound?
        pygame.display.flip()
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
                winner = checkWinner(die1, die2)

                if winner == 0:
                    loseScreen(die1, die2)
                elif winner == 1:
                    winScreen(die1, die2)
                else:
                    drawScreen(die1)

    pygame.display.update()
    mainClock.tick(60)


def winScreen(die1, die2):
    computer = die1
    user = die2

    running = True
    while running:
        screen.fill(backgroundC)


        wincat = pygame.image.load("assets/wincat.png").convert_alpha()
        #display cat
        screen.blit(wincat, width/2, (height/2))
        
        #display table
        tableGen()

        displayDice(computer, user)
        pygame.display.flip()
        pygame.time.wait(2000)

        text_on_screen('WIN! :)', titleFont, green, screen, (width/2), 30)

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

def loseScreen(die1, die2):
    computer = die1
    user = die2

    running = True
    while running:
        screen.fill(backgroundC)

        
        losecat = pygame.image.load("assets/losecat.png").convert_alpha()
        #display cat
        screen.blit(losecat, width/2, (height/2))

        # display table
        tableGen()

        displayDice(computer, user)
        pygame.display.flip()
        pygame.time.wait(2000)
        text_on_screen('LOSE! :(', titleFont, red, screen, (width/2), 30)

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

def drawScreen(die1):
    roll = die1

    running = True
    while running:
        screen.fill(backgroundC)

        #render in mr catto, dice, and table here
        drawcat = pygame.image.load("assets/draw.png").convert_alpha()
        screen.blit(drawcat, width/2, (height/2))

        #render in table
        tableGen()

        displayDice(roll, roll)

        pygame.display.flip()
        pygame.time.wait(2000)
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