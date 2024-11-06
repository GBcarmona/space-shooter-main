import pygame
from os.path import join
import random

import pygame.locals
#join is a method to put all together images you want 
# random = also a method to make random happen =)
#general setup
pygame.init()

WIDTH = 1280
HEIGHT = 720

caption = 'Study space gamee'
pygame.display.set_caption(caption)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True

#place surface 
path_meteor = join('images','meteor.png')



path_laser = join('images','laser.png')
laser = pygame.image.load(path_laser).convert_alpha()
meteor = pygame.image.load(path_meteor).convert_alpha()
path_star = join('images','star.png')
stars = pygame.image.load(path_star).convert_alpha()

path = join('images','space-ship.png')
space_ship = pygame.image.load(path).convert_alpha()
position_space_ship = space_ship.get_rect(center = (WIDTH / 2, HEIGHT / 2) )
position_meteor = meteor.get_rect(center = (WIDTH / 2, HEIGHT / 2) )
position_laser = laser.get_rect(bottomleft=(20, HEIGHT - 20))
position_shipp_direction = pygame.math.Vector2()
shipp_speed = 300

#Vector != array => if you do [1,2,3] times 2 the output will be [1,2,3,1,2,3] and the Vector will multiple the numbers


#convert or covert_alpha is for pygame can do a better perfomace
# space_ship = pygame.image.load('images/space-ship.png') if you put '..images/'
#  if the folder called 'images' is not in the game files will goes on but isn't a good way to make it

def random_star(num_star) :
    '''
    This function generates stars inside the window
    '''
    positions = []
    
    for _ in range(0,num_star) :
        x = random.randint(0,WIDTH - stars.get_width())
        y = random.randint(0,HEIGHT - stars.get_height())
        positions.append((x,y))
    return positions
stars_positions = random_star(20)
#this function ==> an array is set and a loop for is created to generates stars and put then on the array called 
#positions with the append
#yield(x,y)
    
# the variable called 'yield' generates series of number over time but they
#  aren't constantly so i am not using it
# yield: Used to produce a series of values over time. The function can be resumed later.(AI explanation)
# Generator: A function that uses yield to return values one at a time instead of all at once. 

       
#OTHER WAY TO MAKE THE STARS POSITIONS :
# star_position = [(x,y) randint(0,HEIGHT), randint(0,WIDTH) for i in range(20)]
# in while loop ==> for position in star position : screen.blit(stars,position)
        
while running :
    dt = clock.tick() / 1000
    # print(clock.get_fps()) show the rendered fps or Frame Per Second
    #delta time = dt is the time that yout computer gtake to render a frame 
    # inside the while loops the game will run 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        # if event.type == pygame.KEYDOWN and event.type == pygame.K_1 :
        #     print(1)
        # if event.type == pygame.MOUSEMOTION : 
        #     position_space_ship.center = event.pos

    keys = pygame.key.get_pressed()
    # if keys[pygame.K_RIGHT]:  # checks if the right key is on
    #     position_shipp_direction.x = 1  # direction to the right 
    #     position_space_ship.center += position_shipp_direction * dt * shipp_speed
    # EASIER WAY TO DO THAT : return a boolean
    position_shipp_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    position_shipp_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP]) 

    
         
    
    screen.fill('darkgray')
    for places in stars_positions:
        screen.blit(stars,places)
  
    position_space_ship.center += position_shipp_direction * shipp_speed * dt
    # # this makes the space ship object moves 
    if position_space_ship.left <= 0 : 
         position_shipp_direction.x = 1.0
    elif position_space_ship.right >= WIDTH :
         position_shipp_direction.x = -1.0
   
    if position_space_ship.top <= 0 : 
         position_shipp_direction.y = 1.0
    elif position_space_ship.bottom >= HEIGHT :
         position_shipp_direction.y = -1.0

# if position_space_ship.buttom <= HEIGHT or position_space_ship.top > 0 :
#    position_shipp_direction.y = 1.0
# if position_space_ship.right <= WIDTH or position_space_ship.left > 0 : 
#    position_shipp_direction.x = 1.0
# 

    
   
# the space ship goes to the right until reaches the window WIDTH the conditional above stops it 
# because of the oppositional moviment
    screen.blit(meteor,position_meteor)
    screen.blit(space_ship,position_space_ship)
    screen.blit(laser,position_laser)

    
    
    
    
    
    pygame.display.update()
# the for loop is to place the stars that are made in the function that is in the variable stars_allplace
pygame.quit()