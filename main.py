import os
import time
import signal
import random
import random

from config import *
from screen import *
from background import *
from input import *
from brick import *
from ball import *
from paddle import *


def action(ch):
    # move the paddle right
    if ch == 'd':
        myPaddle.moveRight(myGrid.getGrid())
        if ball.isOnPaddle():
            ball.moveWithPaddle(
                myGrid.getGrid(),
                myPaddle.getPosX() +
                ini_x_ball)

    # move the paddle left
    elif ch == 'a':
        myPaddle.moveLeft(myGrid.getGrid())
        if ball.isOnPaddle():
            ball.moveWithPaddle(
                myGrid.getGrid(),
                myPaddle.getPosX() +
                ini_x_ball)

    # release the ball, if on paddle
    if ch == ' ':
        if ball.isOnPaddle():
            ball.release(myPaddle)


if __name__ == '__main__':

    # Initialize the screen and background box for the game
    myGrid = Screen(HEIGHT, WIDTH)
    myBox = Box()
    myBox.createBox(myGrid.getGrid())

    # Initialize the paddle, ball, and bricks
    random_x = random.randint(LEFTWALL, BOX_WIDTH)
    myPaddle = Paddle(random_x, HEIGHT - 2)
    myPaddle.placePaddle(myGrid.getGrid(), random_x)
    ini_x_ball = random.randint(0, myPaddle.getLength() - 1)
    ball = Ball(myPaddle.getPosX() + ini_x_ball, HEIGHT - 3, myGrid.getGrid())

    start_time = time.time()
    curr_time = time.time()

    # main loop of the game
    while True:

        # to keep the cursor at the same place (0,0)
        print("\033[%d;%dH" % (0, 0))

        if (time.time() - curr_time >= 0.15):
            curr_time = time.time()

            ch = get_input()
            if ch == 'q':
                showmessage("Quit")
                break

            action(ch)
            ball.move(myGrid.getGrid(), myPaddle)

            myBox.createBox(myGrid.getGrid())
            myGrid.printGrid()
