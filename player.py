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

    def isGameOver(self):
        return self.__gameOver
    
    def GameOver(self,msg):
        self.__gameOver = True
        self.showmessage(msg)


    def reduceLife(self):
        '''reduces the life of the player and sets the GameOver attribute True if lives over'''
        if self.__lives > 0:
            self.__lives -= 1
            self.updateScores(LIFE_PENALTY)
        else:
            # showmessage(LIVES_OVER, self)
            self.GameOver(LIVES_OVER)
    
    def showStats(self):
        print( Back.RED + Fore.WHITE + Style.BRIGHT +"B R I C K B R E A K E R".center(WIDTH) + RESET)
        print(Back.WHITE + Fore.RED + Style.BRIGHT +''.center(WIDTH) + RESET)
        print(Back.RED + Fore.WHITE + Style.BRIGHT +"Lives Left: {}         Score: {}         Time left: {} ".format(self.getLives(),self.getScores(),self.getTimer()).center(WIDTH) + RESET )
        

    def showmessage(self,msg):
        """Displays the message according to the condition, at end of game"""

        os.system('clear')

        print("\n\n")
        if msg == TIME_OVER:
            print(Fore.RED + 
                "\t\t\t _______  ___   __   __  _______    __   __  _______\n" +
                "\t\t\t|       ||   | |  |_|  ||       |  |  | |  ||       |\n" +
                "\t\t\t|_     _||   | |       ||    ___|  |  | |  ||    _  |\n" +
                "\t\t\t  |   |  |   | |       ||   |___   |  |_|  ||   |_| |\n" +
                "\t\t\t  |   |  |   | |       ||    ___|  |       ||    ___|\n" +
                "\t\t\t  |   |  |   | | ||_|| ||   |___   |       ||   |\n" +
                "\t\t\t  |___|  |___| |_|   |_||_______|  |_______||___|\n" + RESET)

        elif msg == VICTORY:
            print(Fore.GREEN + 
                "\t\t\t __   __  ___   _______  _______  _______  ______    __   __\n" +
                "\t\t\t|  | |  ||   | |       ||       ||       ||    _ |  |  | |  |\n" +
                "\t\t\t|  |_|  ||   | |      _||_     _||   _   ||   | ||  |  |_|  |\n" +
                "\t\t\t|       ||   | |     |    |   |  |  | |  ||   |_||_ |       |\n" +
                "\t\t\t|       ||   | |     |    |   |  |  |_|  ||    __  ||_     _|\n" +
                "\t\t\t |     | |   | |     |_   |   |  |       ||   |  | |  |   |\n" +
                "\t\t\t  |___|  |___| |_______|  |___|  |_______||___|  |_|  |___|\n" + RESET)

        elif msg == LIVES_OVER:
            print(Fore.RED + 
                "\t\t\t _______  _______  __   __  _______    _______  __   __  _______  ______\n" +
                "\t\t\t|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |\n" +
                "\t\t\t|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||\n" +
                "\t\t\t|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_\n" +
                "\t\t\t|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |\n" +
                "\t\t\t|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |\n" +
                "\t\t\t|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n" + RESET)

        elif msg == QUIT:
            print(Fore.MAGENTA +
                "\t\t\t __   __  _______  __   __    _______  __   __  ___   _______ \n" +
                "\t\t\t|  | |  ||       ||  | |  |  |       ||  | |  ||   | |       |\n" +
                "\t\t\t|  |_|  ||   _   ||  | |  |  |   _   ||  | |  ||   | |_     _|\n" +
                "\t\t\t|       ||  | |  ||  |_|  |  |  | |  ||  |_|  ||   |   |   |  \n" +
                "\t\t\t|_     _||  |_|  ||       |  |  |_|  ||       ||   |   |   |  \n" +
                "\t\t\t  |   |  |       ||       |  |      | |       ||   |   |   |  \n" +
                "\t\t\t  |___|  |_______||_______|  |____||_||_______||___|   |___|  \n" + RESET)

        print("\n")
        print("\t\t\t\t\tHope you had a nice time!!!")
        print("\n")
        print("\t\t\t\t\tScore: {}".format(self.getScores()))
        print("\n\n")
