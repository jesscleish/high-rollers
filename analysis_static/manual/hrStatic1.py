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

# defining palette colours (global variables) as dictionary
gameColours={ 
    'green': (101, 155, 94),
    'dG': (73, 113, 69),
    'red': (200, 70,48),
    'dR' : (135, 47, 31),
    'dY': (204, 145, 37)
}

# storing screen variable values REQUIRED FOR DISPLAY
width = screen.get_width()
height = screen.get_height()

# Defining score font
scoreFont = pygame.font.SysFont('rubik', 24)


# Draws text using parameters passed 
# (message, font to use, colour to use, surface to draw on, and coordinates to place middle of text)
def text_on_screen(msg, font, colour, surface, x, y):
    textobject = font.render(msg, True, colour) # Creates the text object out of the font
    textrect = textobject.get_rect() # creates a rectangle around the text object
    textrect.midtop = (x,y) # set coordinates of rectangle
    surface.blit(textobject, textrect) # display on surface indicated

# main_menu not affected by score variable

# tableGen not affected by score variable

# getCatPath function not affected by score variable


# Updates score based on win/lose/draw
def updateScore(score, status):
    if status == 0:
        score = (score-1)
    elif status == 1:
        score = (score+1)

    return score


# Displays the score on the screen
def displayScore(score):
    score = str(score)
    text_on_screen(score, scoreFont, gameColours['dY'], screen, (width-25), 30)


# Begins the "lets roll" screen of game, with button to start
def gameTime(score):
    score = score
    
    displayScore(score)
    gameLogic(score)


# checks winner based on dice inputs
def checkWinner(roll1, roll2):
    if (roll1 > roll2): # Computer wins
        return 0

    elif(roll1 < roll2):   # User wins
        return 1

    elif(roll1 == roll2): # Draw
        return 2


# getDice function not affected by score variable

# showDice function not affected by score variable

# generate rolls, next screen navigation
def gameLogic(score):
    score = score

    die1 = (secrets.randbelow(5)+1) #computer roll
    die2 = (secrets.randbelow(5)+1) #user roll

    displayScore(score)

    winner = checkWinner(die1, die2)
    score = updateScore(score, status)

    if winner == 0:
        loseScreen(die1, die2, winner, score)
    elif winner == 1:
        winScreen(die1, die2, winner, score)
    else:
        drawScreen(die1, winner, score)



# user won
def winScreen(die1, die2, num, score):
    score = score

    displayScore(score)

    gameTime(score)


# screen for when user loses
def loseScreen(die1, die2, num, score):
    score = score

    displayScore(score)

    gameTime(score)
  

# screen for when computer and user dice are equal
def drawScreen(die1, num, score):
   
    score = score

    displayScore(score)

    gameTime(score)