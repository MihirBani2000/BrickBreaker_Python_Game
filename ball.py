from utils import *
from config import *
from thing import Thing

class Ball(Thing):
    ''' class for the Paddle'''

    def __init__(self, x, y, grid, firstBall=True):
        super().__init__(x,y)
        
        # step length while moving
        self.__speedX = 0
        self.__speedY = 0

        self._fig = BLUE + 'O' + RESET
        
        # to store whether the ball is out of screen or not
        self.__outOfScreen = False
        
        # the ball in the beginning starts at top of the paddle
        if firstBall == True:
            self.__onPaddle = True
            grid[y, x] = self._fig
        else:
            self.__onPaddle = False

    def isOutOfScreen(self):
        return self.__outOfScreen
    
    def isOnPaddle(self):
        return self.__onPaddle

    def setSpeed(self, val):
        if abs(self.__speedX * val) <= MAX_SPEED_X:
            self.__speedX = int(self.__speedX * val)            
        if abs(self.__speedY * val) <= MAX_SPEED_Y:
            self.__speedY = int(self.__speedY * val)            

    def release(self, paddle):
        pX, pL = paddle.getPosX(), paddle.getLength()
        self.__onPaddle = False
        self.__speedY = - 1
        self.__speedX = - int((pX + int(pL / 2) - self._x)/2)

    def checkCollisionWall(self, x, y):
        speedX, speedY = self.__speedX, self.__speedY

        if x < LEFTWALL:   # left wall
            x = LEFTWALL
            self._x = x
            speedX = -speedX

        elif x > BOX_WIDTH - 1:   # right wall
            x = BOX_WIDTH - 1
            self._x = x
            speedX = -speedX

        if y < 1:     # top wall
            y = 1
            self._y = y
            speedY = -speedY

        self.__speedX, self.__speedY = speedX, speedY
        return x, y

    def checkCollisionPaddle(self,grid, x, y, paddle):
        pX = paddle.getPosX()
        pL = paddle.getLength()
        speedX, speedY = self.__speedX, self.__speedY

        if (pX <= x < pX + pL) or (pX <= self._x < pX + pL):
            # within the x coordinates of paddle
            if y > HEIGHT - 3:
                # Colliding with the paddle
                # speedX changed according to the position of contact wrt to the mid of paddle
                delta_speedX = -int((pX + int(pL / 2) - self._x)/2)
                if abs(self.__speedX + delta_speedX) <= MAX_SPEED_X:
                    speedX += delta_speedX
                speedY = -speedY
                y = HEIGHT - 3
                self._y = y

        elif y > HEIGHT - 3:
            # ball crossed the paddle
            self.__outOfScreen = True
            speedX = speedY = 0

        self.__speedX, self.__speedY = speedX, speedY
        # self.__x, self.__y = x, y
        return x,y

    def checkCollisionBricks(self,grid, x, y, bricks,player,powerups):
        speedX, speedY = self.__speedX, self.__speedY
        for brick in bricks:
            if brick.isActive():
                # conditions for checking the collision of ball with brick
                brick_flag = False
                bX,bY = brick.getPos()
                bX_len, bY_len = brick.getLength()
                
                # slope_speed = int(abs(self.__speedY/self.__speedX))

                mean_x = self._x + (self.__speedX)/2
                mean_y = self._y + (self.__speedY)/2
                sec_mean_x = self._x + (self.__speedX)/4
                sec_mean_y = self._y + (self.__speedY)/4
                
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
                    player.updateScores(HIT_SCORE)
                    break_flag = brick.handleCollide(grid,player,powerups)
                    if break_flag:
                        player.updateScores(BREAK_SCORE)
                        spawnPowerups(bX+int(bX_len/2),bY+int(bY_len/2),powerups)
                        
        self.__speedX, self.__speedY = speedX, speedY
        return x,y

    def placeBall(self, grid, x, y, paddle,bricks,player,powerups):

        temp_x,temp_y = self.checkCollisionBricks(grid,x,y,bricks,player,powerups)
        temp1_x,temp1_y = self.checkCollisionWall(temp_x,temp_y)
        self._x,self._y = self.checkCollisionPaddle(grid,temp1_x,temp1_y,paddle)

        if not self.__outOfScreen:
            grid[self._y, self._x] = self._fig
        else:
            self.erase(grid)


    def move(self, grid, paddle,bricks,player,powerups):
        if self.__onPaddle:
            # dont do anything if the ball is on the paddle
            return

        newX = self._x + self.__speedX
        newY = self._y + self.__speedY
        self.erase(grid)

        # placing the ball at the required coordinates after checking collisions
        self.placeBall(grid, newX, newY, paddle,bricks,player,powerups)

    def moveWithPaddle(self, grid, x):
        self.erase(grid)
        self._x = x
        grid[self._y, x] = self._fig
