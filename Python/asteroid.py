import pygame as pg
from random import randint
from math import cos, sin , radians

class ASTEROID:
     def __init__ (self,width,height):
          posrandom = randint(1,4)
          if posrandom == 1:
               self.x = -100
               self.y = 300
          elif posrandom == 2:
               self.x = 300
               self.y = -100
          elif posrandom == 3:
               self.x = 1000
               self.y = 300
          else:
               self.x = 300
               self.y = 700

          self.width = width
          self.height = height
          self.speed = 0.8
          self.sprite = pg.image.load("./Assets/Images/Asteroid.png").convert_alpha()
          self.sprite = pg.transform.scale(self.sprite, (self.width,self.height))
          self.mask = pg.mask.from_surface(self.sprite)
          self.rect = pg.Rect(self.x, self.y, self.width, self.height)
          self.dir = randint(-180,180)

     def draw(self,scr):
          self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
          self.rect.center = (self.x, self.y) 
          self.mask = pg.mask.from_surface(self.sprite)

          self.rotated_sprite = pg.transform.rotate(self.sprite, self.dir - 90)
          self.rotated_rect = self.rotated_sprite.get_rect(center=(self.x, self.y))

          scr.blit(self.rotated_sprite, self.rotated_rect)

     def move(self):
          dx = sin(radians(self.dir)) * self.speed
          dy = cos(radians(self.dir)) * self.speed
          self.x += dx
          self.y += dy

     def collide(self,bullets):
          for bullet in bullets:
               offset = (bullet.rect.x - self.rect.x, bullet.rect.y - self.rect.y)
               if self.mask.overlap(bullet.mask, offset):
                    return True, bullet
          return False, False
     
     def ship_collide(self, ship):
          offset = (ship.rect.x - self.rect.x, ship.rect.y - self.rect.y)
          if self.mask.overlap(ship.mask, offset):
               return True
          return False