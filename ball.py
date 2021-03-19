from brick import Brick
from utils import *
from config import *
from thing import Thing

class Ball(Thing):
    ''' class for the Paddle'''

    def __init__(self, x, y, grid, onPaddle=True):
        super().__init__(x,y)
        
        self._speedX = 0
        self._speedY = 0

        self._fig = BLUE + 'O' + RESET
        
        # to store whether the ball is out of screen or not
        self.__outOfScreen = False

        # for the powerup of grabbing ball to paddle
        self.__isSticky = False     
        self.__paddleOffset = 0   

        # for thru ball powerup
        self.__isThru = False     

        # for fire ball powerup
        self.__isFire = False     

        # the ball in the beginning starts at top of the paddle
        self.__onPaddle = onPaddle
        # if onPaddle == True:
        grid[y, x] = self._fig

    def isOutOfScreen(self):
        return self.__outOfScreen
    
    def isOnPaddle(self):
        return self.__onPaddle

    def setOnPaddle(self,val):
        self.__onPaddle = val

    def isSticky(self):
        return self.__isSticky
    
    def setSticky(self,val):
        self.__isSticky = val

    def isThru(self):
        return self.__isThru
    
    def setThru(self,val):
        self.__isThru = val

    def isFire(self):
        return self.__isFire
    
    def setFire(self,val):
        self.__isFire = val

    def setPaddleOffset(self,val):
        self.__paddleOffset = val

    def setPos(self,x,y):
        self._x = x
        self._y = y

    def setSpeed(self, val,val2=None, multiply=True):
        if multiply:
            if abs(self._speedX * val) <= MAX_SPEED_X:
                self._speedX = int(self._speedX * val)            
            if abs(self._speedY * val) <= MAX_SPEED_Y:
                self._speedY = int(self._speedY * val)            
        else:
            self._speedX = val
            self._speedY = val2            

    def release(self, paddle):
        pX, pL = paddle.getPosX(), paddle.getLength()
        self.__onPaddle = False
        self._speedY = - 1
        self._speedX = - int((pX + int(pL / 2) - self._x)/2)

    def checkCollisionPaddle(self,grid, x, y, paddle,bricks,player,falling_flag=False):
        pX = paddle.getPosX()
        pL = paddle.getLength()
        speedX, speedY = self._speedX, self._speedY

        if (pX <= x < pX + pL) or (pX <= self._x < pX + pL):
            # within the x coordinates of paddle
            if y > HEIGHT - 3:
                # Colliding with the paddle
                # if the ball is not sticky, then only change the velocity, otherwise make it zero.
                if SOUND_EFFECTS:
                    os.system("aplay -q ./music/Collision.wav &")
                if self.isSticky():
                    speedY = 0
                    speedX = 0
                    self.setOnPaddle(True)
                    x = int((self._x + x)/2)
                    self.setPaddleOffset(x - pX)
                else:
                    # speedX changed according to the position of contact wrt to the mid of paddle
                    delta_speedX = -int( (pX + int(pL / 2) - self._x)/2)
                    if abs(self._speedX + delta_speedX) <= MAX_SPEED_X:
                        speedX += delta_speedX               
                    speedY = -speedY
                    
                # Falling bricks if the ball hits the paddle, after a fixed time
                if falling_flag:
                    step = 1
                    printBricks(grid,bricks,player,paddle,step) 

                y = HEIGHT - 3

        elif y > HEIGHT - 3:
            # ball crossed the paddle
            self.__outOfScreen = True
            speedX = speedY = 0

        self._speedX, self._speedY = speedX, speedY
        return x,y

    def checkCollisionBricks(self,grid, x, y, bricks,player,powerups):
        speedX, speedY = self._speedX, self._speedY

        # storing a copy of x,y for thru ball
        tempx, tempy = x,y
        tempbricks = []
        for brick in bricks:
            if brick.isActive():
                # conditions for checking the collision of ball with brick
                brick_flag = False
                bX,bY = brick.getPos()
                bX_len, bY_len = brick.getLength()
                
                mean_x = self._x + (self._speedX)/2
                mean_y = self._y + (self._speedY)/2
                sec_mean_x = self._x + (self._speedX)/4
                sec_mean_y = self._y + (self._speedY)/4
                
                inside_flag = (bX <= x < bX + bX_len) and (bY <= y < bY + bY_len)
                mean_inside_flag = (bX <= mean_x < bX + bX_len) and (bY <= mean_y < bY + bY_len)
                sec_mean_inside_flag = (bX <= sec_mean_x < bX + bX_len) and (bY <= sec_mean_y < bY + bY_len)

                if inside_flag or mean_inside_flag or sec_mean_inside_flag:
                    # ball going inside the brick

                    if bY - 1 <= self._y <= bY + bY_len:
                        if (self._x < bX) and (grid[bY,bX-1] == ' ' or grid[bY,bX-1] == self._fig):
                            # left side
                            speedX = -speedX
                            x = bX-1
                            y = int(mean_y)
                            brick_flag = True

                        elif (self._x >= bX + bX_len) and (grid[bY,bX+bX_len] == ' ' or grid[bY,bX+bX_len] == self._fig):
                            # right side
                            speedX = -speedX
                            x = bX + bX_len
                            y = int(mean_y)
                            brick_flag = True

                    if not brick_flag and (bX-1 <= self._x <= bX + bX_len + 1):
                        if self._y >= bY+bY_len:
                            # bottom
                            speedY = -speedY
                            y = bY + bY_len
                            x = int(mean_x)
                            brick_flag = True
                        
                        elif self._y <= bY:
                            # top
                            speedY = -speedY
                            y = bY-1
                            x = int(mean_x)
                            brick_flag = True

                if brick_flag:
                    if SOUND_EFFECTS:
                        os.system("aplay -q ./music/Collision.wav &")
                    break_flag = False
                    # on collision
                    if self.isThru():
                        # if thru ball
                        if brick.isExploding():
                            break_flag = brick.handleCollide(grid,player,powerups,bricks)
                        else:
                            break_flag = brick.destroy(grid,player)
                    if self.isFire():
                        # if fire ball
                        if brick.isExploding():
                            break_flag = brick.handleCollide(grid,player,powerups,bricks)
                        else:
                            break_flag = brick.explode(grid,player,powerups,bricks)
                    else:
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
        
        if self.isThru():
            x,y = tempx,tempy
        else:
            self._speedX, self._speedY = speedX, speedY
        return x,y

    def checkCollisionBoss(self,grid, x, y, boss, bricks,player):
        speedX, speedY = self._speedX, self._speedY

        if not boss.isDead():
            # conditions for checking the collision of ball with boss
            boss_flag = False
            bX,bY = boss.getPos()
            bX_len, bY_len = boss.getLength()
            
            mean_x = self._x + (self._speedX)/2
            mean_y = self._y + (self._speedY)/2
            sec_mean_x = self._x + (self._speedX)/4
            sec_mean_y = self._y + (self._speedY)/4
            
            inside_flag = (bX <= x < bX + bX_len) and (bY <= y < bY + bY_len)
            mean_inside_flag = (bX <= mean_x < bX + bX_len) and (bY <= mean_y < bY + bY_len)
            sec_mean_inside_flag = (bX <= sec_mean_x < bX + bX_len) and (bY <= sec_mean_y < bY + bY_len)

            if inside_flag or mean_inside_flag or sec_mean_inside_flag:
                # ball going inside the boss

                if bY - 1 <= self._y <= bY + bY_len:
                    if (self._x < bX) and (grid[bY,bX-1] == ' ' or grid[bY,bX-1] == self._fig):
                        # left side
                        speedX = -speedX
                        x = bX-1
                        y = int(mean_y)
                        boss_flag = True

                    elif (self._x >= bX + bX_len) and (grid[bY,bX+bX_len] == ' ' or grid[bY,bX+bX_len] == self._fig):
                        # right side
                        speedX = -speedX
                        x = bX + bX_len
                        y = int(mean_y)
                        boss_flag = True

                if not boss_flag and (bX-1 <= self._x <= bX + bX_len + 1):
                    if self._y >= bY+bY_len:
                        # bottom
                        speedY = -speedY
                        y = bY + bY_len
                        x = int(mean_x)
                        boss_flag = True
                    
                    elif self._y <= bY:
                        # top
                        speedY = -speedY
                        y = bY-1
                        x = int(mean_x)
                        boss_flag = True

            if boss_flag:
                if SOUND_EFFECTS:
                    os.system("aplay -q ./music/Collision.wav &")
                boss.handleCollide(grid,player,bricks)
            
        self._speedX, self._speedY = speedX, speedY
        
        return x,y

    def placeBall(self, grid, x, y, paddle,bricks,player,powerups,boss=None,falling_flag=False):

        if boss!=None:
            x,y = self.checkCollisionBoss(grid,x,y,boss,bricks,player)
        temp_x,temp_y = self.checkCollisionBricks(grid,x,y,bricks,player,powerups)
        temp1_x,temp1_y = self.checkCollisionWall(temp_x,temp_y)
        self._x,self._y = self.checkCollisionPaddle(grid,temp1_x,temp1_y,paddle,bricks,player,falling_flag)

        if not self.__outOfScreen:
            grid[self._y, self._x] = self._fig
        else:
            self.erase(grid)

    def moveWithPaddle(self, grid, x):
        self.erase(grid)
        self._x = x
        grid[self._y, x] = self._fig

    def move(self, grid, paddle,bricks,player,powerups,boss=None,falling_flag=False):

        if self.__onPaddle:
            # if the brick is on the paddle, grabbed, or in startup
            newx = paddle.getPosX() + self.__paddleOffset
            self.moveWithPaddle(grid,newx)
            return

        newX = self._x + self._speedX
        newY = self._y + self._speedY
        self.erase(grid)

        # placing the ball at the required coordinates after checking collisions
        self.placeBall(grid, newX, newY, paddle,bricks,player,powerups,boss,falling_flag)

    def split(self,grid,paddle):
        onPaddle = self.isOnPaddle()
        if not onPaddle:
            if SOUND_EFFECTS:
                os.system("aplay -q ./music/Blink.wav &")
            newball = Ball(self._x,self._y,grid,onPaddle)
            self._speedX = int(self._speedX/2)
            if self._speedX == 0:
                self._speedX = 1
            newball.setSpeed(-self._speedX,self._speedY,False)
        else:
            pX = paddle.getPosX()
            pL = paddle.getLength() 
            bX = self._x
            x = bX+1
            if bX == pX + pL - 1:
                x = bX-1
            newball = Ball(x, self._y, grid, onPaddle)
        return newball