from config import *

class Thing():

    def __init__(self,x,y):
        self._x = x
        self._y = y

        self._oldx = 0
        self._oldy = 0
        
        self._lengthX = 1
        self._lengthY = 1
        
        self._fig = None

    def getPosX(self):
        return self._x

    def getPosY(self):
        return self._y

    def getLength(self):
        return self._lengthX, self._lengthY

    def erase(self, grid):
        x, y = self._oldx, self._oldy
        grid[y:y+self._lengthY, x:x + self._lengthX] = ' '

    def updateOld(self):
        self._oldx = self._x
        self._oldy = self._y