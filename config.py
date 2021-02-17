import os
import numpy as np
from colorama import Fore, init, Back, Style

init()

# text styles
BOLD = "\033[1m"
DIM = "\033[2m"
UNDERLINED = "\033[4m"

# colors
RESET = Style.RESET_ALL
GREY = Fore.LIGHTBLACK_EX
BG_GREY = Back.LIGHTBLACK_EX
# CYAN = Fore.LIGHTCYAN_EX + Back.CYAN
RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
BG_BLUE = Back.BLUE
GCOLOR = Fore.LIGHTGREEN_EX + Back.GREEN
WHITE = Fore.WHITE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN

# -------------------------------------------------------------------
# Game
MAX_LIVES = 5
GAME_TIME = 210  # seconds
POWER_TIME = 10  # 10 seconds for a powerup
HIT_SCORE = 10  # 10 points on hitting any brick
BREAK_SCORE = 20  # 20 points on breaking any brick
LIFE_PENALTY = -30  # 30 points penalty in case of losing a life

# Powerups constants
MIN_PADDLE_LENGTH = 5  # 5 units
MAX_PADDLE_LENGTH = 15  # 15 units
EXPAND = 2      # 2 units
SHRINK = 2      # 2 units
FAST_MULTIPLIER = 2

# Powerups symbols
EXPAND_FIG = Back.MAGENTA + WHITE + BOLD + 'L' + RESET
SHRINK_FIG = Back.MAGENTA + WHITE + BOLD + 'S' + RESET
GRAB_FIG = Back.MAGENTA + WHITE + BOLD + 'G' + RESET
FAST_FIG = Back.YELLOW + CYAN + BOLD + 'F' + RESET
THRU_FIG = Back.YELLOW + CYAN + BOLD + 'T' + RESET
MULITPLE_FIG = Back.YELLOW + CYAN + BOLD + 'M' + RESET

# sizes
HEIGHT = 30
WIDTH = 150
LEFTWALL = 2
RIGHTWALL = 2
TOPWALL = 1
BOX_WIDTH = WIDTH - RIGHTWALL

# messages
TIME_OVER = "Time Over"
QUIT = "Quit"
LIVES_OVER = "Lives Over"
VICTORY = "You Win"
