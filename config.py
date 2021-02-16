import os
import numpy as np
from colorama import Fore, init, Back, Style

init()

# Game
MAX_LIVES = 5
GAME_TIME = 210 # seconds
HIT_SCORE = 10  # 10 points on hitting any brick
BREAK_SCORE = 20  # 20 points on breaking any brick
LIFE_PENALTY = -30 # 30 points penalty in case of losing a life 

# messages
TIME_OVER = "Time Over"
QUIT = "Quit"
LIVES_OVER = "Lives Over"
VICTORY = "You Win"


# sizes
HEIGHT = 30
WIDTH = 120
LEFTWALL = 2
RIGHTWALL = 2
TOPWALL = 1
BOX_WIDTH = WIDTH - RIGHTWALL

# text styles
BOLD = "\033[1m"
DIM = "\033[2m"
UNDERLINED = "\033[4m"

# colors
RESET = Style.RESET_ALL
GREY = Fore.LIGHTBLACK_EX
BG_GREY = Back.LIGHTBLACK_EX
CYAN = Fore.LIGHTCYAN_EX + Back.CYAN
RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
BG_BLUE = Back.BLUE
GCOLOR = Fore.LIGHTGREEN_EX + Back.GREEN
WHITE = Fore.WHITE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN


# misc
