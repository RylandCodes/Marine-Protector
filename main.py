import pygame as pg
from sys import exit
from math import degrees
from sys import exit , executable , argv
from os import execl

from Python.ship import SHIP
from Python.bullet import BULLET
from Python.asteroid import ASTEROID
from Python.bg import BG
from Python.health import HEALTH
from Python.score import SCORE
from Python.instructions import INSTRUCTIONS
from Python.gameover import GAMEOVER

pg.init()

def restart_program():
    execl(executable, executable, *argv)

WIDTH = 900
HEIGHT = 600
SCREEN = pg.display.set_mode((WIDTH, HEIGHT), pg.HWSURFACE | pg.DOUBLEBUF)
FPS = 60
CLOCK = pg.time.Clock()
BLACK = (0,0,0)
Bg = BG()
Score = SCORE()
Instructions = INSTRUCTIONS()
Gameover = GAMEOVER()
pg.display.set_caption("Marine Protector - Avoid the Plastic Bags")

ship = SHIP()
Health = HEALTH()
score= 0

bullets = []
asteroids = []

asteroid_wait = 0

health = 30

running = True
while running:
    SCREEN.fill(BLACK)
    Bg.draw(SCREEN)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    asteroid_wait += 1
    if asteroid_wait >= 6:
        asteroid_wait = 0
        asteroid = ASTEROID(100,100)
        asteroids.append(asteroid)

    asteroids = [asteroid for asteroid in asteroids if asteroid.x < 1200 and asteroid.x > -300 and asteroid.y < 900 and asteroid.y > -300]
    for asteroid in asteroids[:]: # Iterate over a copy
        asteroid.draw(SCREEN)
        asteroid.move()
        collide, bullet = asteroid.collide(bullets)
        if collide:
            if bullet:
                bullets.remove(bullet)
            asteroids.remove(asteroid)
            for i in range(2):
                Asteroid = ASTEROID(asteroid.width / 2,asteroid.height / 2)
                Asteroid.x = asteroid.x
                Asteroid.y = asteroid.y

                if Asteroid.width > 5:
                    asteroids.append(Asteroid)
                    
    for asteroid in asteroids[:]:
        ship_collide = asteroid.ship_collide(ship)
        if ship_collide:
            asteroids.remove(asteroid)
            health -= 1
        

    Health.display(SCREEN, health)

    ship.draw(SCREEN)
    ship.move(health)
    if health > 0:
        score += 0.3
        shoot = ship.shoot()
        if shoot:
            bullet = BULLET(ship.x,ship.y,ship.dir-20)
            bullets.append(bullet)
            bullet = BULLET(ship.x,ship.y,ship.dir-10)
            bullets.append(bullet)
            bullet = BULLET(ship.x,ship.y,ship.dir)
            bullets.append(bullet)
            bullet = BULLET(ship.x,ship.y,ship.dir+10)
            bullets.append(bullet)
            bullet = BULLET(ship.x,ship.y,ship.dir+20)
            bullets.append(bullet)
    if not ship.start_moving:
        Instructions.display(SCREEN, health)
    Score.display(SCREEN,score)
    bullets = [bullet for bullet in bullets if bullet.x < 900 and bullet.x > 0 and bullet.y < 600 and bullet.y > 0]
    for bullet in bullets[:]:
        bullet.run(SCREEN)

    if health <= 0:
        Gameover.display(SCREEN)
        keys = pg.key.get_pressed()
        if keys[pg.K_r]:
            running = False  

    pg.display.flip() 
    CLOCK.tick(FPS)

if health <= 0:
    restart_program()
pg.quit()
exit()