import pygame as pg

class BG:
     def __init__ (self):
          self.x = 0
          self.y = 0
          self.width = 900
          self.height = 600
          self.sprite = pg.image.load("./Assets/Images/BG.png").convert_alpha()
          self.sprite = pg.transform.scale(self.sprite, (self.width,self.height))

     def draw(self,scr):
          scr.blit(self.sprite, (self.x, self.y))