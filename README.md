# BRICK BREAKER

## Introduction

This is a terminal based game written in Python3 without the use of any curses libraries, inspired by the classic BrickBreaker games.
External libraries used are - `Numpy` and `Colorama`.

## Gameplay

- You control the Paddle, moving it sideways on the screen to bounce the ball.
- The ball collides with the walls, bricks, and the paddle.
- The target of the game is to destroy all bricks and make highscore.
- There are 3 levels with increasing difficulty.
- In the final level, you have to defeat the boss too.
- After a time limit, the bricks move one level down, when the ball touches the paddle.
- **Bricks:** types:

  | Type      |   Appearance   | Strength | Desription                          |
  | --------- | :------------: | :------: | ----------------------------------- |
  | Red       |      Red       |    3     |                                     |
  | Cyan      |      Cyan      |    2     |                                     |
  | Green     |     Green      |    1     |                                     |
  | Gold      |     Yellow     |   inf    | indestructible                      |
  | Exploding |     White      |    1     | explodes all the adjacent bricks    |
  | Rainbow   | Red/Cyan/Green |  3/2/1   | randomly changes strength and color |

- **Max Lives = 5**, whenever you miss the ball towards the bottom of the screen, a life is lost.
- **Scoring:** scores are calculated as follows:

  > - Single hit = +10
  > - Breaking a brick = +20
  > - Loosing a life = -30

- **Powerups:**
  | Type            | Appearance | Description                                         |
  | --------------- | :--------: | --------------------------------------------------- |
  | Expand Paddle   |     L      | expands the paddle by 2 units                       |
  | Shrink Paddle   |     S      | shrinks the paddle by 2 units                       |
  | Grab Paddle     |     G      | grabs the ball on the paddle                        |
  | Shooting Paddle |     B      | makes the paddle shoots bullets                     |
  | Fast Ball       |     F      | increases ball speed                                |
  | Thru Ball       |     T      | the ball destroys bricks in path and move past them |
  | Multiple Ball   |     M      | the number of ball increases by 2                   |
  | Fire Ball       |     I      | the brick explodes when ball collides               |

## Controls

- <kbd>A</kbd>: move paddle left
- <kbd>D</kbd>: move paddle right
- <kbd>SPACE</kbd>: release ball from paddle
- <kbd>X</kbd>: Change level
- <kbd>Q</kbd>: quit

## Get Set Go

To install the game:

1. Navigate into the repository

   ```(shell)
   $ cd path/to/repository
   ```

2. Install the required packages

   ```(shell)
   $ pip3 install numpy
   $ pip3 install colorama
   ```

3. Be ready to break some bricks!

   ```(shell)
   $ python3 main.py
   ```

---

## The Classes

This game follows the object-oriented programming paradigm. Here's a list of classes used:

- Player
- Screen
- Box
- Thing
  - Ball
  - Boss
  - Weapons
    - Bullet | Bomb
  - Brick
    - RedBrick | CyanBrick | GreenBrick | GoldBrick | ExplodingBrick | RainbowBrick
  - Paddle
  - Powerup
    - FastBall | ThruBall | MultipleBall | FireBall
    - ExpandPaddle | ShrinkPaddle | GrabPaddle | ShootingPaddle

## Object Oriented Concepts

Here's a list of the instances of the OOPS concepts in use:

### Inheritance

- The `Paddle`, `Ball`, `Brick` and its children, `Powerup` and its children, inherit the `Thing` class.
- `RedBrick`, `CyanBrick`, `GreenBrick`, `GoldBrick` and `ExplodingBrick`, inherit the `Brick` class.
- `FastBall`, `ThruBall`, `MultipleBall`, `GrabPaddle`, `ShrinkPaddle` and `ExpandPaddle`, inherit the `Powerup` class.

### Polymorphism

Some examples of polymorphism like _method overriding_. Several other examples are also present in the code.

- The `erase()` method defined in the `Thing` class has been overriden in the `Brick` class.
- The `getLength()` method defined in the `Thing` class has been overriden in the `Paddle` class.
- The `activate()/deActivate()` method defined in the `Powerup` class has been overriden in all children of this same class.

### Encapsulation

The entire game is modelled using classes and objects which encapsulate logically different entities.

### Abstraction

Methods like `Ball.move()`, `Ball.release()`, `Paddle.moveLeft()/Paddle.moveRight()`, `Player.showStats()` abstract away the details and make the code more readable and organised.
