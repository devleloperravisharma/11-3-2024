import pgzrun
import random

TITLE = "gallaga"
WIDTH = 1200
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (65,105,225)
speed = 5
enemies = []
bullets = []
score = 0
direction = 1
for x in range(8):
    for y in range(4):
        enemy = Actor("bug")
        enemies.append(enemy)
        enemies[-1].x = 100 + 50*x
        enemies[-1].y = 80 + 50*y

ship = Actor("galaga")
ship.pos = (WIDTH//2, HEIGHT-50)

def draw():
    screen.clear()
    screen.fill(BLUE)
    ship.draw()
    for enemy in enemies:
        enemy.draw()

def update():
    global score, direction
    move_down = False
    if keyboard.left:
        ship.x -= 5
    if keyboard.right:
        ship.x += 5
pgzrun.go()