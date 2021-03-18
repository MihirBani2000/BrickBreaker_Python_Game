from config import *
from thing import *
from weapon import *

class Paddle(Thing):
    ''' class for the Paddle'''

    def __init__(self, x, y):
        super().__init__(x,y)
    
        # step length while moving
        self._stepX = 3

        self._lengthX = 11
        
        # shooting powerup
        self._isShooting = False

        self._fig = np.full(
            (1, self._lengthX), MAGENTA + '=' + RESET, dtype='<U20')

    def getLength(self):
        return self._lengthX

    def isShooting(self):
        return self._isShooting

    def setShooting(self,val,grid):
        self._isShooting = val
        self.changeFig(val,grid)

    def getFig(self,fig):
        return self._fig

    def changeFig(self, shoot,grid):
        if shoot:
            fig = np.full((1, self._lengthX), MAGENTA + '=' + RESET, dtype='<U20')
            fig[0,0] = YELLOW + '^' + RESET
            fig[0,-1] = YELLOW + '^' + RESET
            self._fig = fig
        else:
            self._fig = np.full(
            (1, self._lengthX), MAGENTA + '=' + RESET, dtype='<U20')
        self.placePaddle(grid,self._x)

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

    def shootBullets(self,grid,bullets):
        x1, y1 = self._x, self._y 
        pL = self._lengthX
        x2 = x1 + pL - 1
        bullet1 = Bullet(x1,y1-1, grid)
        bullets.append(bullet1)
        bullet2 = Bullet(x2,y1-1, grid)
        bullets.append(bullet2)
        if SOUND_EFFECTS:
            os.system("aplay -q ./music/Bullet.wav &")

