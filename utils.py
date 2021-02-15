from config import *


def reposition_cursor():
    '''to keep the cursor at the same place (0,0)'''
    print("\033[%d;%dH" % (0, 0))

def showmessage(msg, player=None):
    """Displays the message according to the condition, at end of game"""

    os.system('clear')
    print("\n\n")
    if msg == TIME_OVER:
        print("\t\t\t _______  ___   __   __  _______    __   __  _______\n" +
              "\t\t\t|       ||   | |  |_|  ||       |  |  | |  ||       |\n" +
              "\t\t\t|_     _||   | |       ||    ___|  |  | |  ||    _  |\n" +
              "\t\t\t  |   |  |   | |       ||   |___   |  |_|  ||   |_| |\n" +
              "\t\t\t  |   |  |   | |       ||    ___|  |       ||    ___|\n" +
              "\t\t\t  |   |  |   | | ||_|| ||   |___   |       ||   |\n" +
              "\t\t\t  |___|  |___| |_|   |_||_______|  |_______||___|\n")

    elif msg == VICTORY:
        print("\t\t\t __   __  ___   _______  _______  _______  ______    __   __\n" +
              "\t\t\t|  | |  ||   | |       ||       ||       ||    _ |  |  | |  |\n" +
              "\t\t\t|  |_|  ||   | |      _||_     _||   _   ||   | ||  |  |_|  |\n" +
              "\t\t\t|       ||   | |     |    |   |  |  | |  ||   |_||_ |       |\n" +
              "\t\t\t|       ||   | |     |    |   |  |  |_|  ||    __  ||_     _|\n" +
              "\t\t\t |     | |   | |     |_   |   |  |       ||   |  | |  |   |\n" +
              "\t\t\t  |___|  |___| |_______|  |___|  |_______||___|  |_|  |___|\n")

    elif msg == LIVES_OVER:
        print("\t\t\t _______  _______  __   __  _______    _______  __   __  _______  ______\n" +
              "\t\t\t|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |\n" +
              "\t\t\t|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||\n" +
              "\t\t\t|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_\n" +
              "\t\t\t|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |\n" +
              "\t\t\t|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |\n" +
              "\t\t\t|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n")

    elif msg == QUIT:
        print("\t\t\t __   __  _______  __   __    _______  __   __  ___   _______ \n" +
              "\t\t\t|  | |  ||       ||  | |  |  |       ||  | |  ||   | |       |\n" +
              "\t\t\t|  |_|  ||   _   ||  | |  |  |   _   ||  | |  ||   | |_     _|\n" +
              "\t\t\t|       ||  | |  ||  |_|  |  |  | |  ||  |_|  ||   |   |   |  \n" +
              "\t\t\t|_     _||  |_|  ||       |  |  |_|  ||       ||   |   |   |  \n" +
              "\t\t\t  |   |  |       ||       |  |      | |       ||   |   |   |  \n" +
              "\t\t\t  |___|  |_______||_______|  |____||_||_______||___|   |___|  \n")

    print("\n\n")
    print("\t\t\t\t\t\t Score: ", player.getScores())
    print("\n\n")
