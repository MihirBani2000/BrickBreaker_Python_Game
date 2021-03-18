from utils import *
from config import *
from thing import Thing

class Bullet(Thing):
    ''' class for the Bullet'''

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
                        os.system("aplay -q ./music/Collision.wav &")
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
                
                    if break_flag and brick.canSpawnPowerups():
                        spawnPowerups(bX+int(bX_len/2),bY+int(bY_len/2),powerups,self)
        if tempbricks:
            for brick in tempbricks:
                bricks.append(brick)      
        
        self._speedY = speedY
        return x,y

    def checkCollisionBoss(self,grid, x, y, boss,player,bricks):
        speedY = self._speedY

        # conditions for checking the collision of bullet with boss
        if not boss.isDead():
            bX,bY = boss.getPos()
            bX_len, bY_len = boss.getLength()
                            
            inside_flag = (bX <= x < bX + bX_len) and (bY <= y < bY + bY_len)
            if inside_flag:
                # bullet going inside the boss
                speedY = 0
                self.__outOfScreen = True
                boss.handleCollide(grid,player,bricks)            
              
        self._speedY = speedY
        return x,y

    def move(self, grid,bricks,player,powerups,boss=None):

        x = self._x
        y = self._y + self._speedY
        self.erase(grid)

        # placing the bullet at the required coordinates after checking collisions
        if boss != None:
            x,y = self.checkCollisionBoss(grid,x,y,boss,player,bricks)
        temp_x,temp_y = self.checkCollisionBricks(grid,x,y,bricks,player,powerups)
        self._x,self._y = self.checkCollisionWall(temp_x,temp_y)

        if not self.__outOfScreen:
            grid[self._y, self._x] = self._fig
        

# class for Bombs, dropped by boss in final level
class Bomb(Thing):
    ''' class for the Bombs'''

    def __init__(self, x, y, grid):
        super().__init__(x,y)
        
        self._speedX = 0
        self._speedY = 1

        self._fig = Back.YELLOW  + '#' + RESET
        
        # to store whether the bomb isaaaaaaaaaddd out of screen or not
        self.__outOfScreen = False
        
        grid[y, x] = self._fig

    def isOutOfScreen(self):
        return self.__outOfScreen
    
    def delete(self):
        self.__outOfScreen = True


    def checkCollisionPaddle(self,grid, x, y, paddle,player):
        pX = paddle.getPosX()
        pL = paddle.getLength()
        speedX, speedY = self._speedX, self._speedY

        if y > HEIGHT - 3:
        # if y coord lower than paddle
            self.__outOfScreen = True
            speedX = speedY = 0
            if (pX <= x < pX + pL) or (pX <= self._x < pX + pL):
            # within the x coordinates of paddle
            # Colliding with the paddle
                if SOUND_EFFECTS:
                    os.system("aplay -q ./music/Collision.wav &")
                    
                y = HEIGHT - 3
                player.reduceLife()

        self._speedX, self._speedY = speedX, speedY
        return x,y

    def move(self, grid,paddle, player):

        x = self._x
        y = self._y + self._speedY
        self.erase(grid)

        # placing the bomb at the required coordinates after checking collisions
        self._x,self._y = self.checkCollisionPaddle(grid,x,y,paddle,player)

        if not self.__outOfScreen:
            grid[self._y, self._x] = self._fig