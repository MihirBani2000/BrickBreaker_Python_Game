import random

from config import *
from powerups import *
from brick import *


def reposition_cursor(x=0,y=0):
    '''to keep the cursor at the same place (x,y)'''
    print("\033[%d;%dH" % (x, y))


def printLayout(bricks,grid,layout,xoffset=0,yoffset=1,custom=None):
    
    obj_brick = Brick()
    br_xlen,br_ylen = obj_brick.getLength()
    

    rows = [ lay.split() for lay in layout ]
    for (rind,row) in enumerate(rows):
        
        for (cind,char) in enumerate(row):
            print("rind",rind, " cind",cind)
            brick = None
            if char == 'G': #green
                brick = GreenBrick(grid, cind * (br_xlen+xoffset), rind*(br_ylen+yoffset)+3)
            elif char == 'R': #red
                brick = RedBrick(grid, cind * (br_xlen+xoffset), rind*(br_ylen+yoffset)+3)
            elif char == 'C': #cyan
                brick = CyanBrick(grid, cind * (br_xlen+xoffset), rind*(br_ylen+yoffset)+3)
            elif char == 'Y': #gold
                brick = GoldBrick(grid, cind * (br_xlen+xoffset), rind*(br_ylen+yoffset)+3)
            elif char == 'E': # exploding
                if custom != None:
                    brick = ExplodingBrick(grid, cind * (br_xlen+xoffset), rind*(br_ylen+custom)+3)
                else:
                    brick = ExplodingBrick(grid, cind * (br_xlen+xoffset), rind*(br_ylen+yoffset)+3)
            if brick!=None:
                bricks.append(brick)

def chooseLayout(bricks,grid):
    '''makes the brick layout based on user choice'''
    obj_brick = Brick()
    br_xlen,br_ylen = obj_brick.getLength()
    while True:
        os.system('clear')
        print("Select a valid option to continue: \n")
        print("1. Layout 1: Boring\n")
        print("2. Layout 2: Fun\n")
        print("3. Layout 3: Death\n")
        print("4. Exit")
        option = input()
        
        if option == '1': 
            '''LAYOUT 1'''

            layout = [  "- - - - G G Y G G G G Y G - - - - -",
                        "- - - Y C C - C Y C - C C Y - - - -",
                        "- - - R Y G R R C R R G Y R - - - -",
                    ]
            printLayout(bricks,grid,layout,2,3)

            # for i in range(1,11):
            #     if i in [3,8]:
            #         rbrick = GoldBrick(grid, i * (br_xlen+6), 15)
            #         grbrick = GoldBrick(grid, i * (br_xlen+4)+10, 15 - 4*(br_ylen))
            #     else :
            #         rbrick = RedBrick(grid, i * (br_xlen+6), 15)
            #         grbrick = GreenBrick(grid, i * (br_xlen+4)+10, 15 - 4*(br_ylen))
                
            #     if i in [1,5,6,10]:
            #         cbrick = GoldBrick(grid, i * (br_xlen+5)+5 , 15 - 2*(br_ylen) )
            #     else:    
            #         cbrick = CyanBrick(grid, i * (br_xlen+5)+5 , 15 - 2*(br_ylen) )
            #     bricks.append(rbrick)
            #     bricks.append(grbrick)
            #     bricks.append(cbrick)
            break



        elif option == '2':
            '''LAYOUT 2'''

            layout = [  "- - - - R G C G R G C G R G C G R - - -",
                        "- - - - - - - - - - - - - - - - - - - -",
                        "- - - Y C G C C Y C R C Y C C G C Y - -",
                        "- - - - - - G E E E E E E E G - - - - -",
                        "- - R R Y R G R R Y R Y R R G R Y R R -",
                    ]
            printLayout(bricks,grid,layout,0,0)


            # for i in range(6,13):
            #     # if i in [5,13]:
            #     brick = ExplodingBrick(grid, i * (br_xlen)+7, 13+br_ylen)
            #     # elif i in [3,8,10,15]:
            #     #     brick = GoldBrick(grid, i * (br_xlen)+7, 13)
            #     # else:
            #     #     brick = RedBrick(grid, i * (br_xlen)+7, 13)
            #     bricks.append(brick)
            # for i in range(1,18):
            #     if i in [5,13]:
            #         brick = GreenBrick(grid, i * (br_xlen)+7, 13)
            #     elif i in [3,8,10,15]:
            #         brick = GoldBrick(grid, i * (br_xlen)+7, 13)
            #     else:
            #         brick = RedBrick(grid, i * (br_xlen)+7, 13)
            #     bricks.append(brick)
            # for i in range(1,16):
            #     if i in [8]:
            #         brick = RedBrick(grid, i * (br_xlen)+13, 14 - 2*br_ylen)
            #     elif i in [3,13]:
            #         brick = GreenBrick(grid, i * (br_xlen)+13, 14 - 2*br_ylen)
            #     elif i in [1,6,10,15]:
            #         brick = GoldBrick(grid, i * (br_xlen)+13, 14 - 2*br_ylen)
            #     else:
            #         brick = CyanBrick(grid, i * (br_xlen)+13, 14 - 2*br_ylen)
            #     bricks.append(brick)
            # for i in range(1,14):
            #     if i in [1,5,9,13]:
            #         brick = RedBrick(grid, i * (br_xlen)+20, br_ylen)
            #     elif i in [3,7,11]:
            #         brick = CyanBrick(grid, i * (br_xlen)+20, br_ylen)
            #     else :
            #         brick = GreenBrick(grid, i * (br_xlen)+20, br_ylen)
            #     bricks.append(brick)
            break
        if option =='3':
            '''Layout 3'''
            layout = [  "- - - - - - G Y R C G R C R Y G - - - - -",
                        "- - - - - Y C R G Y R G Y G R C Y - - - -",
                        "- - - - - G - G - - - - - - G - G - - - -",
                        "- - - - - R C Y E E E E E E Y C R - - - -",
                        "- - - - - - R Y Y Y Y Y Y Y Y R - - - - -"
                    ]
            printLayout(bricks,grid,layout,yoffset=0)
            break
        if option == '4' or option=='q':
            exit()
        else:
            print("select a valid option")



# POWERUPS related
def spawnPowerups(x,y,powerups):
    '''spawns a powerup with chance = probability, and stores in a list'''
    probability = 0.3
    # probability = 1

    # taking 20% chance of spawing a new powerup
    if random.random() <= probability:
        randChoice = random.randint(0,5)
        # randChoice = 4

        if randChoice == 0:
            power = ShrinkPaddle(x,y)
        elif randChoice ==1:
            power = ExpandPaddle(x,y)
        elif randChoice ==2:
            power = FastBall(x,y)
        elif randChoice ==3:
            power = GrabPaddle(x,y)
        elif randChoice ==4:
            power = ThruBall(x,y)
        else:
            power = GrabPaddle(x,y)
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

def deleteBricks(bricks):
    '''to delete the bricks which are not active anymore'''
    if bricks:
        delBricks = []
        for brick in bricks:
            if not brick.isActive():
                delBricks.append(brick)
        
        for brick in delBricks:
            bricks.remove(brick)
            del brick
    
def leftBricks(bricks):
    if bricks:
        for brick in bricks:
            if not brick.isGold():
                return 1 
    return 0

def printBricks(grid,bricks):
    if bricks:
        for brick in bricks:
            bX,bY = brick.getPos()
            fig = brick.getFig()
            brick.placeBrick(grid,bX,bY,fig)