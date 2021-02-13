from config import *


class Paddle():
    ''' class for the Paddle'''

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

        self.__oldx = 0
        
        # step length while moving
        self.__stepX = 2
        
        self.__length = 5
        self.__fig = np.full(
            (1, self.__length), MAGENTA + '=' + RESET, dtype='<U20')
        # self.__fig = MAGENTA + '=' + RESET
        # self.__lives = 3

    def getPosX(self):
        return self.__x

    def getPosY(self):
        return self.__y
        
    # def updateOldX(self):
    #     self.__oldx = self.__x

    def erasePaddle(self,grid):
        x ,y= self.__x,self.__y
        grid[y,x:x+self.__length] = ' '

    def placePaddle(self, grid, x):
        
        if x < LEFTWALL:
            x = LEFTWALL
        elif x > BOX_WIDTH - self.__length:
            x = BOX_WIDTH - self.__length

        self.__x = x
        grid[self.__y, x:x + self.__length] = self.__fig

    def moveRight(self, grid):
        newX = self.__x+self.__stepX
        self.erasePaddle(grid)
        self.placePaddle(grid,newX)

    def moveLeft(self, grid):
        newX = self.__x-self.__stepX
        self.erasePaddle(grid)
        self.placePaddle(grid,newX)
