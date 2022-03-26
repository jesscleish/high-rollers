from matplotlib.pyplot import draw
import pygame
import sys
import secrets


from pygame.locals import *
pygame.init()
pygame.font.init()
pygame.mixer.init()

# set screen resolution
resolution = (725,725)

# open a screen of above resolution
screen = pygame.display.set_mode(resolution)

# storing screen variable values REQUIRED FOR DISPLAY
width = screen.get_width()
height = screen.get_height()

# text_on_screen() not affected by winner/state/num variable

# main_menu() not affected by winner/state/num variable

# tableGen() not affected by winner/state/num variable

# get appropriate cat path to display in outcome screen
def getCatPath(state):
    if state == 0:
        catPath = "assets/wincat.png"
    elif state == 1:
        catPath = "assets/losecat.png"
    elif state == 2:
        catPath = "assets/draw.png"


# tableGen not affected by winner/state/num variable

# Updates score based on win/lose/draw
def updateScore(score, status):
    if status == 0:
        score = (score-1)
    elif status == 1:
        score = (score+1)

# displayScore() not affected by winner/state/num variable

# gameTime() not affected by winner/state/num variable


# checks winner based on dice inputs -> UPDATES STATE
def checkWinner(roll1, roll2):
    if (roll1 > roll2): # Computer wins
        return 0

    elif(roll1 < roll2):   # User wins
        return 1

    elif(roll1 == roll2): # Draw
        return 2


# getDice() not affected by winner/state/num variable

# showDice() not affected by winner/state/num variable


# generate rolls, next screen navigation
def gameLogic(score):
    
    die1 = (secrets.randbelow(5)+1) #computer roll
    die2 = (secrets.randbelow(5)+1) #user roll

    winner = checkWinner(die1, die2)
    score = updateScore(score, winner)
    if winner == 0:
        loseScreen(die1, die2, winner, score)
    elif winner == 1:
        winScreen(die1, die2, winner, score)
    else:
        drawScreen(die1, winner, score)



# user won
def winScreen(die1, die2, num, score):

    status = num

    catPath = getCatPath(status)
    cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
    screen.blit(cat, ((width/4),(height/2)-325))



# screen for when user loses
def loseScreen(die1, die2, num, score):
   
    status = num

    # get path to cat image based on win/lose/draw state passed
    catPath = getCatPath(status)
    cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
    screen.blit(cat, ((width/4),(height/2)-325))


# screen for when computer and user dice are equal
def drawScreen(die1, num, score):
   
    status = num

    # get appropriate cat based on game status (win/loss/draw)
    catPath = getCatPath(status)
    cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
    # Display cat on screeen
    screen.blit(cat, ((width/4),(height/2)-325))