import os
import numpy as np
from colorama import Fore, init, Back, Style

init()


# sizes
HEIGHT = 30
WIDTH = 120
LEFTWALL = 2
RIGHTWALL = 2
TOPWALL = 1
BOX_WIDTH = WIDTH - RIGHTWALL
# Bottom =

# text styles
BOLD = "\033[1m"
DIM = "\033[2m"
UNDERLINED = "\033[4m"

# colors
RESET = Style.RESET_ALL
GREY = Fore.LIGHTBLACK_EX
CYAN = Fore.LIGHTCYAN_EX + Back.CYAN
RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
GCOLOR = Fore.LIGHTGREEN_EX + Back.GREEN
WHITE = Fore.WHITE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN


# misc


def showmessage(msg, obj_mando=None):
    print("\n\n")
    if msg == "Time Up":
        print("\t\t\t _______  ___   __   __  _______    __   __  _______\n" +
              "\t\t\t|       ||   | |  |_|  ||       |  |  | |  ||       |\n" +
              "\t\t\t|_     _||   | |       ||    ___|  |  | |  ||    _  |\n" +
              "\t\t\t  |   |  |   | |       ||   |___   |  |_|  ||   |_| |\n" +
              "\t\t\t  |   |  |   | |       ||    ___|  |       ||    ___|\n" +
              "\t\t\t  |   |  |   | | ||_|| ||   |___   |       ||   |\n" +
              "\t\t\t  |___|  |___| |_|   |_||_______|  |_______||___|\n")

    elif msg == "You won":
        print("\t\t\t __   __  ___   _______  _______  _______  ______    __   __\n" +
              "\t\t\t|  | |  ||   | |       ||       ||       ||    _ |  |  | |  |\n" +
              "\t\t\t|  |_|  ||   | |      _||_     _||   _   ||   | ||  |  |_|  |\n" +
              "\t\t\t|       ||   | |     |    |   |  |  | |  ||   |_||_ |       |\n" +
              "\t\t\t|       ||   | |     |    |   |  |  |_|  ||    __  ||_     _|\n" +
              "\t\t\t |     | |   | |     |_   |   |  |       ||   |  | |  |   |\n" +
              "\t\t\t  |___|  |___| |_______|  |___|  |_______||___|  |_|  |___|\n")

    elif msg == "Lives over":
        print("\t\t\t _______  _______  __   __  _______    _______  __   __  _______  ______\n" +
              "\t\t\t|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |\n" +
              "\t\t\t|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||\n" +
              "\t\t\t|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_\n" +
              "\t\t\t|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |\n" +
              "\t\t\t|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |\n" +
              "\t\t\t|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n")

    elif msg == "Quit":
        print("\t\t\t __   __  _______  __   __    _______  __   __  ___   _______ \n" +
              "\t\t\t|  | |  ||       ||  | |  |  |       ||  | |  ||   | |       |\n" +
              "\t\t\t|  |_|  ||   _   ||  | |  |  |   _   ||  | |  ||   | |_     _|\n" +
              "\t\t\t|       ||  | |  ||  |_|  |  |  | |  ||  |_|  ||   |   |   |  \n" +
              "\t\t\t|_     _||  |_|  ||       |  |  |_|  ||       ||   |   |   |  \n" +
              "\t\t\t  |   |  |       ||       |  |      | |       ||   |   |   |  \n" +
              "\t\t\t  |___|  |_______||_______|  |____||_||_______||___|   |___|  \n")

    print("\n\n")

    # if (msg != "Quit!!"):
    #     print("\t\t\t\t\t\t\t Score: ", obj_mando.get_score())

    print("\n\n")
