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
pygame.display.set_caption(caption)  # Simplified caption setting
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join('images', 'space-ship.png')).convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.speed = 300
        self.player_direction = pygame.Vector2()
        
        #cooldown
        self.can_shoot = True
        self.laser_timer = 0
        self.cooldown = 500
    
    def laser_cooldown(self) : 
        ''' 
        laser cooldown until shoot again
        '''
        if not self.can_shoot :
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_timer >= self.cooldown : 
                self.can_shoot = True


    def update(self, dt):
        self.player_direction.x = int(pygame.key.get_pressed()[pygame.K_RIGHT]) - int(pygame.key.get_pressed()[pygame.K_LEFT])
        self.player_direction.y = int(pygame.key.get_pressed()[pygame.K_DOWN]) - int(pygame.key.get_pressed()[pygame.K_UP])

        if self.player_direction.length() != 0:
            self.player_direction.normalize()  # Normalize for consistent movement
            
        recent_key = pygame.key.get_just_pressed()
        if recent_key[pygame.K_SPACE] : 
            Laser(self.rect.midtop,all_sprites)
            self.can_shoot = False # set to make the cooldown
            self.laser_timer = pygame.time.get_ticks()
        
        self.laser_cooldown()
        self.rect.center += self.speed * dt * self.player_direction
        
       
    


# Grouping all sprites
all_sprites = pygame.sprite.Group()
 

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos ,*groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join('images', 'laser.png'))
        self.rect = self.image.get_frect(midbottom = pos)
        self.speed = 500
        
    def update(self,dt) : 
        #moves the laser
        self.rect.centery -= self.speed * dt   
        #Removes the laser that it goes off the screen
        if self.rect.bottom < 0 :
            self.kill()


class Stars(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join('images', 'star.png'))
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))


# Create stars
for _ in range(21):
    Stars(all_sprites)

# Create player
player = Player(all_sprites)


class Meteor(pygame.sprite.Sprite) :
    def __init__(self, pos ,*groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join("Images","meteor.png"))
        self.rect = self.image.get_frect(center = pos)
        self.speed = random.randint(500,550)
        self.direction = pygame.Vector2(random.uniform(-0.5,0.5),y=1)
        self.spawn_time = pygame.time.get_ticks()
        self.time = 2000
        
    def update(self,dt) :
        self.rect.centery += self.direction.y * self.speed  * dt
       
        if pygame.time.get_ticks() - self.spawn_time >= self.time :
            self.kill()
        
        
        

# Meteor spawn event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)  # Spawn meteor every 500 milliseconds == half second

# Game loop
running = True
while running:
    dt = clock.tick(60) / 1000  # Delta time for smoother movement

    screen.fill(('silver'))  # Fill screen with silver color

    # pool of events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==  meteor_event :
            x , y = random.randint(0,WIDTH) , random.randint(-100,-50)  
            Meteor((x,y),all_sprites)       
          
    # Update all sprites with delta time
    all_sprites.update(dt)
    

    # Draw all sprites on the screen
    all_sprites.draw(screen)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()