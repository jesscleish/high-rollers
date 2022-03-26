from matplotlib.pyplot import draw
import pygame

from pygame.locals import *
pygame.init()
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
    'dR' : (135, 47, 31)
}

# storing screen variable values
width = screen.get_width()
height = screen.get_height()

# text_on_screen() not affected by mouse position variables


# Game main menu, with start and exit buttons
def main_menu():
    
    # track position of mouse
    mx, my = pygame.mouse.get_pos()

    # Generate play/quit buttons
    playButton = pygame.Rect(width/7, (height/2), 200, 100)
    quitButton = pygame.Rect(((width/7)+200+width/7), (height/2), 200, 100)

    # Hover on buttons
    if playButton.collidepoint((mx, my)):
        # Rendering button darker green
        pygame.draw.rect(screen, gameColours['dG'], playButton)
    else:
        # Rendering button green
        pygame.draw.rect(screen, gameColours['green'], playButton)


    if quitButton.collidepoint((mx,my)):
        # Rendering button darker red
        pygame.draw.rect(screen, gameColours['dR'], quitButton)
    else:
        # Rendering button light red
        pygame.draw.rect(screen, gameColours['red'], quitButton)

# tableGen() not affected by mouse position variables

# getCatPath() not affected by mouse position variables

# updateScore() not affected by mouse position variables

# displayScore() not affected by mouse position variables


# Begins the "lets roll" screen of game, with button to start
def gameTime(score):


    # mouse position
    mx, my = pygame.mouse.get_pos()

    rollButton = pygame.Rect(width/3, (height-100), 225, 70)

    # Hover on roll button
    if rollButton.collidepoint((mx, my)):
        pygame.draw.rect(screen, gameColours['dR'], rollButton)
        
    else:
        pygame.draw.rect(screen, gameColours['red'], rollButton)
        

# checkWinner() not affected by mouse position variables

# getDice() not affected by mouse position variables

# showDice() not affected by mouse position variables

# gameLogic() not affected by mouse position variables


# user won
def winScreen(die1, die2, status, score):
    
    # mouse coordinates
    mx, my = pygame.mouse.get_pos()

    againButton = pygame.Rect(width/7, (height-70), 225, 50)
    quitButton = pygame.Rect(width/7+300, (height-70), 225, 50)

    # hover effects (collision)
    if againButton.collidepoint((mx, my)):
        pygame.draw.rect(screen, gameColours['dG'], againButton)
        
    else:
        pygame.draw.rect(screen, gameColours['green'], againButton)


    if quitButton.collidepoint((mx, my)):
        pygame.draw.rect(screen, gameColours['dR'], quitButton)

    else:
        pygame.draw.rect(screen, gameColours['red'], quitButton)


# screen for when user loses
def loseScreen(die1, die2, status, score):
 
    againButton = pygame.Rect(width/7, (height-70), 225, 50)
    quitButton = pygame.Rect(width/7+300, (height-70), 225, 50)

    # mouse coordinates
    mx, my = pygame.mouse.get_pos()

    # hover collision
    if againButton.collidepoint((mx, my)):
        pygame.draw.rect(screen, gameColours['dG'], againButton)
    else:
        pygame.draw.rect(screen, gameColours['green'], againButton)

    if quitButton.collidepoint((mx, my)):
        pygame.draw.rect(screen, gameColours['dR'], quitButton)
    else:
        pygame.draw.rect(screen, gameColours['red'], quitButton)



# screen for when computer and user dice are equal
def drawScreen(die1, status, score):
    
        againButton = pygame.Rect(width/7, (height-70), 225, 50)
        quitButton = pygame.Rect(width/7+300, (height-70), 225, 50)

        mx, my = pygame.mouse.get_pos()

        if againButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, gameColours['dG'], againButton)
        else:
            pygame.draw.rect(screen, gameColours['green'], againButton)
      

        if quitButton.collidepoint((mx, my)):
            pygame.draw.rect(screen, gameColours['dR'], quitButton)
        else:
            pygame.draw.rect(screen, gameColours['red'], quitButton)
    
