from config import *
from thing import *
from weapon import *
from brick import *

class Boss(Thing):
    ''' class for the Boss'''

    def __init__(self, x, y):
        super().__init__(x,y)
    
        # step length while moving
        self._stepX = 3

        self._lengthX = 11
        self._lengthY = 2

        self._health = 5
        self._dead = False

        self._fig = np.full(
            (self._lengthY, self._lengthX), YELLOW + '=' + RESET, dtype='<U20')

    def getHealth(self):
        return self._health
    
    def isDead(self):
        return self._dead
            
    def spawnBricks(self,grid,y,bricks,type):
        br_xlen,br_ylen = bricks[0].getLength()

        for i in range(1,20):
            if type == 'green':
                brick = GreenBrick(grid, i * (br_xlen)+1, y)
            elif type=='cyan':
                brick = CyanBrick(grid, i * (br_xlen)+1, y)
            elif type=='red':
                brick = RedBrick(grid, i * (br_xlen)+1, y)
            
            brick.setSpawnPowerups(False)
            bricks.append(brick)

    def handleCollide(self,grid,player,bricks):
        if SOUND_EFFECTS:
            os.system("aplay -q Collision.wav &")

        # reducing the health on collision
        if not self._dead:
            self._health -= 1
            if self._health > 0:
                player.updateScores(BOSS_HIT_SCORE)

                if self._health == 3:
                    self.spawnBricks(grid,6,bricks,'green')
                    # pass
                elif self._health == 2:
                    self.spawnBricks(grid,3,bricks,'cyan')
                    # pass
            else:
                player.updateScores(BOSS_BREAK_SCORE)
                self._dead = True

    def placeBoss(self, grid, x):

        if x < LEFTWALL:
            x = LEFTWALL
        elif x > BOX_WIDTH - self._lengthX:
            x = BOX_WIDTH - self._lengthX

        self._x = x
        if not self._dead:
            grid[self._y: self._y + self._lengthY, self._x: self._x + self._lengthX] = self._fig
        else:
            grid[self._y: self._y + self._lengthY, self._x: self._x + self._lengthX] = " "
    
    def moveRight(self, grid):
        newX = self._x + self._stepX
        self.erase(grid)
        self.placeBoss(grid, newX)

    def moveLeft(self, grid):
        newX = self._x - self._stepX
        self.erase(grid)
        self.placeBoss(grid, newX)

    def dropBombs(self,grid,bombs):
        if not self._dead:
            x1 = self._x + self._lengthX//2
            y1 = self._y + self._lengthY 
            bomb = Bomb(x1,y1, grid)
            bombs.append(bomb)