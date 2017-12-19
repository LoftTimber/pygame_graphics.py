# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
height = 600
leight = 800
SIZE = (leight, height)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
YELLOW = (255, 255, 0)
    

# Game loop
done = False



while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(WHITE)
    #44
    #29
    #69
    #135
    

    
    leight_in_pixels = 50
    size_of_pixel = leight/leight_in_pixels
    
    grid_line = 0



    ''' makes art'''
    pygame.draw.rect(screen, BLACK, [5*size_of_pixel, 22*size_of_pixel, 6*size_of_pixel, 7*size_of_pixel])
    pygame.draw.rect(screen, YELLOW, [6*size_of_pixel, 23*size_of_pixel, 5*size_of_pixel, 5*size_of_pixel])







    
    '''
    pygame.draw.rect(screen, BLACK, [10*size_of_pixel, 35*size_of_pixel, size_of_pixel, size_of_pixel])
    pygame.draw.rect(screen, BLACK, [11*size_of_pixel, 35*size_of_pixel, size_of_pixel, size_of_pixel])
    pygame.draw.rect(screen, YELLOW, [12*size_of_pixel, 35*size_of_pixel, size_of_pixel*3, size_of_pixel]) 
    pygame.draw.rect(screen, BLACK, [15*size_of_pixel, 35*size_of_pixel, size_of_pixel, size_of_pixel])
    pygame.draw.rect(screen, YELLOW, [16*size_of_pixel, 35*size_of_pixel, size_of_pixel*2, size_of_pixel*4])
    pygame.draw.rect(screen, YELLOW, [18*size_of_pixel, 35*size_of_pixel, size_of_pixel, size_of_pixel])
    pygame.draw.rect(screen, BLACK, [19*size_of_pixel, 35*size_of_pixel, size_of_pixel, size_of_pixel])
    pygame.draw.rect(screen, YELLOW, [20*size_of_pixel, 35*size_of_pixel, size_of_pixel, size_of_pixel])
    pygame.draw.rect(screen, YELLOW, [21*size_of_pixel, 35*size_of_pixel, size_of_pixel, size_of_pixel])
    pygame.draw.rect(screen, BLACK, [22*size_of_pixel, 35*size_of_pixel, size_of_pixel, size_of_pixel])
    pygame.draw.rect(screen, YELLOW, [23*size_of_pixel, 35*size_of_pixel, size_of_pixel*14, size_of_pixel])
    pygame.draw.rect(screen, BLACK, [37*size_of_pixel, 35*size_of_pixel, size_of_pixel, size_of_pixel])
    '''







    
    ''' makes grid '''
    
    while grid_line <= (leight_in_pixels-1)*size_of_pixel:
        pygame.draw.line(screen, BLACK, [grid_line, 0], [grid_line, height])
        grid_line += size_of_pixel
    grid_line = 0
    while grid_line <= (leight_in_pixels-1)*size_of_pixel:
        pygame.draw.line(screen, BLACK, [0, grid_line], [leight, grid_line])
        grid_line += size_of_pixel
   

    
    
    

    

    
    
    
    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
