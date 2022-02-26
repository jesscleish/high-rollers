import pytest
import pygame
import highrollers
import secrets

# Test the resolution is set
def testScreenExist():
    assert highrollers.resolution == (725,725)

# Test the width and height are set from the resolution
def testWidthHeight():
    assert highrollers.width == 725
    assert highrollers.height == 725

# Test the dices passed result in "win" status detection
def testWinDisp():
    die1 = 2 #computer
    die2 = 6 #user
    result = highrollers.checkWinner(die1, die2)
    assert result == 1


# Test the dices passed result in "lose" status detection
def testLoseDisp():
    die1 = 5 #computer
    die2 = 1 #user
    result = highrollers.checkWinner(die1, die2)
    assert result == 0

# Test the dices passed result in "draw" status detection
def testDrawDisp():
    die1 = 3 #computer
    die2 = 3 #user
    result = highrollers.checkWinner(die1, die2)
    assert result == 2

# Tests the die roll to ensure a value is set
def testDieSet():
    die = (secrets.randbelow(5)+1) #get a roll
    assert die is not None

# ensure roll =1 die assets both displayed
def testDispDie1():
    compRoll, userRoll = highrollers.getDice(1,1)
    assert compRoll == "assets/b1.png"
    assert userRoll == "assets/r1.png"

# ensure roll =2 die assets both displayed
def testDispDie2():
    compRoll, userRoll = highrollers.getDice(2,2)
    assert compRoll == "assets/b2.png"
    assert userRoll == "assets/r2.png"

# ensure roll =3 die assets both displayed
def testDispDie3():
    compRoll, userRoll = highrollers.getDice(3,3)
    assert compRoll == "assets/b3.png"
    assert userRoll == "assets/r3.png"

# ensure roll =4 die assets both displayed
def testDispDie4():
    compRoll, userRoll = highrollers.getDice(4,4)
    assert compRoll == "assets/b4.png"
    assert userRoll == "assets/r4.png"

# ensure roll =5 die assets both displayed
def testDispDie5():
    compRoll, userRoll = highrollers.getDice(5,5)
    assert compRoll == "assets/b5.png"
    assert userRoll == "assets/r5.png"

# ensure roll =6 die assets both displayed
def testDispDie6():
    compRoll, userRoll = highrollers.getDice(6,6)
    assert compRoll == "assets/b6.png"
    assert userRoll == "assets/r6.png"

# test victory cat path is obtained
def testWinCat():
    catPath = highrollers.getCatPath(0)
    assert catPath == "assets/wincat.png"

# test loss cat path is obtained
def testLoseCat():
    catPath = highrollers.getCatPath(1)
    assert catPath == "assets/losecat.png"

# test draw cat path is obtained
def testDrawCat():
    catPath = highrollers.getCatPath(2)
    assert catPath == "assets/draw.png"

# Test collision with "PLAY" button triggers (main screen)
def testPlayGame():
    #use mock action here to simulate clicking play on main menu
    mx, my = (highrollers.width/7), (highrollers.height/2)
    playButton = pygame.Rect(highrollers.width/7, (highrollers.height/2), 200, 100)
    assert playButton.collidepoint((mx,my)) == True

# Test collision with "QUIT" button triggers (main screen)
def testExit():
    # simulate mouse collision and verify it is detected
    mx, my = ((highrollers.width/7)+200+highrollers.width/7), (highrollers.height/2)
    quitButton = pygame.Rect(((highrollers.width/7)+200+highrollers.width/7), (highrollers.height/2), 200, 100)
    assert quitButton.collidepoint((mx,my)) == True

# Test collision with "ROLL" button triggers
def testStartRoll():
    # simulate mouse collision and verify it is detected
    mx, my = (highrollers.width/3), (highrollers.height-100)
    rollButton = pygame.Rect(highrollers.width/3, (highrollers.height-100), 225, 70)
    assert rollButton.collidepoint((mx,my))

# Test collision with "play again" button triggers 
def testPlayAgain():
    # simulate mouse collision and verify it is detected
    mx, my = (highrollers.width/7), (highrollers.height-70)
    againButton = pygame.Rect(highrollers.width/7, (highrollers.height-70), 225, 50)
    assert againButton.collidepoint((mx, my)) == True

# collision with "quit" button triggers (outcome screen)
def testQuit():
    # simulate mouse collision and verify it is detected
    mx, my = (highrollers.width/7+300), (highrollers.height-70)
    quitButton = pygame.Rect(highrollers.width/7+300, (highrollers.height-70), 225, 50)
    assert quitButton.collidepoint((mx, my)) == True

# Test increasing score actually increases
def testScoreUp():
    score = 50
    score = highrollers.updateScore(score, 1)
    assert score == 51

# Test decreasing score actually decreases
def testScoreDown():
    score = 50
    score = highrollers.updateScore(score, 0)
    assert score == 49

# Test draw results in no score change
def testScoreDraw():
    score = 50
    score = highrollers.updateScore(score, 2)
    assert score == 50

# Test all palette colours defined correctly
def testPalette():
    assert highrollers.gameColours['background'] == (252, 222, 190)
    assert highrollers.gameColours['green'] == (101, 155, 94)
    assert highrollers.gameColours['dG'] == (73, 113, 69)
    assert highrollers.gameColours['red'] == (200, 70,48)
    assert highrollers.gameColours['dR'] == (135, 47, 31)
    assert highrollers.gameColours['yellow']== (255, 188, 66)
    assert highrollers.gameColours['dY'] == (204, 145, 37)
    assert highrollers.gameColours['black'] == (35, 32, 32)
    assert highrollers.gameColours['brown'] ==(90, 53, 42)
    assert highrollers.gameColours['linen'] == (254, 245, 236)

# Test table generation function is successful
def testTable():
    status = highrollers.tableGen()
    assert status == True