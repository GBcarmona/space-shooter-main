import pygame
from os.path import join
import random

# Initialize pygame
pygame.init()

# Game window dimensions
WIDTH = 1280
HEIGHT = 720

# Set the window caption and display
caption = 'Study Space Game'
pygame.display.set_caption(caption)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



# images loads

meteor_image = pygame.image.load(join('images.png','meteor.png')).convert_alpha()
laser_image = pygame.image.load(join('images.png','laser.png')).convert_alpha()



class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join('images','space-ship.png')).convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.speed = 300
        self.player_direction = pygame.Vector2()

    def update(self,dt) : 
        
        self.player_direction.x = int(pygame.key.get_pressed()[pygame.K_RIGHT]) - int(pygame.key.get_pressed()[pygame.K_LEFT])
        self.player_direction.y = int(pygame.key.get_pressed()[pygame.K_DOWN]) - int(pygame.key.get_pressed()[pygame.K_UP])

        if self.player_direction.length() != 0 :
            self.player_direction = self.player_direction.normalize() 

        self.rect.center += self.speed * dt * self.player_direction

all_sprites = pygame.sprite.Group()


class Stars (pygame.sprite.Sprite) :   
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join('images','star.png'))
        self.rect = self.image.get_rect(center=(random.randint(0,WIDTH),random.randint(0,HEIGHT)))

#Sprites have been displayed
for i in range(21) :
    Stars(all_sprites)

player = Player(all_sprites)
# Meteor spawns 
meteor_event = pygame.event.custom_type
pygame.time.set_timer(meteor_event,500)
# Game loop
running = True
while running:
    dt = clock.tick(60) / 1000  # Delta time for smoother movement
    screen.fill(('silver'))          
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                print('fire laser')
        if event.type == meteor_event :
            print('KUDASAI')
    #update all_sprites with the arguemnt delta time
    all_sprites.update(dt)
        
   
    all_sprites.draw(screen)
    pygame.display.update()


pygame.quit()
