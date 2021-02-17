import os
import time
import signal
import random

from config import *
from utils import *
from screen import *
from background import *
from input import *
from brick import *
from ball import *
from paddle import *
from player import *
from powerups import *


def action(ch):
    """takes action according to the keyboard input"""
    # quit the game
    if ch == 'q':
        myPlayer.GameOver(QUIT)
    
    # move the paddle right
    if ch == 'd':
        myPaddle.moveRight(myGrid.getGrid())
        if ball.isOnPaddle():
            ball.moveWithPaddle(myGrid.getGrid(), myPaddle.getPosX() + rand_x_ball)

    # move the paddle left
    elif ch == 'a':
        myPaddle.moveLeft(myGrid.getGrid())
        if ball.isOnPaddle():
            ball.moveWithPaddle(myGrid.getGrid(), myPaddle.getPosX() + rand_x_ball)

    # release the ball, if on paddle
    if ch == ' ':
        if ball.isOnPaddle():
            ball.release(myPaddle)


if __name__ == '__main__':

    # Initialize the player
    myPlayer = Player()

    # Initialize the screen and background box for the game
    myGrid = Screen(HEIGHT, WIDTH)
    myBox = Box()
    myBox.createBox(myGrid.getGrid())

    # Initialize the paddle, ball
    random_x = random.randint(LEFTWALL, BOX_WIDTH)
    myPaddle = Paddle(random_x, HEIGHT - 2)
    myPaddle.placePaddle(myGrid.getGrid(), random_x)
    rand_x_ball = random.randint(0, myPaddle.getLength() - 1)
    ball = Ball(myPaddle.getPosX() + rand_x_ball, HEIGHT - 3, myGrid.getGrid())

    # Initialize the bricks and layout
    bricks = []
    makeLayout(bricks,myGrid.getGrid())
    
    # Initialize the powerups
    powerups = []
    activatedPowerups = []
    

    # storing the time values, used later
    start_time = time.time()
    curr_time = time.time()
    seconds_time = time.time()

    os.system('clear')
    # main loop of the game
    while True:
        # to keep the cursor at the same place (0,0)
        reposition_cursor()

        # updating the timer at every second
        if (0.9 < time.time() - seconds_time < 1.1):
            seconds_time = time.time()
            myPlayer.setTimer()

        # run loop if the condition is true, sets the interval between each game frame
        if (time.time() - curr_time >= 0.15):
            curr_time = time.time()

            # game time limit
            if myPlayer.getTimer() <= 0:
                myPlayer.GameOver(TIME_OVER)

            # action performed based on input from keyboard
            ch = get_input()
            action(ch)

            # check all the powerups, movement, activation and deactivation
            movePowerups(powerups,activatedPowerups,myGrid.getGrid(), myPaddle,myPlayer,ball)
            # check the active powerups and deactive/delete accordingly
            deleteActivePowerups(activatedPowerups,myGrid.getGrid(),myPaddle,ball)


            # if the ball is out of the screen
            if ball.isOutOfScreen():
                # delete the ball and re initialize the ball
                del ball
                rand_x_ball = random.randint(0, myPaddle.getLength() - 1)
                ball = Ball(myPaddle.getPosX() + rand_x_ball, HEIGHT - 3, myGrid.getGrid())
                # reduce the life of player
                myPlayer.reduceLife()
                #  deactivate/delete every powerup, already activated or not
                deleteAllPowerups(powerups,myGrid.getGrid())
                deleteActivePowerups(activatedPowerups,myGrid.getGrid(),myPaddle,ball,all=True)

            # exit the loop if the game is over
            if myPlayer.isGameOver():
                break

            # moving the ball to correct place
            ball.move(myGrid.getGrid(), myPaddle,bricks,myPlayer,powerups)

            
            # delete the inactive bricks
            deleteBricks(bricks)
            # print the rest bricks
            printBricks(myGrid.getGrid(),bricks) 

            # if all the bricks are destroyed - VICTORY
            if not leftBricks(bricks):
                myPlayer.GameOver(VICTORY)

            # print the stats and the top header of the game session
            myPlayer.showStats()
            myBox.createBox(myGrid.getGrid())
            myGrid.printGrid()

