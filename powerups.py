import time

from numpy.lib.arraypad import pad
from config import *
from thing import Thing

class Powerup(Thing):

    def __init__(self,x,y):
        super().__init__(x,y)      

        self._isActive = False
        self._time = None
        self._speedY = 1
        self._onScreen = True
        self._fig = Back.GREEN + "P" + RESET
    
    def activate(self):
        '''returns true if successfully activated, false otherwise'''

        if not self._isActive:
            self._isActive = True
            self._time = time.time()
            return True
        return False

    def deActivate(self):
        '''returns true if successfully deactivated, false otherwise'''

        if not self._isActive:
            return False
        
        self._isActive = False
        return True

    def getTime(self):
        return self._time


    def checkCollisionPaddle(self,grid, x, y, paddle=None,ball=None):
        pX = paddle.getPosX()
        pL = paddle.getLength()
        activationFlag = False

        if pX <= x <= pX + pL:
            # within the x coordinates of paddle
            if y > HEIGHT - 3:
                # Colliding with the paddle
                self._y = HEIGHT - 3
                activationFlag = self.activate(grid,paddle,ball)
                self.erase(grid)
                self._onScreen = False
                

        elif y > HEIGHT - 3:
            # powerup missed the paddle
            self._y = HEIGHT - 3
            self.erase(grid)
            self._onScreen = False

        self._y = y
        return activationFlag

    def move(self, grid, paddle=None, player=None,ball=None):
        activationFlag = False
        if self._onScreen:
            # print("debug")
            newY = self._y + self._speedY
            self.erase(grid)

            activationFlag = self.checkCollisionPaddle(grid,self._x,newY,paddle,ball)

            # placing the powerup at the required coordinates after checking collisions
            if grid[self._y,self._x]  == ' ' and (self._y < HEIGHT-3):
                grid[self._y,self._x] = self._fig

        return activationFlag


# Paddle powerups
        # expand paddle
        # shrink paddle
        # paddle grab
class ExpandPaddle(Powerup):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._fig = EXPAND_FIG
        # self._onScreen = True

    def activate(self,grid,paddle,ball):
        if paddle.getLength() + EXPAND <= MAX_PADDLE_LENGTH :
            if super().activate():
                paddle.expandLength(grid,EXPAND,ball)
            return True
        return False
    def deActivate(self,grid,paddle,ball):
        if super().deActivate():
            paddle.shrinkLength(grid,EXPAND,ball)
            return True
        return False
            

class ShrinkPaddle(Powerup):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._fig = SHRINK_FIG
    
    def activate(self,grid,paddle,ball):
        if paddle.getLength() - SHRINK >= MIN_PADDLE_LENGTH :
            if super().activate():
                paddle.shrinkLength(grid,SHRINK,ball)
            return True
        return False

    def deActivate(self,grid,paddle,ball):
        if super().deActivate():
            paddle.expandLength(grid,SHRINK,ball)
            return True
        return False

# class GrabPaddle(Powerup):
#     # self._ballx
#     # self.
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self._fig = GRAB_FIG
        
#     def activate(self,grid,paddle,ball):
#         # if paddle.getLength() - SHRINK >= MIN_PADDLE_LENGTH :
#         if super().activate():
#             pass
#             # paddle.shrinkLength(grid,SHRINK,ball)

#     def deActivate(self,grid,paddle,ball):
#         if super().deActivate():
#             pass
#             # paddle.expandLength(grid,SHRINK,ball)

# Ball powerups
        # thru ball
        # fast ball
        # ball multiplier
class FastBall(Powerup):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._fig = FAST_FIG
    
    def activate(self,grid,paddle,ball):
        if super().activate():
            ball.setSpeed(FAST_MULTIPLIER)
            return True
        return False

    def deActivate(self,grid,paddle,ball):
        if super().deActivate():
            ball.setSpeed(1/FAST_MULTIPLIER)
            return True
        return False
