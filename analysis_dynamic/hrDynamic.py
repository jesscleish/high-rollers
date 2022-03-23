from matplotlib.pyplot import draw
import pygame
import sys
import secrets
import time # Used for dynamic analysis
import datetime

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

# defining palette colours (global variables) as dictionary
gameColours={ 
    'background': (252, 222, 190), 
    'green': (101, 155, 94),
    'dG': (73, 113, 69),
    'red': (200, 70,48),
    'dR' : (135, 47, 31),
    'yellow': (255, 188, 66),
    'dY': (204, 145, 37),
    'black': (35, 32, 32),
    'brown':(90, 53, 42),
    'linen': (254, 245, 236)
}

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
# (message, font to use, colour to use, surface to draw on, and coordinates to place middle of text)
def text_on_screen(msg, font, colour, surface, x, y):
    f = open("dynamicLog.txt", "a")
    start = time.time()
    textobject = font.render(msg, True, colour) # Creates the text object out of the font
    textrect = textobject.get_rect() # creates a rectangle around the text object
    textrect.midtop = (x,y) # set coordinates of rectangle
    surface.blit(textobject, textrect) # display on surface indicated
    end = time.time()
    result = str(end-start)
    f.write("text_on_screen function: " + result + "s \n")


# Game main menu, with start and exit buttons
def main_menu():
    f = open("dynamicLog.txt", "w") # Creates dynamic log for OVERWRITE for current run
    f.truncate() #deletes contents of previous logs in case
    
    today = datetime.date.today()
    dateForm = today.strftime("%B %d, %Y") # Writes current date in written form
    nowdate = datetime.datetime.now()
    nowString = nowdate.strftime("%H:%M:%S")
    f.write("Dynamic Analysis began at: " + dateForm + ", " + nowString + "\n")
    f.close()

    # Starts timer
    f = open("dynamicLog.txt", "a") # opens dynamic log for APPEND
    start = time.time()  # take the start time measurement after document setup


    pygame.display.set_caption("High Rollers")

    letsplay = pygame.mixer.Sound("sounds/lpag.mp3")
    pygame.mixer.Sound.play(letsplay)

    click = False
    while True:
        
        # Fill screen with designated background colour
        screen.fill(gameColours['background'])
        text_on_screen('HIGH ROLLERS', titleFont, gameColours['black'], screen, (width/2), 100)

        # track position of mouse
        mx, my = pygame.mouse.get_pos()

        # Generate play/quit buttons
        playButton = pygame.Rect(width/7, (height/2), 200, 100)
        quitButton = pygame.Rect(((width/7)+200+width/7), (height/2), 200, 100)

        # Hover on buttons
        if playButton.collidepoint((mx, my)):
            # Rendering button darker green
            pygame.draw.rect(screen, gameColours['dG'], playButton)
            if click:
                end = time.time()
                result = str(end-start)
                f.write("Main menu: " + result + "s \n")
                f.close()
                gameTime(0)
        else:
            # Rendering button green
            pygame.draw.rect(screen, gameColours['green'], playButton)
        text_on_screen('play', buttonFont, gameColours['linen'], screen, (width/7)+100, (height/2)+25)

        if quitButton.collidepoint((mx,my)):
            # Rendering button darker red
            pygame.draw.rect(screen, gameColours['dR'], quitButton)
            if click:
                end = time.time()
                result = str(end-start)
                f.write("Main menu to QUIT: " + result + "s \n")
                f.close()
                pygame.quit()
        else:
            # Rendering button light red
            pygame.draw.rect(screen, gameColours['red'], quitButton)
        text_on_screen('quit', buttonFont, gameColours['linen'], screen, ((width/7)+300+width/7), (height/2)+25)


        # Loop to loog for pygame events to exit or move to next screen
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                end = time.time()
                result = str(end-start)
                f.write("Main menu on FORCE QUIT: " + result + "s \n")
                f.close()
                pygame.quit()
                sys.exit()
        
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


# Generates the rectangle (table) across the bottom of the screen
def tableGen():
    f = open("dynamicLog.txt", "a")
    start = time.time()
    table = pygame.Rect(0, height-250, width, 400)
    pygame.draw.rect(screen, gameColours['brown'], table)
    end = time.time()
    result = str(end-start)
    f.write("tableGen function: " + result + "s \n")
    f.close()
    


# get appropriate cat path to display in outcome screen
def getCatPath(state):
    f = open("dynamicLog.txt", "a")
    start = time.time()

    if state == 0:
        catPath = "assets/wincat.png"
    elif state == 1:
        catPath = "assets/losecat.png"
    elif state == 2:
        catPath = "assets/draw.png"
    
    end = time.time()
    result = str(end-start)
    f.write("catPath function: " + result + "s \n")
    f.close()
    return catPath


# Updates score based on win/lose/draw
def updateScore(score, status):
    f = open("dynamicLog.txt", "a")
    start = time.time()
    if status == 0:
        score = (score-1)
    elif status == 1:
        score = (score+1)

    end = time.time()
    result = str(end-start)
    f.write("updateScore function: " + result + "s \n")
    f.close()
    return score


# Displays the score on the screen
def displayScore(score):
    f = open("dynamicLog.txt", "a")
    start = time.time()

    score = str(score)
    text_on_screen('Score:', scoreFont, gameColours['dY'], screen, (width-90), 30)
    text_on_screen(score, scoreFont, gameColours['dY'], screen, (width-25), 30)

    end = time.time()
    result = str(end-start)
    f.write("displayScore function: " + result + "s \n")
    f.close()


# Begins the "lets roll" screen of game, with button to start
def gameTime(score):
    f = open("dynamicLog.txt", "a")
    start = time.time()

    score = score
    click = False


    running = True
    while running:
        # Fill screen with designated background colour
        screen.fill(gameColours['background'])

        # Render before-roll cat, and table
        pregame = pygame.image.load("assets/preroll.png").convert_alpha()
        pregame = pygame.transform.scale(pregame, (400, 450))
        screen.blit(pregame, ((width/4),(height/2)-325))
        tableGen()
        pygame.display.flip() #update screen

        text_on_screen('LETS ROLL!', titleFont, gameColours['yellow'], screen, (width/2), 30)
        displayScore(score)

        # mouse position
        mx, my = pygame.mouse.get_pos()

        rollButton = pygame.Rect(width/3, (height-100), 225, 70)

        # Hover on roll button
        if rollButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, gameColours['dR'], rollButton)
            if click:
                end = time.time()
                result = str(end-start)
                f.write("gameTime function: " + result + "s \n")
                f.close()
                gameLogic(score)
        else:
            pygame.draw.rect(screen, gameColours['red'], rollButton)
        
        text_on_screen('ROLL', buttonFont, gameColours['linen'], screen, (width/3)+115, (height-90))

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                end = time.time()
                result = str(end-start)
                f.write("gameTime function on FORCE QUIT: " + result + "s \n")
                f.close()
                pygame.quit()
                sys.exit()
            
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True
    
        pygame.display.update()
        mainClock.tick(60)


# checks winner based on dice inputs
def checkWinner(roll1, roll2):
    f = open("dynamicLog.txt", "a")
    start = time.time()

    if (roll1 > roll2): # Computer wins
        end = time.time()
        result = str(end-start)
        f.write("checkWinner function, Computer Win: " + result + "s \n")
        f.close()
        return 0

    elif(roll1 < roll2):   # User wins
        end = time.time()
        result = str(end-start)
        f.write("checkWinner function, User Win: " + result + "s \n")
        f.close()
        return 1

    elif(roll1 == roll2): # Draw
        end = time.time()
        result = str(end-start)
        f.write("checkWinner function, Draw: " + result + "s \n")
        f.close()
        return 2



# Obtains image path for computer and user rolled dice
def getDice(die1, die2):
    f = open("dynamicLog.txt", "a")
    start = time.time()

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

    end = time.time()
    result = str(end-start)
    f.write("getDice function: " + result + "s \n")
    f.close()
    return (compRoll, userRoll)

# Displays dice based on img path
def showDice(compRoll, userRoll):
    f = open("dynamicLog.txt", "a")
    start = time.time()

    # resize dice
    userRollR = pygame.transform.scale((pygame.image.load(userRoll).convert_alpha()), (80, 80))
    compRollR = pygame.transform.scale((pygame.image.load(compRoll).convert_alpha()), (80, 80))

    # display user and computer dice
    screen.blit(userRollR, ((width/2)+45, (height/2)+200))
    screen.blit(compRollR, ((width/4)+105, (height/2)+150))
    pygame.display.update()
    
    end = time.time()
    result = str(end-start)
    f.write("showDice function: " + result + "s \n")
    f.close()


# generate rolls, next screen navigation
def gameLogic(score):
    f = open("dynamicLog.txt", "a")
    start = time.time()

    score = score
    running = True
    die1 = (secrets.randbelow(5)+1) #computer roll
    die2 = (secrets.randbelow(5)+1) #user roll

    # Create event for after 2 seconds to move to win/loss/draw screen
    dust_clear_event = pygame.USEREVENT + 1
    pygame.time.set_timer(dust_clear_event, 2000)
    
    # sound effect for rolling dice
    diceroll = pygame.mixer.Sound("sounds/diceroll.wav")
    pygame.mixer.Sound.play(diceroll)

    while running:
        # Fill screen with designated background colour
        screen.fill(gameColours['background'])


        # render cat rolling die, and table
        rollcat = pygame.image.load("assets/rollcat.png").convert_alpha()
        rollcat = pygame.transform.scale(rollcat, (400, 450))
        screen.blit(rollcat, ((width/4),(height/2)-325))
        tableGen()
        
        displayScore(score)

        # show dust for rolling
        dust = pygame.image.load("assets/dust.png").convert_alpha()
        dust = pygame.transform.scale(dust, (300, 300))
        screen.blit(dust, ((width/4)+5, (height/2)+50))

        pygame.display.flip() # update display

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                end = time.time()
                result = str(end-start)
                f.write("gameLogic function on FORCE QUIT: " + result + "s \n")
                f.close()
                pygame.quit()
                sys.exit()
            
            if ev.type == dust_clear_event:
                # Once dust can clear, navigate to next screen for victory/loss/draw
                winner = checkWinner(die1, die2)
                score = updateScore(score, winner)
                if winner == 0:
                    end = time.time()
                    result = str(end-start)
                    f.write("gameLogic function if Computer Win: " + result + "s \n")
                    f.close()
                    loseScreen(die1, die2, winner, score)
                elif winner == 1:
                    end = time.time()
                    result = str(end-start)
                    f.write("gameLogic function if User Win: " + result + "s \n")
                    f.close()
                    winScreen(die1, die2, winner, score)
                else:
                    end = time.time()
                    f.write("gameLogic function if Draw: " + result + "s \n")
                    f.close()
                    drawScreen(die1, winner, score)

    pygame.display.update()
    mainClock.tick(60)


# user won
def winScreen(die1, die2, num, score):
    f = open("dynamicLog.txt", "a")
    start = time.time()

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
        screen.fill(gameColours['background'])

        # get path to cat image based on win/lose/draw state passed
        catPath = getCatPath(state)
        cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
        #display cat
        screen.blit(cat, ((width/4),(height/2)-325))
        
        #display table and dice
        tableGen()
        cRoll, uRoll = getDice(computer, user) # get dice img paths
        showDice(cRoll, uRoll)

        displayScore(score)

        text_on_screen('WIN! :)', statusFont, gameColours['green'], screen, (width/2), 30)
        
        # mouse coordinates
        mx, my = pygame.mouse.get_pos()

        againButton = pygame.Rect(width/7, (height-70), 225, 50)
        quitButton = pygame.Rect(width/7+300, (height-70), 225, 50)
        pygame.draw.rect(screen, gameColours['green'], againButton)
        pygame.draw.rect(screen, gameColours['red'], quitButton)


        # hover effects (collision)
        if againButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, gameColours['dG'], againButton)
            if click:
                end = time.time()
                result = str(end-start)
                f.write("winScreen function on PLAY AGAIN: " + result + "s \n")
                f.close()
                gameTime(score)
        else:
            pygame.draw.rect(screen, gameColours['green'], againButton)
        text_on_screen('replay', buttonFont, gameColours['linen'], screen, (width/7)+115, (height-75))

        if quitButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, gameColours['dR'], quitButton)
            if click:
                end = time.time()
                result = str(end-start)
                f.write("winScreen function on EXIT: " + result + "s \n")
                f.close()
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, gameColours['red'], quitButton)
        text_on_screen('quit', buttonFont, gameColours['linen'], screen, (width/7)+415, (height-75))

        # event loop looking for click or escape
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                end = time.time()
                result = str(end-start)
                f.write("winScreen function on FORCE QUIT: " + result + "s \n")
                f.close()
                pygame.quit()
                sys.exit()

            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True
    
        pygame.display.update()
        mainClock.tick(60)


# screen for when user loses
def loseScreen(die1, die2, num, score):
    f = open("dynamicLog.txt", "a")
    start = time.time()

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
        screen.fill(gameColours['background'])

        againButton = pygame.Rect(width/7, (height-70), 225, 50)
        quitButton = pygame.Rect(width/7+300, (height-70), 225, 50)

        # get path to cat image based on win/lose/draw state passed
        catPath = getCatPath(state)
        cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
        #display cat
        screen.blit(cat, ((width/4),(height/2)-325))

        # display table and dice
        tableGen()
        cRoll, uRoll = getDice(computer, user)
        showDice(cRoll, uRoll)

        displayScore(score)

        text_on_screen('LOSE! :(', statusFont, gameColours['red'], screen, (width/2), 30)

        # mouse coordinates
        mx, my = pygame.mouse.get_pos()

        # hover collision
        if againButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, gameColours['dG'], againButton)
            if click:
                end = time.time()
                result = str(end-start)
                f.write("loseScreen function on PLAY AGAIN: " + result + "s \n")
                f.close()
                gameTime(score)
        else:
            pygame.draw.rect(screen, gameColours['green'], againButton)
        text_on_screen('replay', buttonFont, gameColours['linen'], screen, (width/7)+115, (height-75))

        if quitButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, gameColours['dR'], quitButton)
            if click:
                end = time.time()
                result = str(end-start)
                f.write("loseScreen function on EXIT: " + result + "s \n")
                f.close()
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, gameColours['red'], quitButton)
        text_on_screen('quit', buttonFont, gameColours['linen'], screen, (width/7)+415, (height-75))

        # event loop looking for click or escape
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                end = time.time()
                result = str(end-start)
                f.write("loseScreen function on FORCE QUIT: " + result + "s \n")
                f.close()
                pygame.quit()
                sys.exit()

            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True
    
    
        pygame.display.update()
        mainClock.tick(60)


# screen for when computer and user dice are equal
def drawScreen(die1, num, score):
    f = open("dynamicLog.txt", "a")
    start = time.time()

    click = False
    roll = die1
    state = num
    score = score
    
    # play "draw" sound effect
    drawsound = pygame.mixer.Sound("sounds/angrycat.mp3")
    pygame.mixer.Sound.play(drawsound)

    running = True
    while running:
        screen.fill(gameColours['background'])

        againButton = pygame.Rect(width/7, (height-70), 225, 50)
        quitButton = pygame.Rect(width/7+300, (height-70), 225, 50)

        # get appropriate cat based on game status (win/loss/draw)
        catPath = getCatPath(state)
        cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
        # Display cat on screeen
        screen.blit(cat, ((width/4),(height/2)-325))

        #render in table
        tableGen()

        cRoll, uRoll = getDice(roll, roll)
        showDice(cRoll, uRoll)

        displayScore(score)

        text_on_screen('DRAW!', statusFont, gameColours['yellow'], screen, (width/2), 30)
        mx, my = pygame.mouse.get_pos()

        if againButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, gameColours['dG'], againButton)
            if click:
                end = time.time()
                result = str(end-start)
                f.write("drawScreen function on PLAY AGAIN: " + result + "s \n")
                f.close()
                gameTime(score)
        else:
            pygame.draw.rect(screen, gameColours['green'], againButton)
        text_on_screen('replay', buttonFont, gameColours['linen'], screen, (width/7)+115, (height-75))

        if quitButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, gameColours['dR'], quitButton)
            if click:
                end = time.time()
                result = str(end-start)
                f.write("drawScreen function on EXIT: " + result + "s \n")
                f.close()
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, gameColours['red'], quitButton)
        text_on_screen('quit', buttonFont, gameColours['linen'], screen, (width/7)+415, (height-75))


        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                end = time.time()
                result = str(end-start)
                f.write("drawScreen function on FORCE QUIT: " + result + "s \n")
                f.close()
                pygame.quit()
                sys.exit()


            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True
    
        pygame.display.update()
        mainClock.tick(60)
