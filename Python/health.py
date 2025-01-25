import pygame as pg

class HEALTH:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.font_size = 60
        self.font = pg.font.Font("./Assets/fonts/PixelFont.ttf", self.font_size) 
        self.color = (200, 255, 255)
    
    def display(self, screen, health):
        if health <= 0:
            health = 0
        score_text = self.font.render(f"HP: {health}", True, self.color) 
        screen.blit(score_text, (self.x, self.y)) 