import random

from config import *
from powerups import *
from brick import *


def reposition_cursor(x=0,y=0):
    '''to keep the cursor at the same place (x,y)'''
    print("\033[%d;%dH" % (x, y))


def makeLayout(bricks,grid):
    '''makes the brick layout'''
    obj_brick = Brick()
    br_xlen,br_ylen = obj_brick.getLength()
    while True:
        os.system('clear')
        print("Select a valid option to continue: ")
        print("1. Layout 1")
        print("2. Layout 2")
        print("3. Exit")
        option = input()
        if option == '1': 
            '''LAYOUT 1'''
            for i in range(1,11):
                if i in [3,8]:
                    rbrick = GoldBrick(grid, i * (br_xlen+6), 15)
                    grbrick = GoldBrick(grid, i * (br_xlen+4)+10, 15 - 4*(br_ylen))
                else :
                    rbrick = RedBrick(grid, i * (br_xlen+6), 15)
                    grbrick = GreenBrick(grid, i * (br_xlen+4)+10, 15 - 4*(br_ylen))
                
                if i in [1,5,6,10]:
                    cbrick = GoldBrick(grid, i * (br_xlen+5)+5 , 15 - 2*(br_ylen) )
                else:    
                    cbrick = CyanBrick(grid, i * (br_xlen+5)+5 , 15 - 2*(br_ylen) )
                bricks.append(rbrick)
                bricks.append(grbrick)
                bricks.append(cbrick)
            break
        elif option == '2':
            '''LAYOUT 2'''
            for i in range(1,18):
                if i in [5,13]:
                    brick = GreenBrick(grid, i * (br_xlen)+7, 13)
                elif i in [3,8,10,15]:
                    brick = GoldBrick(grid, i * (br_xlen)+7, 13)
                else:
                    brick = RedBrick(grid, i * (br_xlen)+7, 13)
                bricks.append(brick)
            for i in range(1,16):
                if i in [8]:
                    brick = RedBrick(grid, i * (br_xlen)+13, 13 - 2*br_ylen)
                elif i in [3,13]:
                    brick = GreenBrick(grid, i * (br_xlen)+13, 13 - 2*br_ylen)
                elif i in [1,6,10,15]:
                    brick = GoldBrick(grid, i * (br_xlen)+13, 13 - 2*br_ylen)
                else:
                    brick = CyanBrick(grid, i * (br_xlen)+13, 13 - 2*br_ylen)
                bricks.append(brick)
            for i in range(1,14):
                if i in [1,5,9,13]:
                    brick = RedBrick(grid, i * (br_xlen)+20, 1)
                elif i in [3,7,11]:
                    brick = CyanBrick(grid, i * (br_xlen)+20, 1)
                else :
                    brick = GreenBrick(grid, i * (br_xlen)+20, 1)
                bricks.append(brick)
            break
        if option == '3':
            exit()
        else:
            print("select a valid option")



# POWERUPS related
def spawnPowerups(x,y,powerups):
    '''spawns a powerup with chance = probability, and stores in a list'''
    probability = 0.2

    # taking 20% chance of spawing a new powerup
    if random.random() <= probability:
        randChoice = random.randint(0,5)

        if randChoice == 0:
            power = ShrinkPaddle(x,y)
        elif randChoice ==1:
            power = ExpandPaddle(x,y)
        elif randChoice ==2:
            power = FastBall(x,y)
        elif randChoice ==3:
            power = ExpandPaddle(x,y)
        elif randChoice ==4:
            power = ShrinkPaddle(x,y)
        else:
            power = ExpandPaddle(x,y)
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