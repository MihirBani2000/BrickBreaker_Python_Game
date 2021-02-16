from config import *
from thing import Thing

class Brick(Thing):

    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        # self._x = x
        # self._y = y

        self._lengthX = 5
        self._lengthY = 2
        
        self._isActive = True
        
    def getPos(self):
        return self._x, self._y

    # def getLength(self):
    #     return self._lengthX,self._lengthY

    def erase(self, grid):
        x, y = self._x, self._y
        grid[y:y+self._lengthY, x:x + self._lengthX] = ' '
        self._isActive = False
        self._x = self._y = 0

    def makeBrick(self,bgcolor):
        fig = np.full( (self._lengthY, self._lengthX), bgcolor + '#' + RESET , dtype='<U20')
        fig[:,0] = bgcolor + '[' + RESET
        fig[:,-1] = bgcolor + ']' + RESET
        return fig
        
    def placeBrick(self, grid, x,y, fig):
        self._x,self._y = x,y
        grid[y:y+self._lengthY, x:x + self._lengthX] = fig

    def isActive(self):
        return self._isActive

# color of the bricks defines the current strength of the brick
# GOLD = indestructible
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
        self._fig = super().makeBrick(self.__color)
        super().placeBrick(grid,x,y,self._fig)
    
    def handleCollide(self,grid,player):

        if self.__maxStren - self.__currStren == 0:
            # first time of collision
            self.__currStren -= 1
            self.__color = Back.CYAN
            self._fig = super().makeBrick(self.__color)
            super().placeBrick(grid,self._x,self._y,self._fig)

        elif self.__maxStren - self.__currStren == 1:
            # second time collision
            self.__currStren -= 1
            self.__color = Back.GREEN
            self._fig = super().makeBrick(self.__color)
            super().placeBrick(grid,self._x,self._y,self._fig)

        elif self.__maxStren - self.__currStren == 2:
            # third time collision
            player.updateScores(BREAK_SCORE)
            self.__currStren = 0
            self.__color = Back.BLACK
            self.erase(grid)
            
class CyanBrick(Brick):
    '''CyanBrick class
    cyan brick is the brick, with cyan color and strength = 2
    '''
    def __init__(self, grid,x, y):
        super().__init__(x, y)
        self.__maxStren = 2
        self.__currStren = self.__maxStren
        self.__color = Back.CYAN
        self._fig = super().makeBrick(self.__color)
        super().placeBrick(grid,x,y,self._fig)
    
    def handleCollide(self,grid,player):

        if self.__maxStren - self.__currStren == 0:
            # first time of collision
            self.__currStren -= 1
            self.__color = Back.GREEN
            self._fig = super().makeBrick(self.__color)
            super().placeBrick(grid,self._x,self._y,self._fig)

        elif self.__maxStren - self.__currStren == 1:
            # second time collision
            player.updateScores(BREAK_SCORE)
            self.__currStren = 0
            self.__color = Back.BLACK
            self.erase(grid)
    

class GreenBrick(Brick):
    '''GreenBrick class
    green brick is the brick, with green color and strength = 1
    '''
    def __init__(self, grid,x, y):
        super().__init__(x, y)
        self.__maxStren = 1
        self.__currStren = self.__maxStren
        self.__color = Back.GREEN
        self._fig = super().makeBrick(self.__color)
        super().placeBrick(grid,x,y,self._fig)
    
    def handleCollide(self,grid,player):

        if self.__maxStren - self.__currStren == 0:
            # first time of collision
            player.updateScores(BREAK_SCORE)
            self.__currStren = 0
            self.__color = Back.BLACK
            self.erase(grid)
    

class GoldBrick(Brick):
    '''GoldBrick class
    Gold brick is the brick, with Gold(Yellow) color and strength = inf
    '''
    def __init__(self, grid,x, y):
        super().__init__(x, y)
        self.__maxStren = 10
        self.__currStren = self.__maxStren
        self.__color = Back.YELLOW
        self._fig = super().makeBrick(self.__color)
        super().placeBrick(grid,x,y,self._fig)
    
    def handleCollide(self,grid):
        # dont do anything if the powerup "Thru ball" is not activated
        return 
        # if self.__maxStren - self.__currStren == 0:
        #     # first time of collision
        #     self.__currStren = 0
        #     self.__color = Back.BLACK
        #     self.erase(grid)
    