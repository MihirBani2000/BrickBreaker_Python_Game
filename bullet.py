from utils import *
from config import *
from thing import Thing

class Bullet(Thing):
    ''' class for the Paddle'''

    def __init__(self, x, y, grid):
        super().__init__(x,y)
        
        self._speedX = 0
        self._speedY = -1

        self._fig = MAGENTA + '^' + RESET
        
        # to store whether the ball is out of screen or not
        self.__outOfScreen = False
        
        grid[y, x] = self._fig

    def isOutOfScreen(self):
        return self.__outOfScreen
    
    def delete(self):
        self.__outOfScreen = True

    def checkCollisionWall(self, x, y):
        if not self.__outOfScreen:
            # top wall collision check
            if y < 1:       
                y = 1
                self._y = y
                self.__outOfScreen = True
                self._speedY = 0
        return x, y

    def checkCollisionBricks(self,grid, x, y, bricks,player,powerups):
        speedY = self._speedY
        tempbricks = []
        for brick in bricks:
            if brick.isActive():
                # conditions for checking the collision of bullet with brick
                brick_flag = False
                bX,bY = brick.getPos()
                bX_len, bY_len = brick.getLength()
                                
                inside_flag = (bX <= x < bX + bX_len) and (bY <= y < bY + bY_len)
                if inside_flag:
                    # bullet going inside the brick
                    speedY = 0
                    self.__outOfScreen = True
                    brick_flag = True

                if brick_flag:
                    if SOUND_EFFECTS:
                        os.system("aplay -q Collision.wav &")
                    break_flag = False
                    # on collision
                    if brick.isRainbow():
                            player.updateScores(HIT_SCORE)
                            newBrick = brick.handleCollide(grid,player,powerups)
                            tempbricks.append(newBrick)
                            # break
                    elif brick.isExploding():
                        break_flag = brick.handleCollide(grid,player,powerups,bricks)
                    else:
                        player.updateScores(HIT_SCORE)
                        break_flag = brick.handleCollide(grid,player,powerups)
                        if break_flag:
                            player.updateScores(BREAK_SCORE)
                
                    if break_flag:
                        spawnPowerups(bX+int(bX_len/2),bY+int(bY_len/2),powerups,self)
        if tempbricks:
            for brick in tempbricks:
                bricks.append(brick)      
        
        self._speedY = speedY
        return x,y

    def move(self, grid,bricks,player,powerups):

        x = self._x
        y = self._y + self._speedY
        self.erase(grid)

        # placing the bullet at the required coordinates after checking collisions
        temp_x,temp_y = self.checkCollisionBricks(grid,x,y,bricks,player,powerups)
        self._x,self._y = self.checkCollisionWall(temp_x,temp_y)

        if not self.__outOfScreen:
            grid[self._y, self._x] = self._fig
        # else:
        #     self.erase(grid)