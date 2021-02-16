from config import *
from thing import Thing

class Ball(Thing):
    ''' class for the Paddle'''

    def __init__(self, x, y, grid, firstBall=True):
        super().__init__(x,y)
        # self.__x = x
        # self.__y = y

        # self.__oldx = 0
        # self.__oldy = 0

        # step length while moving
        self.__speedX = 0
        self.__speedY = 0

        self._fig = YELLOW + 'O' + RESET
        
        # to store whether the ball is out of screen or not
        self.__outOfScreen = False
        
        # the ball in the beginning starts at top of the paddle
        if firstBall == True:
            self.__onPaddle = True
            grid[y, x] = self._fig
        else:
            self.__onPaddle = False

    # def getPosX(self):
    #     return self.__x

    # def getPosY(self):
    #     return self.__y

    def isOutOfScreen(self):
        return self.__outOfScreen
    
    # def updateOld(self):
    #     self.__oldx = self.__x
    #     self.__oldy = self.__y

    # def erase(self, grid):
    #     grid[self._oldy, self._oldx] = ' '

    def isOnPaddle(self):
        return self.__onPaddle

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
        # self.__x,self.__y = x,y
        return x, y

    def checkCollisionPaddle(self,grid, x, y, paddle):
        pX = paddle.getPosX()
        pL = paddle.getLength()
        speedX, speedY = self.__speedX, self.__speedY

        if pX <= x <= pX + pL:
            # within the x coordinates of paddle
            if y > HEIGHT - 3:
                # Colliding with the paddle
                # speedX changed according to the position of contact wrt to the mid of paddle
                speedX -= int((pX + int(pL / 2) - x)/2)
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

    def checkCollisionBricks(self,grid, x, y, bricks,player):
        speedX, speedY = self.__speedX, self.__speedY
        for brick in bricks:
            if brick.isActive():
                # conditions for checking the collision of ball with brick
                brick_flag = False
                bX,bY = brick.getPos()
                bX_len,bY_len = brick.getLength()


                if (bX <= x <= bX + bX_len) and (bY <= y <= bY + bY_len):
                    # ball going inside the brick
                    
                    if self._y >= bY:
                        # bottom
                        speedY = -speedY
                        y = bY + bY_len + 1
                        brick_flag = True
                    
                    elif self._y <= bY:
                        # top
                        speedY = -speedY
                        y = bY-1
                        brick_flag = True
                    
                    elif self._x <= bX:
                        # left side
                        speedX = -speedX
                        x = bX-1
                        brick_flag = True

                    elif self._x >= bX + bX_len:
                        # right side
                        speedX = -speedX
                        x = bX + bX_len + 1
                        brick_flag = True

                if brick_flag:
                    player.updateScores(HIT_SCORE)
                    brick.handleCollide(grid,player)

        self.__speedX, self.__speedY = speedX, speedY
        # self.__x, self.__y = x, y
        return x,y

    def placeBall(self, grid, x, y, paddle,bricks,player):

        temp_x,temp_y = self.checkCollisionWall(x, y)
        temp_x,temp_y  = self.checkCollisionBricks(grid,temp_x,temp_y,bricks,player)
        self._x,self._y = self.checkCollisionPaddle(grid,temp_x,temp_y,paddle)

        if not self.__outOfScreen:
            grid[self._y, self._x] = self._fig
        else:
            self.updateOld()
            self.erase(grid)


    def move(self, grid, paddle,bricks,player):
        if self.__onPaddle:
            # dont do anything if the ball is on the paddle
            return

        self.updateOld()
        newX = self._x + self.__speedX
        newY = self._y + self.__speedY
        self.erase(grid)

        # placing the ball at the required coordinates after checking collisions
        self.placeBall(grid, newX, newY, paddle,bricks,player)

    def moveWithPaddle(self, grid, x):
        self.updateOld()
        self.erase(grid)
        self._x = x
        grid[self._y, x] = self._fig
