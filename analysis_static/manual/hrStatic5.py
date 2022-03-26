from matplotlib.pyplot import draw
import pygame
import secrets

from pygame.locals import *
pygame.init()

# screen setup not required/affected by die1/computer roll variable

# text_on_screen() not affected by die1/computer roll variable

# main_menu() not affected by die1/computer roll variable

# tableGen() not affected by die1/computer roll variable

# getCatPath() not affected by die1/computer roll variable

# updateScore() not affected by die1/computer roll variable

# displayScore() not affected by die1/computer roll variable

# gameTime() not affected by die1/computer roll variable


# checks winner based on dice inputs
def checkWinner(roll1, roll2):
    if (roll1 > roll2): # Computer wins
        return 0

    elif(roll1 < roll2):   # User wins
        return 1

    elif(roll1 == roll2): # Draw
        return 2


# Obtains image path for computer and user rolled dice
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

    return (compRoll, userRoll) #userRoll no longer variable used, but still included in the line to preserve source code

# showDice() not affected by die1/computer roll variable

# generate rolls, next screen navigation
def gameLogic(score):

    die1 = (secrets.randbelow(5)+1) #computer roll

    status = checkWinner(die1, die2)
    if status == 0:
        loseScreen(die1, die2, status, score)
    elif status == 1:
        winScreen(die1, die2, status, score)
    else:
        drawScreen(die1, status, score)


# user won
def winScreen(die1, die2, status, score):
    computer = die1

    cRoll, uRoll = getDice(computer, user) # get dice img paths

# screen for when user loses
def loseScreen(die1, die2, status, score):
    
    computer = die1

    cRoll, uRoll = getDice(computer, user)
        

# screen for when computer and user dice are equal
def drawScreen(die1, status, score):
  
    roll = die1

    cRoll, uRoll = getDice(roll, roll)
