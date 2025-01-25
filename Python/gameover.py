import pygame as pg

class GAMEOVER:
    def __init__(self):
        self.x = 100
        self.y = 200
        self.font_size = 40
        self.font = pg.font.Font("./Assets/fonts/PixelFont.ttf", self.font_size) 
        self.color = (255, 255, 255)
    
    def display(self, screen):
        score_text = self.font.render(f"Microplastics continues to harm turtles", True, self.color) 
        screen.blit(score_text, (self.x, self.y)) 
        score_text = self.font.render(f"           Stop polluting our oceans!", True, self.color) 
        screen.blit(score_text, (self.x, self.y + 60)) 
        score_text = self.font.render(f"                 Press R to Restart", True, self.color) 
        screen.blit(score_text, (self.x, self.y + 180))