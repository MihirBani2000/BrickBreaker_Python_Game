from config import *
from utils import *
from thing import Thing

class Brick(Thing):

    def __init__(self, x=0, y=0):
        super().__init__(x,y)

        self._lengthX = 7
        self._lengthY = 3
        
        self._isActive = True
        self._isGold = False
        self._isExplode = False
        self._isVisited = False
        
    def getPos(self):
        return self._x, self._y

    def getFig(self):
        return self._fig

    def erase(self, grid):
        x, y = self._x, self._y
        grid[y:y+self._lengthY, x:x + self._lengthX] = ' '
        self._isActive = False

    def makeBrick(self,bgcolor,char = ':'):
        fig = np.full( (self._lengthY, self._lengthX), bgcolor + char + RESET , dtype='<U20')
        fig[:,0] = bgcolor + '[' + RESET
        fig[:,-1] = bgcolor + ']' + RESET
        return fig
        
    def placeBrick(self, grid, x,y, fig):
        if self._isActive:
            self._x,self._y = x,y
            grid[y:y+self._lengthY, x:x + self._lengthX] = fig

    def isActive(self):
        return self._isActive

    def setActive(self,val):
        self._isActive = val

    def isGold(self):
        return self._isGold
    
    def isExplode(self):
        return self._isExplode
    
    def isVisited(self):
        return self._isVisited

    def setVisited(self,val):
        self._isVisited = val

# color of the bricks defines the current strength of the brick
# EXPLODING = explodes and also destroys nearby bricks
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
    
    def handleCollide(self,grid,player,powerups):

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
            self.__currStren = 0
            self.__color = Back.BLACK
            self.erase(grid)
            self._isActive = False
            return True # returns true if brick broke

            
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
    
    def handleCollide(self,grid,player,powerups):

        if self.__maxStren - self.__currStren == 0:
            # first time of collision
            self.__currStren -= 1
            self.__color = Back.GREEN
            self._fig = super().makeBrick(self.__color)
            super().placeBrick(grid,self._x,self._y,self._fig)

        elif self.__maxStren - self.__currStren == 1:
            # second time collision
            self.__currStren = 0
            self.__color = Back.BLACK
            self.erase(grid)
            self._isActive = False
            return True # returns true if brick broke

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
    
    def handleCollide(self,grid,player,powerups):

        if self.__maxStren - self.__currStren == 0:
            # first time of collision
            self.__currStren = 0
            self.__color = Back.BLACK
            self.erase(grid)
            self._isActive = False
            return True # returns true if brick broke
    

class GoldBrick(Brick):
    '''GoldBrick class
    Gold brick is the brick, with Gold(Yellow) color and strength = inf
    '''
    def __init__(self, grid,x, y):
        super().__init__(x, y)
        self._isGold = True
        self.__maxStren = 10
        self.__currStren = self.__maxStren
        self.__color = Back.YELLOW + Style.BRIGHT
        self._fig = super().makeBrick(self.__color,char='#')
        super().placeBrick(grid,x,y,self._fig)
    
    def handleCollide(self,grid,player,powerups):
        # dont do anything until the powerup "Thru ball" is not activated
        return 
        # if self.__maxStren - self.__currStren == 0:
        #     # first time of collision
        #     self.__currStren = 0
        #     self.__color = Back.BLACK
        #     self.erase(grid)

class ExplodingBrick(Brick):
    '''ExplodingBrick class
    Exploding brick is the brick, with White color and explodes on collision
    also explodes the nearby bricks
    '''
    def __init__(self, grid,x, y):
        super().__init__(x, y)
        self._isExplode = True
        self.__maxStren = 1
        self.__currStren = self.__maxStren
        self.__color = Back.WHITE + Style.BRIGHT
        self._fig = super().makeBrick(self.__color,char='*')
        super().placeBrick(grid,x,y,self._fig)
    
    def checkBoundary(self,brick1,brick2):
        '''if self and brick are in contact, return True, otherwise False'''
        return False

    def checkNeighbours(self,grid,bricks):
        '''checks all the nearby bricks of an exploding brick'''
        explodingBricks = []
        explodingBricks.append(self)
        self.setVisited(True)
        for brick in bricks:
            '''check the nearby bricks to the current brick
                if not visited, and exploding, push it to list, recursive call on the list
                if not visited, and normal, set the visited
                if visited, ignore
            '''
            if brick.isVisited():
                continue
            elif brick.isExploding():
                pass
            else:
                pass
        return

    def destroyNeighbours(self,grid,bricks):
        if bricks:
            for brick in bricks:
                if brick.isVisited() and brick.isActive():
                    brick.erase(grid)
                    brick.setActive(False)
        return

    def handleCollide(self,grid,player,powerups,bricks):
        
        if self.__maxStren - self.__currStren == 0:
            # first time of collision
            self.__currStren = 0
            self.__color = Back.BLACK
            self.erase(grid)
            self.checkNeighbours(grid,bricks)
            self.destroyNeighbours(grid,bricks)
            return True
        return False

    
