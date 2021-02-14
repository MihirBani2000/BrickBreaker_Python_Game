from config import *

class Brick():

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.Xlen = 5
        self.Ylen = 1

        self.isActive = True

    def getPos(self):
        return self.x,self.y

    def getLength(self):
        return self.Xlen,self.Ylen

    def eraseBrick(self, grid):
        x, y = self.x, self.y
        grid[y:y+self.Ylen, x:x + self.Xlen] = ' '
        self.isActive = False
        self.x = self.y = 0

    def makeBrick(self,bgcolor):
        fig = np.full( (self.Ylen, self.Xlen), bgcolor + '#' + RESET , dtype='<U20')
        fig[:,0] = bgcolor + '|' + RESET
        fig[:,-1] = bgcolor + '|' + RESET
        return fig
        
    def placeBrick(self, grid, x,y,fig):
        self.x,self.y = x,y
        grid[y:y+self.Ylen, x:x + self.Xlen] = fig

    def checkCollision(self,ball):
        if self.isActive:
            return 
        return 0

# color of the bricks defines the current strength of the brick
# RED = 3
# CYAN = 2
# GREEN = 1

class RedBrick(Brick):
    '''RedBrick class
    red brick is the brick, with red color and strength = 3
    '''
    def __init__(self, grid,x, y):
        super().__init__(x, y)
        self.__maxStren = 3
        self.__currStren = self.__maxStren
        self.__color = Back.RED
        self.__fig = super().makeBrick(self.__color)
        super().placeBrick(grid,x,y,self.__fig)
    
    def ifCollide(self,grid,ball):
        flag = super().checkCollision(ball)

        if flag:

            if self.__maxStren - self.__currStren == 0:
                # first time of collision
                self.__currStren -= 1
                self.__color = Back.CYAN
                self.__fig = super().makeBrick(self.__color)
                super().placeBrick(grid,self.x,self.y,self.__fig)

            elif self.__maxStren - self.__currStren == 1:
                # second time collision
                self.__currStren -= 1
                self.__color = Back.GREEN
                self.__fig = super().makeBrick(self.__color)
                super().placeBrick(grid,self.x,self.y,self.__fig)

            elif self.__maxStren - self.__currStren == 2:
                # third time collision
                self.__currStren = 0
                self.__color = Back.BLACK
                self.eraseBrick(self, grid)
            
    