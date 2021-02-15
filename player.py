from config import *
from utils import *
import time

class Player():

    def __init__(self):
        self.__lives = MAX_LIVES
        self.__scores = 0
        self.__timer = GAME_TIME
        self.__gameOver = False

    def getLives(self):
        return self.__lives

    def getScores(self):
        return self.__scores

    def updateScores(self,val):
        self.__scores += val
    
    def getTimer(self):
        return self.__timer
    
    def setTimer(self):
        self.__timer -= 1
        return self.__timer

    def isGameOver(self):
        return self.__gameOver
    
    def GameOver(self):
        self.__gameOver = True

    def reduceLife(self):
        '''reduces the life of the player and sets the GameOver attribute True if lives over'''
        if self.__lives > 0:
            self.__lives -= 1
            self.updateScores(LIFE_PENALTY)
        else:
            showmessage(LIVES_OVER, self)
            self.GameOver()
    
    def showStats(self):
        print( Back.RED + Fore.WHITE + Style.BRIGHT +"B R I C K B R E A K E R".center(WIDTH) + RESET)
        print(Back.WHITE + Fore.RED + Style.BRIGHT +''.center(WIDTH) + RESET)
        print(Back.RED + Fore.WHITE + Style.BRIGHT +"Lives Left: {}         Score: {}         Time left: {} ".format(self.getLives(),self.getScores(),self.getTimer()).center(WIDTH) + RESET )
        