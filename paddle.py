from config import *
from thing import Thing

class Paddle(Thing):
    ''' class for the Paddle'''

    def __init__(self, x, y):
        super().__init__(x,y)
        # self.__x = x
        # self.__y = y
        # self._oldx = 0

        # step length while moving
        self._stepX = 3

        self._lengthX = 10
        
        self._fig = np.full(
            (1, self._lengthX), MAGENTA + '=' + RESET, dtype='<U20')
        # self.__fig = MAGENTA + '=' + RESET

    # def getPosX(self):
    #     return self.__x

    # def getPosY(self):
    #     return self.__y

    def getLength(self):
        return self._lengthX

    # def updateOld(self):
    #     self._oldx = self._x

    # def erase(self, grid):
    #     x, y = self._oldx, self._oldy
    #     grid[y, x:x + self._lengthX] = ' '

    def placePaddle(self, grid, x):

        if x < LEFTWALL:
            x = LEFTWALL
        elif x > BOX_WIDTH - self._lengthX:
            x = BOX_WIDTH - self._lengthX

        self._x = x
        grid[self._y, self._x: self._x + self._lengthX] = self._fig

    def moveRight(self, grid):
        newX = self._x + self._stepX
        self.updateOld()
        self.erase(grid)
        self.placePaddle(grid, newX)

    def moveLeft(self, grid):
        newX = self._x - self._stepX
        self.updateOld()
        self.erase(grid)
        self.placePaddle(grid, newX)
