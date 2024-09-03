import os
import pygame as pg
import sys, time
from bird import Bird

class Game:
    def __init__(self):
        # Initialize Pygame
        pg.init()
        self.width = 600
        self.height = 768
        self.window = pg.display.set_mode((self.width, self.height))
        self.scale_factor = 1.5  # Adjust as needed
        self.clock = pg.time.Clock()
        self.move_speed = 250  # Pixels per second
        # Setup background and ground images
        self.bird = Bird(self.scale_factor)
        self.is_enter_pressed = False
        self.bgSetup()

    def gameLoop(self):
        last_time = time.time()
        while True:
            #Calculating Delta Time
            new_time = time.time()
            dt = new_time - last_time
            last_time = new_time
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                #Checking if the button is pressed which turns the is_enter_pressed to True
                if event.type == pg.KEYDOWN:
                    #If enter is pressed
                    if event.key == pg.K_RETURN:
                        self.is_enter_pressed = True
                    #If space is pressed
                    if event.key == pg.K_SPACE and self.is_enter_pressed:
                        self.bird.flap(dt)
            
            self.updateEverything(dt)
            self.drawEverything()
            pg.display.update()
            #Caps the frame rate to 60
            self.clock.tick(60)

    def updateEverything(self, dt):
        if self.is_enter_pressed:
        #Creates the movement of the ground
            self.ground1_rect.x -= self.move_speed * dt
            self.ground2_rect.x -= self.move_speed * dt

            if self.ground1_rect.right < 0:
                self.ground1_rect.x = self.ground2_rect.right
            if self.ground2_rect.right < 0:
                self.ground2_rect.x = self.ground1_rect.right

            self.bird.update(dt)

    def drawEverything(self):
        self.window.blit(self.bg_img, (0, -200))
        self.window.blit(self.ground1_img, self.ground1_rect)
        self.window.blit(self.ground2_img, self.ground2_rect)
        self.window.blit(self.bird.image, self.bird.rect)

    def bgSetup(self):
        # Get the directory of the current script
        script_dir = os.path.dirname(__file__)
        
        # Construct the full paths to the images
        bg_img_path = os.path.join(script_dir, 'assets', 'bg.png')
        ground_img_path = os.path.join(script_dir, 'assets', 'ground.png')

        # Load and transform the images
        self.bg_img = pg.transform.scale(pg.image.load(bg_img_path).convert(), (600, 1066))
        self.ground1_img = pg.transform.scale(pg.image.load(ground_img_path).convert(), (600, 250))
        self.ground2_img = pg.transform.scale(pg.image.load(ground_img_path).convert(), (600, 250))
        
        # Get the rectangles for the ground images
        self.ground1_rect = self.ground1_img.get_rect()
        self.ground2_rect = self.ground2_img.get_rect()

        # Set the positions for the ground images
        self.ground1_rect.x = 0
        self.ground2_rect.x = self.ground1_rect.right
        self.ground1_rect.y = 568
        self.ground2_rect.y = 568

# Initialize the game
game = Game()
game.gameLoop()