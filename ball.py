from config import *


class Ball():
    ''' class for the Paddle'''

    def __init__(self, x, y, grid, firstBall=True):
        self.__x = x
        self.__y = y

        self.__oldx = 0
        self.__oldy = 0

        # step length while moving
        self.__speedX = 0
        self.__speedY = 0

        self.__fig = YELLOW + 'O' + RESET

        # the ball in the beginning starts at top of the paddle
        if firstBall == True:
            self.__onPaddle = True
            grid[y, x] = self.__fig
        else:
            self.__onPaddle = False

    def getPosX(self):
        return self.__x

    def getPosY(self):
        return self.__y

    def updateOld(self):
        self.__oldx = self.__x
        self.__oldy = self.__y

    def eraseBall(self, grid):
        grid[self.__oldy, self.__oldx] = ' '

    def isOnPaddle(self):
        return self.__onPaddle

    def release(self, paddle):
        pX, pL = paddle.getPosX(), paddle.getLength()
        self.__onPaddle = False
        self.__speedY = -1
        self.__speedX = -(pX + int(pL / 2) - self.__x)

    def checkCollisionWall(self, x, y):
        speedX, speedY = self.__speedX, self.__speedY

        if x < LEFTWALL:
            # left wall
            x = LEFTWALL
            self.__x = x
            speedX = -speedX

        elif x > BOX_WIDTH - 1:
            # right wall
            x = BOX_WIDTH - 1
            self.__x = x
            speedX = -speedX

        if y < 1:
            # top wall
            y = 1
            self.__y = y
            speedY = -speedY

        self.__speedX, self.__speedY = speedX, speedY
        return x,y

    def checkCollisionPaddle(self,x, y, paddle):
        pX = paddle.getPosX()
        pL = paddle.getLength()
        # x, y = self.__x, self.__y
        speedX, speedY = self.__speedX, self.__speedY

        if pX <= x <= pX + pL - 1:
            # within the paddle x coordinates
            if y > HEIGHT - 3:
                # Colliding with the paddle
                # speedX changed according to the position of contact wrt to
                # the mid of paddle
                speedX -= (pX + int(pL / 2) - x)
                # speedX -= int((pX + (pL / 2) - x)/1.5)
                speedY = -speedY
                y = HEIGHT - 3
                self.__y = y

        elif y > HEIGHT - 3:
            print("ball down")
            # ball crossed the paddle
            # life lost

        self.__speedX, self.__speedY = speedX, speedY
        # self.__x, self.__y = x, y
        return x,y

    def placeBall(self, grid, x, y, paddle):

        # x,y = self.checkCollisionWall(x, y)
        # x,y = self.checkCollisionPaddle(x,y,paddle)

        grid[y, x] = self.__fig

    def move(self, grid, paddle):
        if self.__onPaddle:
            # dont do anything if the ball is on the paddle
            return
        self.updateOld()
        newX = self.__x + self.__speedX
        newY = self.__y + self.__speedY
        self.eraseBall(grid)
        self.placeBall(grid, newX, newY, paddle)
        # showmessage("Quit")

    def moveWithPaddle(self, grid, x):
        self.updateOld()
        self.eraseBall(grid)
        self.__x = x
        grid[self.__y, x] = self.__fig
