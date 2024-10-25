import pygame
#general setup
pygame.init()

caption = 'Study space gamee'
pygame.display.set_caption(caption)
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

#testing place surface retangle
surf = pygame.Surface((100,200))
surf.fill('orange')
x= 100

space_ship = pygame.image.load('images/space-ship.png')
# space_ship = pygame.image.load('images/space-ship.png') if you put ..images/ if the images is out of the file it will goes well but it not good to do it


while running :
    # inside the while loops the game will run
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    screen.fill('silver')
    screen.blit(space_ship,(x,150))
    x += 0.1
    
    pygame.display.update()
    
pygame.quit()