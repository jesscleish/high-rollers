from matplotlib.pyplot import draw
import pygame


from pygame.locals import *
pygame.init()
pygame.mixer.init()

# set screen resolution
resolution = (725,725)

# open a screen of above resolution
screen = pygame.display.set_mode(resolution)

# storing screen variable values
width = screen.get_width()
height = screen.get_height()

# text_on_screen() not affected by catPath variable

# main_menu() not affected by catPath variable

# tableGen() not affected by catPath variable


# get appropriate cat path to display in outcome screen
def getCatPath(state):
    if state == 0:
        catPath = "assets/wincat.png"
    elif state == 1:
        catPath = "assets/losecat.png"
    elif state == 2:
        catPath = "assets/draw.png"
    return catPath

# updateScore() not affected by catPath variable

# displayScore() not affected by catPath variable

# gameTime() not affected by catPath variable
        
# checkWinner() not affected by catPath variable

# getDice() not affected by catPath variable

# showDice() not affected by catPath variable

# gameLogic() not affected by catPath variable

# user won
def winScreen(die1, die2, num, score):
    state = num

    # get path to cat image based on win/lose/draw state passed
    catPath = getCatPath(state)
    cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
    #display cat
    screen.blit(cat, ((width/4),(height/2)-325))


# screen for when user loses
def loseScreen(die1, die2, num, score):
    state = num
    # get path to cat image based on win/lose/draw state passed
    catPath = getCatPath(state)
    cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
    #display cat
    screen.blit(cat, ((width/4),(height/2)-325))



# screen for when computer and user dice are equal
def drawScreen(die1, num, score):
  
    state = num

    # get appropriate cat based on game status (win/loss/draw)
    catPath = getCatPath(state)
    cat = pygame.transform.scale(pygame.image.load(catPath).convert_alpha(), (400, 450))
    # Display cat on screeen
    screen.blit(cat, ((width/4),(height/2)-325))
