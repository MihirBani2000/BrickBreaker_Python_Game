from config import *


class Box:
    ''' Creates the background of the game
        like a box
        Walls on the three sides: top, left, right
        empty bottom
    '''

    def __init__(self):
        self.__wallDepth = 2
        self.__leftWall = BG_BLUE + BLUE + '|' + RESET
        self.__rightWall = BG_BLUE + BLUE + '|' + RESET
        self.__topWall = BLUE + '_' + RESET
        self.__bottom = RED + '^' + RESET

    def createBox(self, grid):
        # Left wall
        grid[1:HEIGHT - 1, 0:self.__wallDepth] = self.__leftWall
        # Right wall
        grid[1:HEIGHT - 1, WIDTH - self.__wallDepth:] = self.__rightWall
        # top wall
        grid[0, :] = self.__topWall
        # bottom
        grid[HEIGHT - 1, :] = self.__bottom

# the box
# ____________________
# ||                ||
# ||                ||
# ||                ||
# ||                ||
# ||                ||
# ||                ||
# ^^^^^^^^^^^^^^^^^^^^
