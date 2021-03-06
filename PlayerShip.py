import pygame
from Constants import *

# Class for the User ship
class PlayerShip(pygame.sprite.Sprite):
    def __init__(self, image, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT * 0.95
        self.pause = False

# defining the position of the spaceship on the screen 
    def update(self):
        pos = pygame.mouse.get_pos()
        if self.pause == False:
            self.rect.x = pos[0]
            if self.rect.right >= SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
