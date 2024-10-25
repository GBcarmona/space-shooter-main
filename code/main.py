import pygame
from os.path import join
import random
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

#testing place surface retangle

path = join('images','space_ship.png')
path_star = join('images','star.png')

stars = pygame.image.load(path_star).convert_alpha()
space_ship = pygame.image.load(path).convert_alpha()
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
    # inside the while loops the game will run
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    
    screen.fill('darkgray')
    for places in stars_positions:
        screen.blit(stars,places)
    screen.blit(space_ship,(100,150))
    
    
    
    pygame.display.update()
# the for loop is to place the stars that are made in the function that is in the variable stars_allplace
pygame.quit()