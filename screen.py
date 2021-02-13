from config import *


class Screen:
    '''The screen for the game, in the form of a matrix of characters'''

    def __init__(self, rows, columns):
        '''Constructor for the grid'''
        self.__rows = rows
        self.__columns = columns
        self.__grid = np.full((self.__rows, self.__columns), ' ', dtype='<U20')

    def getGrid(self):
        return self.__grid

    def getRows(self):
        return self.__rows

    def getColumns(self):
        return self.__columns

    def printGrid(self):
        '''Prints the whole grid'''

        for i in range(self.__rows):
            for j in range(self.__columns):
                print(BOLD + self.__grid[i][j], end='')
            print()

