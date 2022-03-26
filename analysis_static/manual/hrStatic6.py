from matplotlib.pyplot import draw
import pygame
import sys
import secrets

from pygame.locals import *
pygame.init()
pygame.font.init()
pygame.mixer.init()

# set screen re# screen setup not required/affected by die1/computer roll variable

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

# showDice() not affected by die1/computer roll variable


# generate rolls, next screen navigation
def gameLogic(score):

    die2 = (secrets.randbelow(5)+1) #user roll

    winner = checkWinner(die1, die2)
    if status == 0:
        loseScreen(die1, die2, winner, score)
    elif winner == 1:
        winScreen(die1, die2, winner, score)
    else:
        drawScreen(die1, winner, score)


# user won
def winScreen(die1, die2, num, score):
    user = die2

    cRoll, uRoll = getDice(computer, user) # get dice img paths


# screen for when user loses
def loseScreen(die1, die2, num, score):
    
    user = die2

    cRoll, uRoll = getDice(computer, user)
        
