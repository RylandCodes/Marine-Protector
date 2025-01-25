import pygame as pg

class INSTRUCTIONS:
    def __init__(self):
        self.x = 125
        self.y = 200
        self.font_size = 60
        self.font = pg.font.Font("./Assets/fonts/PixelFont.ttf", self.font_size) 
        self.color = (255, 255, 255)
    
    def display(self, screen, hp):
        score_text = self.font.render(f"Press Arrow Keys to move", True, self.color) 
        screen.blit(score_text, (self.x, self.y)) 
        score_text = self.font.render(f"Press Q or Space to shoot", True, self.color) 
        screen.blit(score_text, (self.x, self.y + 60))
        score_text = self.font.render(f"       Avoid Plastic Bags", True, self.color) 
        screen.blit(score_text, (self.x, self.y + 120))