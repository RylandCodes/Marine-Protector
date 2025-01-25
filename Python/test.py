import pygame as pg
pg.init()
screen = pg.display.set_mode((800, 600))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.flip()