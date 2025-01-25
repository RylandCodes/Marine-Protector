import pygame as pg
from math import radians, cos, sin

class SHIP:
     def __init__ (self):
          self.x = 450
          self.y = 300
          self.width = 120
          self.height = 120
          self.sprite = pg.image.load("./Assets/Images/Ship.png").convert_alpha()
          self.sprite = pg.transform.scale(self.sprite, (self.width,self.height))
          self.mask = pg.mask.from_surface(self.sprite)
          self.rect = pg.Rect(self.x, self.y, self.width, self.height)
          self.dir = 180
          self.speed = 0.5
          self.velocity_x = 0
          self.velocity_y = 0
          self.friction = 0.975
          self.debounce = False
          self.debounce_frame = 0
          self.start_moving = False

     def draw(self,scr):
          self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
          self.rect.center = (self.x, self.y) 
          self.mask = pg.mask.from_surface(self.sprite)

          self.rotated_sprite = pg.transform.rotate(self.sprite, self.dir)
          self.rotated_rect = self.rotated_sprite.get_rect(center=(self.x, self.y))

          scr.blit(self.rotated_sprite, self.rotated_rect)

     def move(self, hp):
          keys = pg.key.get_pressed()

          if keys[pg.K_LEFT] or keys[pg.K_a]:
               self.dir += 4.5
          elif keys[pg.K_RIGHT] or keys[pg.K_d]:
               self.dir -= 4.5
          
          if (keys[pg.K_w] or keys[pg.K_UP]) and hp > 0:
               self.start_moving = True
               dx = sin(radians(self.dir)) * self.speed
               dy = cos(radians(self.dir)) * self.speed
               self.velocity_x += dx
               self.velocity_y += dy

          if self.x >= 920:
               self.x = 0
               
          elif self.x <= -20:
               self.x = 900
               
          elif self.y >= 620:
               self.y = 0
               
          elif self.y <= -20:
               self.y = 620
               
          self.velocity_x *= self.friction
          self.velocity_y *= self.friction
          
          self.x += self.velocity_x
          self.y += self.velocity_y
     
     def shoot(self):
          if not self.debounce:
               self.debounce = True
               keys = pg.key.get_pressed()
               if keys[pg.K_SPACE] or keys[pg.K_q]:
                    return True
          else:
               if self.debounce:
                    self.debounce_frame += 1
               if self.debounce_frame >= 5:
                    self.debounce = False
                    self.debounce_frame  = 0
          return False
