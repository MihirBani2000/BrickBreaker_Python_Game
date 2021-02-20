from config import *
from thing import Thing

class Paddle(Thing):
    ''' class for the Paddle'''

    def __init__(self, x, y):
        super().__init__(x,y)
    
        # step length while moving
        self._stepX = 3

        self._lengthX = 11
        
        self._fig = np.full(
            (1, self._lengthX), MAGENTA + '=' + RESET, dtype='<U20')

    def getLength(self):
        return self._lengthX

    def updateLength(self,grid,val):
        self.erase(grid)
        self._lengthX += val
        self._fig = np.full(
            (1, self._lengthX), MAGENTA + '=' + RESET, dtype='<U20')
        self.placePaddle(grid,self._x)

    def shrinkLength(self,grid,val,balls):
        for ball in balls:
            if ball.isOnPaddle():
                bX = ball.getPosX()
                rel_b_p_x = self._x + self._lengthX - bX
                if rel_b_p_x <= val:
                    ball.moveWithPaddle(grid, bX - val)
        self.updateLength(grid, -val)

    def placePaddle(self, grid, x):

        if x < LEFTWALL:
            x = LEFTWALL
        elif x > BOX_WIDTH - self._lengthX:
            x = BOX_WIDTH - self._lengthX

        self._x = x
        grid[self._y, self._x: self._x + self._lengthX] = self._fig

    def moveRight(self, grid):
        newX = self._x + self._stepX
        self.erase(grid)
        self.placePaddle(grid, newX)

    def moveLeft(self, grid):
        newX = self._x - self._stepX
        self.erase(grid)
        self.placePaddle(grid, newX)
