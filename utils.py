import random

from config import *
from powerups import *
from brick import *


def reposition_cursor(x=0,y=0):
    '''to keep the cursor at the same place (x,y)'''
    print("\033[%d;%dH" % (x, y))


# POWERUPS related
def spawnPowerups(x,y,powerups):
    '''spawns a powerup with chance = probability, and stores in a list'''
    probability = 1

    # taking 20% chance of spawing a new powerup
    if random.random() <= probability:
        randChoice = random.randint(0,5)

        if randChoice == 0:
            power = ShrinkPaddle(x,y)
        elif randChoice ==1:
            power = ExpandPaddle(x,y)
        elif randChoice ==2:
            power = ShrinkPaddle(x,y)
        elif randChoice ==3:
            power = ShrinkPaddle(x,y)
            # pass
        elif randChoice ==4:
            power = ShrinkPaddle(x,y)
            # pass
        else:
            power = ShrinkPaddle(x,y)
            # pass
    powerups.append(power)

def deleteActivePowerups(powerups,grid,paddle,ball,all=False):
    '''to delete and deactivate the powerups'''
    if not all and powerups:
        for power in powerups:
            if round(time.time()) - power.getTime() >= POWER_TIME:
                power.deActivate(grid,paddle,ball)
                powerups.remove(power)
                del power
                return
    
    if all and powerups:
        delPowers = []
        for power in powerups:
            power.deActivate(grid,paddle,ball)
            delPowers.append(power)
        for power in delPowers:
            powerups.remove(power)
            del power
        delPowers.clear()
        return    
    
def deleteAllPowerups(powerups,grid):
    '''to delete all the powerups'''
    if powerups:
        delPowers = []
        for power in powerups:
            power.erase(grid)
            delPowers.append(power)
        for power in delPowers:
            powerups.remove(power)
            del power
        delPowers.clear()
        return    

def movePowerups(powerups,activatedPowerups,grid,paddle,player,ball):
    if powerups:
        delPower = []
        for power in powerups:
            if power.move(grid,paddle,player,ball):
                activatedPowerups.append(power)
                delPower.append(power)
        if delPower:
            for power in delPower:
                powerups.remove(power)



# BRICK related
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

def printBricks(grid,bricks):
    for brick in bricks:
        bX,bY = brick.getPos()
        fig = brick.getFig()
        brick.placeBrick(grid,bX,bY,fig)