import pygame as pg


class Bird(pg.sprite.Sprite):
    def __init__(self, scale_factor):
        super(Bird, self).__init__()
        #convert_alpha() is used to convert the image to a format that is easier to work with and faster to render
        self.image_list = [
            pg.transform.scale_by(pg.image.load('assets/birdup.png').convert_alpha(),scale_factor), 
            pg.transform.scale_by(pg.image.load('assets/birddown.png').convert_alpha(),scale_factor)
        ]
        #The image_index is used to determine which image to display
        self.image_index = 1
        #The image is the current image to display
        self.image = self.image_list[self.image_index]
        #The rect is the rectangle that represents the image
        self.rect = self.image.get_rect(center=(100,100))
        self.y_velocity = 0
        self.gravity = 10
        self.flap_speed = 250
        self.anim_counter = 0

    def update(self,dt):
        self.playAnimation()
        self.applyGravity(dt)
        

    def applyGravity(self, dt):
        self.y_velocity += self.gravity * dt
        self.rect.y += self.y_velocity 

    def flap(self, dt):
        self.y_velocity =- self.flap_speed * dt

    def playAnimation(self):
        if self.anim_counter == 5:
            self.image = self.image_list[self.image_index]
            if self.image_index == 0: self.image_index = 1
            else: self.image_index = 0

            self.anim_counter = 0
        
        self.anim_counter += 1