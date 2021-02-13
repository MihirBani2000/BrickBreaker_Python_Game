import os
import time
import signal
import random


from config import *
from screen import *
from background import *
from input import *
from brick import *
from ball import *
from paddle import *


if __name__ == '__main__':
    print('inside main.py')
    # showmessage("Quit")
    game_screen = Screen(HEIGHT,WIDTH)
    game_box = Box()
    game_box.createBox(game_screen.getGrid())
    game_screen.printGrid()