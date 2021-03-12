from config import *


class Thing():

    def __init__(self, x, y):
        self._x = x
        self._y = y

        self._speedX = 0
        self._speedY = 0

        self._oldx = 0
        self._oldy = 0

        self._lengthX = 1
        self._lengthY = 1

        self._fig = None

    def getPosX(self):
        return self._x

    def getSpeed(self):
        return self._speedX, self._speedY

    def getPosY(self):
        return self._y

    def getLength(self):
        return self._lengthX, self._lengthY

    def updateOld(self):
        self._oldx = self._x
        self._oldy = self._y

    def erase(self, grid):
        self.updateOld()
        x, y = int(self._oldx), int(self._oldy)
        grid[y:y + self._lengthY, x:x + self._lengthX] = ' '
    
    def checkCollisionWall(self, x, y):
        speedX, speedY = self._speedX, self._speedY

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

        self._speedX, self._speedY = speedX, speedY
        return x, y
