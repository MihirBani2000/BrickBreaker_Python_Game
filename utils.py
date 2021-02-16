from config import *


def reposition_cursor():
    '''to keep the cursor at the same place (0,0)'''
    print("\033[%d;%dH" % (0, 0))

def initializeBricks():
    pass

def deleteBricks(bricks):
    '''to delete the bricks which are not active anymore'''
    delBricks = []
    for brick in bricks:
        if not brick.isActive():
            delBricks.append(brick)
    
    for brick in delBricks:
        bricks.remove(brick)
        del brick
    
def leftBricks(bricks):
    for brick in bricks:
        if not brick.isGold():
            return 1 
    return 0