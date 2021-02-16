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

    # quit the game
    if ch == 'q':
        showmessage(QUIT,myPlayer)
        myPlayer.GameOver()
    
    # move the paddle right
    if ch == 'd':
        myPaddle.moveRight(myGrid.getGrid())
        if ball.isOnPaddle():
            ball.moveWithPaddle(myGrid.getGrid(), myPaddle.getPosX() + ini_x_ball)

    # move the paddle left
    elif ch == 'a':
        myPaddle.moveLeft(myGrid.getGrid())
        if ball.isOnPaddle():
            ball.moveWithPaddle(myGrid.getGrid(), myPaddle.getPosX() + ini_x_ball)

    # release the ball, if on paddle
    if ch == ' ':
        if ball.isOnPaddle():
            ball.release(myPaddle)


if __name__ == '__main__':
    os.system('clear')

    # Initialize the screen and background box for the game
    myGrid = Screen(HEIGHT, WIDTH)
    myBox = Box()
    myBox.createBox(myGrid.getGrid())

    # Initialize the player
    myPlayer = Player()

    # Initialize the paddle, ball
    random_x = random.randint(LEFTWALL, BOX_WIDTH)
    myPaddle = Paddle(random_x, HEIGHT - 2)
    myPaddle.placePaddle(myGrid.getGrid(), random_x)
    ini_x_ball = random.randint(0, myPaddle.getLength() - 1)
    ball = Ball(myPaddle.getPosX() + ini_x_ball, HEIGHT - 3, myGrid.getGrid())

    # Initialize the bricks
    bricks = []
    obj_brick = Brick()
    br_xlen,br_ylen = obj_brick.getLength()
    # print(br_xlen)
    for i in range(2,15):
        rbrick = RedBrick(myGrid.getGrid(), i * (br_xlen+2) + 2, 15)
        bricks.append(rbrick)
        cbrick = CyanBrick(myGrid.getGrid(), i * (br_xlen+2) - 2, 15 - 2*(br_ylen+1) )
        bricks.append(cbrick)
        grbrick = GreenBrick(myGrid.getGrid(), i * (br_xlen+2) - 4, 15 - 4*(br_ylen+1))
        bricks.append(grbrick)
        # YET TO DO
        # goldbrick = GoldBrick(myGrid.getGrid(), i * (br_xlen+2) - 4, 15 - 4*(br_ylen+1))
        # bricks.append(goldbrick)

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


        if (time.time() - curr_time >= 0.15):
            curr_time = time.time()

            if myPlayer.getTimer() <= 0:
                showmessage(TIME_OVER,myPlayer)
                myPlayer.GameOver()

            ch = get_input()
            # action performed based on input from keyboard
            action(ch)

            # if the ball is out of the screen
            if ball.isOutOfScreen():
                # delete the ball and re initialize the ball
                del ball
                ran_x_ball = random.randint(0, myPaddle.getLength() - 1)
                ball = Ball(myPaddle.getPosX() + ran_x_ball, HEIGHT - 3, myGrid.getGrid())
                # also reduce the life of player
                myPlayer.reduceLife()

            if myPlayer.isGameOver():
                break

            # moving the ball to correct place
            ball.move(myGrid.getGrid(), myPaddle,bricks,myPlayer)

            myPlayer.showStats()
            myBox.createBox(myGrid.getGrid())
            myGrid.printGrid()

