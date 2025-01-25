import pygame as pg

class SCORE:
    def __init__(self):
        self.x = 20
        self.y = 80
        self.font_size = 60
        self.font = pg.font.Font("./Assets/fonts/PixelFont.ttf", self.font_size) 
        self.color = (200, 255, 255)
    def display(self, screen , score):
        score = int(score)
        score_text = self.font.render(f"Score: {score}", True, self.color) 
        screen.blit(score_text, (self.x, self.y)) 