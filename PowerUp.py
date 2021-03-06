import pygame

# Class for the power up drops 
class PowerUp(pygame.sprite.Sprite):

    def __init__(self, power_ups_id, power_ups_id_list, images, pos_x, pos_y, *group):
        super().__init__(*group) # calling initialisation of the parent function
        self.power_ups_id = power_ups_id
        self.power_ups_id_list = power_ups_id_list
        self.images = images
        self.index = 0
        self.image = self.images[self.power_ups_id_list.index(self.power_ups_id)][self.index]
        self.rect = self.image.get_rect()
        self.rect.centerx = pos_x
        self.rect.y = pos_y
        self.animation_frames = 10
        self.current_frame = 0
        self.speed = 10
        self.pause = False

#Defining the position of the powerup on the screen
    def update(self):
        if self.pause == False:
            self.current_frame += 1 #Frames count up
            if self.current_frame >= self.animation_frames: # If frames reach max, restart. 
                self.current_frame = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.power_ups_id_list.index(self.power_ups_id)][self.index]
            self.rect.y += self.speed
        else:
            self.current_frame += 0
            self.rect.y += 0
