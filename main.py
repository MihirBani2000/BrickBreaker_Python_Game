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
from weapon import *
from boss import *

def action(ch,level):
    """takes action according to the keyboard input"""
    # quit the game
    if ch == 'q':
        myPlayer.GameOver(QUIT)
    
    # move the paddle right
    if ch == 'd':
        myPaddle.moveRight(myGrid.getGrid())
    
        if level==LEVELS:
            myBoss.moveRight(myGrid.getGrid(),balls)
    
    # move the paddle left
    elif ch == 'a':
        myPaddle.moveLeft(myGrid.getGrid())
    
        if level==LEVELS:
            myBoss.moveLeft(myGrid.getGrid(),balls)
    
    # release the ball, if on paddle
    if ch == ' ':
        for ball in balls:
            if ball.isOnPaddle():
                ball.release(myPaddle)
    
    # skip to the next level
    if ch == 'x':
        if level<LEVELS:
            return True
        elif level==LEVELS:
            myPlayer.GameOver(QUIT)
    return False


if __name__ == '__main__':

    # levels
    level = 0
    # Initialize the player
    myPlayer = Player()

    while (0 <= level < LEVELS):
        os.system('clear')
        level+=1
        level_break_flag = 0

        # Initialize the screen and background box for the game
        myGrid = Screen(HEIGHT, WIDTH)
        myBox = Box()
        myBox.createBox(myGrid.getGrid())

        # Initialize the paddle
        random_x = random.randint(LEFTWALL, BOX_WIDTH)
        myPaddle = Paddle(random_x, HEIGHT - 2)
        myPaddle.placePaddle(myGrid.getGrid(), random_x)
        
        # Initialize the boss in final level
        if level==LEVELS:
            myBoss = Boss(random_x, 1)
            myBoss.placeBoss(myGrid.getGrid(), random_x)
        else:
            myBoss = None
        bombs = []
        
        # Initialize the ball
        balls = []
        rand_x_ball = random.randint(0, myPaddle.getLength() - 1)
        ball_1 = Ball(myPaddle.getPosX() + rand_x_ball, HEIGHT - 3, myGrid.getGrid())
        ball_1.setPaddleOffset(rand_x_ball)
        balls.append(ball_1)
        
        # Initialize the bricks and layout
        bricks = []
        chooseLayout(bricks,myGrid.getGrid(),level)
        
        # Initialize the powerups
        powerups = []
        activatedPowerups = []

        # flag for activation of falling bricks
        falling_flag = 0
        
        # bullets for shooting powerup
        bullets = []

        # storing the time values, used later
        start_time = time.time()
        curr_time = time.time()
        seconds_time = time.time()
        bullet_start_time = time.time()
        bomb_start_time = time.time()
        myPlayer.setTimer(GAME_TIME)

        # main loop of the game
        while not level_break_flag:
        # while True:
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

                # falling bricks time check, and flag
                fall_diff = time.time() - start_time
                if FALLING_BRICK_TIME <= fall_diff:
                    falling_flag = 1
                
                # action performed based on input from keyboard
                ch = get_input()
                if action(ch,level):    
                    level_break_flag = 1
                    # break

                # check all the powerups, movement, activation and deactivation
                movePowerups(powerups,activatedPowerups,myGrid.getGrid(), myPaddle,myPlayer,balls)
                # check the active powerups and deactive/delete accordingly
                deleteActivePowerups(activatedPowerups,myGrid.getGrid(),myPaddle,balls,bullets)

                # shooting bullets
                if myPaddle.isShooting():
                    temp_diff = time.time() - bullet_start_time
                    if SHOOTING_INTERVAL <= temp_diff:
                        bullet_start_time = time.time()
                        myPaddle.shootBullets(myGrid.getGrid(),bullets) 
                        # x1,y1 = myPaddle.getPosX(), myPaddle.getPosY() 
                        # pL = myPaddle.getLength()
                        # x2 = x1 + pL - 1
                        # bullet1 = Bullet(x1,y1-1, myGrid.getGrid())
                        # bullets.append(bullet1)
                        # bullet2 = Bullet(x2,y1-1, myGrid.getGrid())
                        # bullets.append(bullet2)
                else:
                    bullet_start_time = time.time() - SHOOTING_INTERVAL

                # delete the old bullets
                delItems(bullets)
                
                # if the last/only ball is out of the screen
                delBalls(balls)
                if not balls:
                    rand_x_ball = random.randint(0, myPaddle.getLength() - 1)
                    ball_2 = Ball(myPaddle.getPosX() + rand_x_ball, HEIGHT - 3, myGrid.getGrid())
                    ball_2.setPaddleOffset(rand_x_ball)
                    balls.append(ball_2)

                    # reduce the life of player
                    myPlayer.reduceLife()

                    #  deactivate/delete every powerup, already activated or not
                    deleteAllPowerups(powerups,myGrid.getGrid())
                    deleteActivePowerups(activatedPowerups,myGrid.getGrid(),myPaddle,balls,bullets,all=True)


                # exit the loop if the game is over
                if myPlayer.isGameOver():
                    exit()

                if level==LEVELS:
                # if its the final level
                    
                    # dropping bombs
                    temp_diff = time.time() - bomb_start_time
                    if BOMB_INTERVAL <= temp_diff:
                        bomb_start_time = time.time()
                        myBoss.dropBombs(myGrid.getGrid(),bombs) 
                    
                    # delete the old bombs
                    delItems(bombs)

                    if bombs:
                        for bomb in bombs:
                            # moving the bomb to correct place
                            bomb.move(myGrid.getGrid(),myPaddle,myPlayer)
                
                for ball in balls:
                # moving the ball to correct place
                    ball.move(myGrid.getGrid(), myPaddle,bricks,myPlayer,powerups,myBoss,falling_flag)

                if bullets:
                    for bullet in bullets:
                        # moving the bullet to correct place
                        bullet.move(myGrid.getGrid(),bricks,myPlayer,powerups,myBoss)
                
                # delete the inactive bricks
                deleteBricks(bricks)

                # print the remaining bricks
                printBricks(myGrid.getGrid(),bricks,myPlayer,myPaddle) 
                
                # if all the bricks are destroyed - VICTORY
                if not leftBricks(bricks):
                    if level<LEVELS:
                        level_break_flag=1
                    else:
                        myPlayer.GameOver(VICTORY)

                # exit the code if the game is over
                if myPlayer.isGameOver():
                    exit()
                
                # print the stats and the top header of the game session
                myPlayer.showStats(myPaddle,activatedPowerups,level,myBoss)
                myBox.createBox(myGrid.getGrid())
                myGrid.printGrid()

