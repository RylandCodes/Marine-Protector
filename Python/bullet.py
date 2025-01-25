import pygame as pg
import math

class BULLET:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.radius = 12
        self.speed = 15
        self.dir = math.radians(-dir + 90) 
        self.sprite = pg.image.load("./Assets/Images/Bullet.png")
        self.sprite = pg.transform.scale(self.sprite, (self.radius,self.radius))
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
        self.mask = pg.mask.from_surface(self.sprite)
    def run(self, scr):
        self.x += math.cos(self.dir) * self.speed
        self.y += math.sin(self.dir) * self.speed
      
        self.rect.center = (self.x, self.y)
        
        scr.blit(self.sprite, self.rect)
    

