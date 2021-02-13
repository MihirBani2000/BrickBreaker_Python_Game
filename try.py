import autopep8
import numpy as np
from colorama import init,Style,Fore,Back 

init()

RESET = Style.RESET_ALL
GREY = Fore.LIGHTBLACK_EX
CYAN = Fore.LIGHTCYAN_EX+Back.CYAN
RED = Fore.RED
BLUE = Fore.BLUE
GCOLOR = Fore.LIGHTGREEN_EX+Back.GREEN
WHITE = Fore.WHITE
ICE = Fore.CYAN


print(Back.MAGENTA)
for i in range(4):
    for j in range(30):
        print(' | ', end='')
    print()
print(Back.RESET)