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
    os.system('clear')

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

    # Initialize the bricks
    bricks = []
    obj_brick = Brick()
    br_xlen,br_ylen = obj_brick.getLength()
    # grbrick = GreenBrick(myGrid.getGrid(), 4 * (br_xlen+2) - 4, 15 - 4*(br_ylen+1))
    # bricks.append(grbrick)
    # gobrick = GoldBrick(myGrid.getGrid(), 9 * (br_xlen+2) - 4, 15 - 4*(br_ylen+1))
    # bricks.append(gobrick)
    for i in range(1,11):
        if i in [3,8]:
            rbrick = GoldBrick(myGrid.getGrid(), i * (br_xlen+6), 15)
            grbrick = GoldBrick(myGrid.getGrid(), i * (br_xlen+4)+10, 15 - 4*(br_ylen))
        else :
            rbrick = RedBrick(myGrid.getGrid(), i * (br_xlen+6), 15)
            grbrick = GreenBrick(myGrid.getGrid(), i * (br_xlen+4)+10, 15 - 4*(br_ylen))
        
        if i in [1,5,6,10]:
            cbrick = GoldBrick(myGrid.getGrid(), i * (br_xlen+5)+5 , 15 - 2*(br_ylen) )
        else:    
            cbrick = CyanBrick(myGrid.getGrid(), i * (br_xlen+5)+5 , 15 - 2*(br_ylen) )

        bricks.append(rbrick)
        bricks.append(grbrick)
        bricks.append(cbrick)

    # for i in range(1,11):
    #     cbrick = CyanBrick(myGrid.getGrid(), i * (br_xlen+5)+5 , 15 - 2*(br_ylen) )
    #     bricks.append(cbrick)

    # for i in range(1,11):
    #     grbrick = GreenBrick(myGrid.getGrid(), i * (br_xlen+4)+10, 15 - 4*(br_ylen))
    #     bricks.append(grbrick)
    # for i in range(1,11):
    #     goldbrick = GoldBrick(myGrid.getGrid(), i * (br_xlen+2) - 4, 15 - 4*(br_ylen+1))
    #     bricks.append(goldbrick)
    #     pass
    
    
    # storing the time values, used later
    start_time = time.time()
    curr_time = time.time()
    seconds_time = time.time()

    # main loop of the game
    while True:
        # to keep the cursor at the same place (0,0)
        reposition_cursor()

        # updating the timer at every second
        if (0.9 < time.time() - seconds_time < 1.1):
            seconds_time = time.time()
            myPlayer.setTimer()

        # run loop if condition
        if (time.time() - curr_time >= 0.15):
            curr_time = time.time()

            # # updating the timer at every second
            # if (0.9 < time.time() - seconds_time < 1.1):
            #     seconds_time = time.time()
            #     myPlayer.setTimer()

            if myPlayer.getTimer() <= 0:
                myPlayer.GameOver(TIME_OVER)

            ch = get_input()
            # action performed based on input from keyboard
            action(ch)

            # if the ball is out of the screen
            if ball.isOutOfScreen():
                # delete the ball and re initialize the ball
                del ball
                rand_x_ball = random.randint(0, myPaddle.getLength() - 1)
                ball = Ball(myPaddle.getPosX() + rand_x_ball, HEIGHT - 3, myGrid.getGrid())
                # also reduce the life of player
                myPlayer.reduceLife()

            # exit the loop if the game is over
            if myPlayer.isGameOver():
                break

            # moving the ball to correct place
            ball.move(myGrid.getGrid(), myPaddle,bricks,myPlayer)

            # delete the inactive bricks
            deleteBricks(bricks)

            # if all the bricks are destroyed - VICTORY
            if not leftBricks(bricks):
                myPlayer.GameOver(VICTORY)

            # print the stats and the top header of the game session
            myPlayer.showStats()
            myBox.createBox(myGrid.getGrid())
            myGrid.printGrid()

