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

    def checkCollisionPaddle(self,grid, x, y, paddle=None,balls=None):
        pX = paddle.getPosX()
        pL = paddle.getLength()
        activationFlag = False
        ball_list = []
        isMultiple = isinstance(self,MultipleBall)
        if pX <= x <= pX + pL:
            # within the x coordinates of paddle
            if y > HEIGHT - 3:
                # Colliding with the paddle
                self._y = HEIGHT - 3
                if isMultiple:
                    ball_list = self.activate(grid,paddle,balls)
                else:
                    activationFlag = self.activate(grid,paddle,balls)
                self.erase(grid)
                self._onScreen = False
                
        elif y > HEIGHT - 3:
            # powerup missed the paddle
            self._y = HEIGHT - 3
            self.erase(grid)
            self._onScreen = False

        self._y = y
        if isMultiple:
            return ball_list
        return activationFlag

    def move(self, grid, paddle=None, player=None,balls=None):

        activationFlag = False
        ball_list = []
        isMultiple = isinstance(self,MultipleBall)

        if self._onScreen:

            newY = self._y + self._speedY
            self.erase(grid)

            if isMultiple:
                ball_list = self.checkCollisionPaddle(grid,self._x,newY,paddle,balls)
            else:
                activationFlag = self.checkCollisionPaddle(grid,self._x,newY,paddle,balls)

            # placing the powerup at the required coordinates after checking collisions
            if grid[self._y,self._x]  == ' ' and (self._y < HEIGHT-3):
                grid[self._y,self._x] = self._fig

        if isMultiple:
            return ball_list

        return activationFlag


# Paddle powerups
        # expand paddle
        # shrink paddle
        # paddle grab
class ExpandPaddle(Powerup):
    '''expands the paddle by 2 units'''
    def __init__(self, x, y):
        super().__init__(x, y)
        self._fig = EXPAND_FIG

    def activate(self,grid,paddle,balls):
        if paddle.getLength() + EXPAND <= MAX_PADDLE_LENGTH :
            if super().activate():
                paddle.updateLength(grid,EXPAND)
            return True
        return False
        
    def deActivate(self,grid,paddle,balls):
        if super().deActivate():
            paddle.shrinkLength(grid,EXPAND,balls)
            return True
        return False
            
class ShrinkPaddle(Powerup):
    '''shrinks the paddle by 2 units'''

    def __init__(self, x, y):
        super().__init__(x, y)
        self._fig = SHRINK_FIG
    
    def activate(self,grid,paddle,balls):
        if paddle.getLength() - SHRINK >= MIN_PADDLE_LENGTH :
            if super().activate():
                paddle.shrinkLength(grid,SHRINK,balls)
            return True
        return False

    def deActivate(self,grid,paddle,balls):
        if super().deActivate():
            paddle.updateLength(grid,SHRINK)
            return True
        return False

class GrabPaddle(Powerup):
    '''grabs the ball onto the paddle'''

    def __init__(self, x, y):
        super().__init__(x, y)
        self._fig = GRAB_FIG
        
    def activate(self,grid,paddle,balls):
        if super().activate():
            for ball in balls:
                ball.setSticky(True)
            return True
        return False

    def deActivate(self,grid,paddle,balls):
        if super().deActivate():
            for ball in balls:
                ball.setSticky(False)
            return True
        return False

# Ball powerups
        # fast ball
        # thru ball
        # ball multiplier

class FastBall(Powerup):
    '''Increases the ball speed upto a limit'''
    def __init__(self, x, y):
        super().__init__(x, y)
        self._fig = FAST_FIG
    
    def activate(self,grid,paddle,balls):
        if super().activate():
            for ball in balls:
                ball.setSpeed(FAST_MULTIPLIER)
            return True
        return False

    def deActivate(self,grid,paddle,balls):
        if super().deActivate():
            for ball in balls:
                ball.setSpeed(1/FAST_MULTIPLIER)
            return True
        return False

class ThruBall(Powerup):
    '''makes the ball to go past all bricks, by destroying it'''
    def __init__(self, x, y):
        super().__init__(x, y)
        self._fig = THRU_FIG
    
    def activate(self,grid,paddle,balls):
        if super().activate():
            for ball in balls:
                ball.setThru(True)
            return True
        return False

    def deActivate(self,grid,paddle,balls):
        if super().deActivate():
            for ball in balls:
                ball.setThru(False)
            return True
        return False

class MultipleBall(Powerup):
    '''Increases the ball speed upto a limit'''
    def __init__(self, x, y):
        super().__init__(x, y)
        self._fig = MULITPLE_FIG
    
    def activate(self,grid,paddle,balls):
        if super().activate():
            newballs = []
            for ball in balls:
                newball = ball.split(grid,paddle)
                newballs.append(newball)
            return newballs
        return False

    def deActivate(self,grid,paddle,balls):
        if super().deActivate():
            # if balls have more than one ball, remove the extra balls
            half_len = int(len(balls)/2)
            if half_len >= 1:
                while len(balls) > half_len:
                    delball = balls.pop()
                    delball.erase(grid)
                    del delball
            return True
        return False