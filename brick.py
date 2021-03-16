import random
from config import *
from utils import *
from thing import Thing

class Brick(Thing):

    def __init__(self, x=0, y=0):
        super().__init__(x,y)

        self._lengthX = 7
        self._lengthY = 3
        
        self._isActive = True
        self._isVisited = False
        
        self._currStren = 0
        self._maxStren = 0

        # special types
        self._isGold = False
        self._isExplode = False
        self._isRainbow = False
        
        self.spawnPowerups = True
        
    def getPos(self):
        return self._x, self._y

    def getFig(self):
        return self._fig

    def canSpawnPowerups(self):
        return self.spawnPowerups 
    
    def setSpawnPowerups(self,val):
        self.spawnPowerups = val 

    def erase(self, grid,deactivate=True):
        x, y = self._x, self._y
        grid[y:y+self._lengthY, x:x + self._lengthX] = ' '
        if deactivate:
            self._isActive = False

    def makeBrick(self,bgcolor,char = ':'):
        fig = np.full( (self._lengthY, self._lengthX), bgcolor + char + RESET , dtype='<U20')
        fig[:,0] = bgcolor + '[' + RESET
        fig[:,-1] = bgcolor + ']' + RESET
        return fig
        
    def placeBrick(self, grid, x,y, fig):
        self.erase(grid,False)
        if self._isActive:
            self._x,self._y = x,y
            grid[y:y+self._lengthY, x:x + self._lengthX] = fig

    def isActive(self):
        return self._isActive

    def setActive(self,val):
        self._isActive = val

    def isGold(self):
        return self._isGold
    
    def isExploding(self):
        return self._isExplode
    
    def isRainbow(self):
        return self._isRainbow
    
    def isVisited(self):
        return self._isVisited

    def setVisited(self,val):
        self._isVisited = val

    def destroy(self,grid,player):
        # exploding the brick, irrespective of type
        self._currStren = 0
        self._color = Back.BLACK
        self.erase(grid)
        # self._isActive = False
        self._isVisited = False
        player.updateScores(EXPLODE_SCORE)
        # returns true if brick explodes
        return True 

    def getAdjacentNeighbours(self,grid,bricks):
        # get the adjacent neigbours of the current brick
        neighbours = []
        bx, by = self.getPos()
        bx_len,by_len = self.getLength()

        for brick in bricks:
            bx1, by1 = brick.getPos()
            bx1_len,by1_len = brick.getLength()

            if (bx==bx1) and (by==by1):
            # dont check with the same brick
                continue
            
            # all the conditions now
            if (by == by1 + by1_len) or (by1 == by + by_len):
            # the other brick is just above/below the self brick
                if (bx <= bx1 <= bx+bx_len) or (bx <= bx1 + bx1_len <= bx + bx_len): 
                    # if the brick is in contact with self, from top/bottom
                    neighbours.append(brick)
            
            elif (bx == bx1 + bx1_len) or (bx1 == bx + bx_len):
            # the other brick is just left/right of the self brick
                if (by <= by1 <= by+by_len) or (by <= by1 + by1_len <= by + by_len): 
                    # if the brick is in contact with self, from sides
                    neighbours.append(brick)
        return neighbours

    def getAllNeighbours(self,grid,bricks):
        '''marks all the neighbours of all the exploding bricks in a cluster'''
        
        if self.isVisited():
            # if visited already return the function
            return
        self.setVisited(True)

        if not self.isExploding():
            # dont go further if its not an exploding brick
            return

        # get the neighbour of current brick if its exploding
        neighbours = self.getAdjacentNeighbours(grid,bricks)
        if neighbours:
            for brick in neighbours:
                brick.getAllNeighbours(grid,bricks)

    def destroyNeighbours(self,grid,bricks,player):
        if bricks:
            for brick in bricks:
                if brick.isVisited() and brick.isActive():
                    brick.destroy(grid,player)
        return

    def explode(self,grid,player,powerups,bricks):
        self._isExplode = True
        self._currStren = 0
        self._color = Back.BLACK
        self.getAllNeighbours(grid,bricks)
        self.destroyNeighbours(grid,bricks,player)
        return True


# color of the bricks defines the current strength of the brick
# EXPLODING = explodes and also destroys nearby bricks
# GOLD = indestructible
# RED = 3
# CYAN = 2
# GREEN = 1
# RAINBOW = changes between RED, CYAN, GREEN randomly until touched by ball

class RedBrick(Brick):
    '''RedBrick class
    red brick is the brick, with red color and strength = 3
    '''
    def __init__(self, grid,x, y):
        super().__init__(x, y)
        self._maxStren = 3
        self._currStren = self._maxStren
        self._color = Back.RED
        self._fig = super().makeBrick(self._color)
        super().placeBrick(grid,x,y,self._fig)
    
    def handleCollide(self,grid,player,powerups):

        if self._maxStren - self._currStren == 0:
            # first time of collision
            self._currStren -= 1
            self._color = Back.CYAN
            self._fig = super().makeBrick(self._color)
            super().placeBrick(grid,self._x,self._y,self._fig)

        elif self._maxStren - self._currStren == 1:
            # second time collision
            self._currStren -= 1
            self._color = Back.GREEN
            self._fig = super().makeBrick(self._color)
            super().placeBrick(grid,self._x,self._y,self._fig)

        elif self._maxStren - self._currStren == 2:
            # third time collision
            self._currStren = 0
            self._color = Back.BLACK
            self.erase(grid)
            self._isActive = False
            return True # returns true if brick broke

            
class CyanBrick(Brick):
    '''CyanBrick class
    cyan brick is the brick, with cyan color and strength = 2
    '''
    def __init__(self, grid,x, y):
        super().__init__(x, y)
        self._maxStren = 2
        self._currStren = self._maxStren
        self._color = Back.CYAN
        self._fig = super().makeBrick(self._color)
        super().placeBrick(grid,x,y,self._fig)
    
    def handleCollide(self,grid,player,powerups):

        if self._maxStren - self._currStren == 0:
            # first time of collision
            self._currStren -= 1
            self._color = Back.GREEN
            self._fig = super().makeBrick(self._color)
            super().placeBrick(grid,self._x,self._y,self._fig)

        elif self._maxStren - self._currStren == 1:
            # second time collision
            self._currStren = 0
            self._color = Back.BLACK
            self.erase(grid)
            self._isActive = False
            return True # returns true if brick broke

class GreenBrick(Brick):
    '''GreenBrick class
    green brick is the brick, with green color and strength = 1
    '''
    def __init__(self, grid,x, y):
        super().__init__(x, y)
        self._maxStren = 1
        self._currStren = self._maxStren
        self._color = Back.GREEN
        self._fig = super().makeBrick(self._color)
        super().placeBrick(grid,x,y,self._fig)
    
    def handleCollide(self,grid,player,powerups):

        if self._maxStren - self._currStren == 0:
            # first time of collision
            self._currStren = 0
            self._color = Back.BLACK
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
        self._maxStren = 10
        self._currStren = self._maxStren
        self._color = Back.YELLOW + Style.BRIGHT
        self._fig = super().makeBrick(self._color,char='#')
        super().placeBrick(grid,x,y,self._fig)
    
    def handleCollide(self,grid,player,powerups):
        # dont do anything
        return 


class RainbowBrick(Brick):
    '''RainbowBrick class
    rainbow brick changes between Red, Cyan and Green Brick 
    untill collided for the first time
    '''
    def __init__(self, grid,x, y):
        super().__init__(x, y)
        self._isRainbow = True
        self.figs = []
        colors = [Back.GREEN,Back.CYAN,Back.RED]
        for color in colors:
            self._fig = super().makeBrick(color)
            self.figs.append(self._fig)
        self.type = random.randint(0,2)
        self._fig = self.figs[self.type] 
        self.placeBrick(grid,x,y)
    
    def placeBrick(self, grid, x,y, fig=None):
        self.erase(grid,False)
        if self._isActive:
            self._x,self._y = x,y
            self.type = random.randint(0,2)
            self._fig = self.figs[self.type]
            grid[y:y+self._lengthY, x:x + self._lengthX] = self._fig

    def handleCollide(self,grid,player,powerups):
        # first time of collision
        self.erase(grid)
        if self.type == 0:
            newBrick = GreenBrick(grid,self._x,self._y)
        elif self.type == 1:
            newBrick = CyanBrick(grid,self._x,self._y)
        else:
            newBrick = RedBrick(grid,self._x,self._y)

        return newBrick # returns new brick formed if rainbowBrick is collided 


class ExplodingBrick(Brick):
    '''ExplodingBrick class
    Exploding brick is the brick, with White color and explodes on collision
    also explodes the nearby bricks
    '''
    def __init__(self, grid,x, y):
        super().__init__(x, y)
        self._isExplode = True
        self._maxStren = 1
        self._currStren = self._maxStren
        self._color = Back.WHITE + Style.BRIGHT
        self._fig = super().makeBrick(self._color,char = Fore.BLACK + '*')
        super().placeBrick(grid,x,y,self._fig)
    

    def handleCollide(self,grid,player,powerups,bricks):
        if self._maxStren - self._currStren == 0:
            # first time of collision
            self._currStren = 0
            self._color = Back.BLACK
            self.getAllNeighbours(grid,bricks)
            self.destroyNeighbours(grid,bricks,player)
            return True
        return False
    




