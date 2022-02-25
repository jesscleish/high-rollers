from matplotlib.pyplot import draw
import pygame
import sys
import secrets

# Setup pygame window
mainClock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.font.init()
pygame.mixer.init()

# set screen resolution
resolution = (725,725)

# open a screen of above resolution
screen = pygame.display.set_mode(resolution)

# defining palette colours(global variables)
backgroundC = (252, 222, 190)
green = (101, 155, 94)
dGreen = (73, 113, 69)
red = (200, 70,48)
dRed = (135, 47, 31)
yellow = (255, 188, 66)
black = (35, 32, 32)
brown = (90, 53, 42)
linen = (254, 245, 236)
scoreYellow = (204, 145, 37)

# storing screen variable values
width = screen.get_width()
height = screen.get_height()

# Defining title font
titleFont = pygame.font.SysFont('rubikbold', 72)

# Defining button font
buttonFont = pygame.font.SysFont('rubik', 46)

# Defining score font
scoreFont = pygame.font.SysFont('rubik', 24)

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

    letsplay = pygame.mixer.Sound("sounds/lpag.mp3")
    pygame.mixer.Sound.play(letsplay)

    click = False
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
                gameTime(0)
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
    table = pygame.Rect(0, height-250, width, 400)
    pygame.draw.rect(screen, brown, table)


# get appropriate cat path to display in outcome screen
def getCatPath(state):
    if state == 0:
        catPath = "assets/wincat.png"
    elif state == 1:
        catPath = "assets/losecat.png"
    elif state == 2:
        catPath = "assets/draw.png"
    return catPath

def updateScore(score, status):
    if status == 0:
        score = (score-1)
    elif status == 1:
        score = (score+1)

    return score

def displayScore(score):
    score = str(score)
    text_on_screen('Score:', scoreFont, scoreYellow, screen, (width-90), 30)
    text_on_screen(score, scoreFont, scoreYellow, screen, (width-25), 30)


def gameTime(score):
    score = score
    click = False
    running = True
    while running:
        # Fill screen with designated background colour
        screen.fill(backgroundC)

        #render in mr catto and table here
        pregame = pygame.image.load("assets/preroll.png").convert_alpha()
        pregame = pygame.transform.scale(pregame, (400, 450))
        screen.blit(pregame, ((width/4),(height/2)-325))
        tableGen()
        pygame.display.flip()

        text_on_screen('LETS ROLL!', titleFont, yellow, screen, (width/2), 30)
        displayScore(score)

        mx, my = pygame.mouse.get_pos()

        rollButton = pygame.Rect(width/3, (height-100), 225, 70)

        # Hover on roll button
        if rollButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, dRed, rollButton)
            if click:
                gameLogic(score)
        else:
            pygame.draw.rect(screen, red, rollButton)
        
        text_on_screen('ROLL', buttonFont, linen, screen, (width/3)+115, (height-90))

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

    elif(roll1 < roll2):   # User wins
        return 1

    elif(roll1 == roll2): # Draw
        return 2


def getDice(die1, die2):
    if die1 == 1:
        compRoll = "assets/b1.png"
    elif die1 == 2:
        compRoll = "assets/b2.png"
    elif die1 == 3:
        compRoll = "assets/b3.png"
    elif die1 == 4:
        compRoll = "assets/b4.png"
    elif die1 == 5:
        compRoll = "assets/b5.png"
    elif die1 == 6:
        compRoll = "assets/b6.png"

                
    if die2 == 1:
        userRoll = "assets/r1.png"
    elif die2 == 2:
        userRoll = "assets/r2.png"
    elif die2 == 3:
        userRoll = "assets/r3.png"
    elif die2 == 4:
        userRoll = "assets/r4.png"
    elif die2 == 5:
        userRoll = "assets/r5.png"
    elif die2 == 6:
        userRoll = "assets/r6.png"

    return (compRoll, userRoll)

def showDice(compRoll, userRoll):
    # resize dice
    userRollR = pygame.transform.scale((pygame.image.load(userRoll).convert_alpha()), (80, 80))
    compRollR = pygame.transform.scale((pygame.image.load(compRoll).convert_alpha()), (80, 80))

    # display user and computer dice
    screen.blit(userRollR, ((width/2)+45, (height/2)+200))
    screen.blit(compRollR, ((width/4)+105, (height/2)+150))
    pygame.display.update()



# generate rolls, next screen navigation
def gameLogic(score):
    score = score
    running = True
    die1 = (secrets.randbelow(5)+1) #computer roll
    die2 = (secrets.randbelow(5)+1) #user roll

    dust_clear_event = pygame.USEREVENT + 1
    pygame.time.set_timer(dust_clear_event, 2000)
    
    # sound effect for rolling dice
    diceroll = pygame.mixer.Sound("sounds/diceroll.wav")
    pygame.mixer.Sound.play(diceroll)

    while running:
        # Fill screen with designated background colour
        screen.fill(backgroundC)


        # render rolly cat and table
        rollcat = pygame.image.load("assets/rollcat.png").convert_alpha()
        rollcat = pygame.transform.scale(rollcat, (400, 450))
        screen.blit(rollcat, ((width/4),(height/2)-325))
        tableGen()
        
        displayScore(score)

        # show dust for rolling and make it wiggle if i can
        dust = pygame.image.load("assets/dust.png").convert_alpha()
        dust = pygame.transform.scale(dust, (300, 300))
        screen.blit(dust, ((width/4)+5, (height/2)+50))

        pygame.display.flip()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    running = False
            if ev.type == dust_clear_event:
                # Once dust can clear, navigate to next screen for victory/loss/draw
                winner = checkWinner(die1, die2)
                score = updateScore(score, winner)
                if winner == 0:
                    loseScreen(die1, die2, winner, score)
                elif winner == 1:
                    winScreen(die1, die2, winner, score)
                else:
                    drawScreen(die1, winner, score)

    pygame.display.update()
    mainClock.tick(60)


def winScreen(die1, die2, num, score):
    score = score
    computer = die1
    user = die2
    state = num
    click = False

    # sound effect for win
    winsound = pygame.mixer.Sound("sounds/trumpetwin.mp3")
    pygame.mixer.Sound.play(winsound)


    running = True
    while running:
        screen.fill(backgroundC)

        catPath = getCatPath(state)
        cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
        #display cat
        screen.blit(cat, ((width/4),(height/2)-325))
        
        #display table and dice
        tableGen()
        cRoll, uRoll = getDice(computer, user)
        showDice(cRoll, uRoll)

        displayScore(score)

        text_on_screen('WIN! :)', statusFont, green, screen, (width/2), 30)
        
        mx, my = pygame.mouse.get_pos()

        againButton = pygame.Rect(width/7, (height-70), 225, 50)
        quitButton = pygame.Rect(width/7+300, (height-70), 225, 50)
        pygame.draw.rect(screen, green, againButton)
        pygame.draw.rect(screen, red, quitButton)

        
        if againButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, dGreen, againButton)
            if click:
                gameTime(score)
        else:
            pygame.draw.rect(screen, green, againButton)
        text_on_screen('replay', buttonFont, linen, screen, (width/7)+115, (height-75))

        if quitButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, dRed, quitButton)
            if click:
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, red, quitButton)
        text_on_screen('quit', buttonFont, linen, screen, (width/7)+415, (height-75))

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


def loseScreen(die1, die2, num, score):
    score = score
    click = False
    computer = die1
    user = die2
    state = num

    # sound effect for lose
    losesound = pygame.mixer.Sound("sounds/losetrombone.wav")
    pygame.mixer.Sound.play(losesound)

    running = True
    while running:
        screen.fill(backgroundC)

        againButton = pygame.Rect(width/7, (height-70), 225, 50)
        quitButton = pygame.Rect(width/7+300, (height-70), 225, 50)

        catPath = getCatPath(state)
        cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
        #display cat
        screen.blit(cat, ((width/4),(height/2)-325))

        # display table and dice
        tableGen()
        cRoll, uRoll = getDice(computer, user)
        showDice(cRoll, uRoll)

        displayScore(score)

        text_on_screen('LOSE! :(', statusFont, red, screen, (width/2), 30)

        mx, my = pygame.mouse.get_pos()

        if againButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, dGreen, againButton)
            if click:
                gameTime(score)
        else:
            pygame.draw.rect(screen, green, againButton)
        text_on_screen('replay', buttonFont, linen, screen, (width/7)+115, (height-75))

        if quitButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, dRed, quitButton)
            if click:
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, red, quitButton)
        text_on_screen('quit', buttonFont, linen, screen, (width/7)+415, (height-75))

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

def drawScreen(die1, num, score):
    click = False
    roll = die1
    state = num
    score = score
    

    drawsound = pygame.mixer.Sound("sounds/angrycat.mp3")
    pygame.mixer.Sound.play(drawsound)
    running = True
    while running:
        screen.fill(backgroundC)

        againButton = pygame.Rect(width/7, (height-70), 225, 50)
        quitButton = pygame.Rect(width/7+300, (height-70), 225, 50)

        #render in mr catto, dice, and table here
        catPath = getCatPath(state)
        cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
        screen.blit(cat, ((width/4),(height/2)-325))

        #render in table
        tableGen()

        cRoll, uRoll = getDice(roll, roll)
        showDice(cRoll, uRoll)

        displayScore(score)

        text_on_screen('DRAW!', statusFont, red, screen, (width/2), 30)
        mx, my = pygame.mouse.get_pos()

        if againButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, dGreen, againButton)
            if click:
                gameTime(score)
        else:
            pygame.draw.rect(screen, green, againButton)
        text_on_screen('replay', buttonFont, linen, screen, (width/7)+115, (height-75))

        if quitButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, dRed, quitButton)
            if click:
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, red, quitButton)
        text_on_screen('quit', buttonFont, linen, screen, (width/7)+415, (height-75))

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
