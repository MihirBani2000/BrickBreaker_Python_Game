# design

### class bricks

- some health or strength of a brick
- if health zero, delete the brick, or make it disappear
- different types of bricks (subclasses),
  (different color, strength)
  (change the color as the health changes)
  - indestructible
  - 3 hits
  - 2 hits
  - 1 hit
- Collision
  - collision with a ball, reduce health by one, if not indestructible

### class ball

- velocity of ball x,y
- Collision:
  - collision with wall
    - if left or right : reverse x velocity
    - if top : reverse y velocity
  - collision with brick
    - reduce health if normal brick
    - if top or bottom: reverse y velocity
    - if left or right: reverse x velocity
  - collision with paddle
    - different parts of paddle, give different speed

### class paddle

- length
- movement
- Collision:
  - depending on the position where ball hits
    - (`pos - mid`) will be added to the velocity

### powerups

- expand paddle
- shrink paddle
- ball multiplier
- fast ball
- thru ball
- paddle grab

### class player

- score, and calculation
- lives, total and left
- time limit
- current playing time
