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

    '''draw flower'''
    x = 500
    y = 500
    pygame.draw.polygon(screen, YELLOW, [[x, y], [x-50, y-100], [x, y-200], [x+50, y-100]])
    pygame.draw.polygon(screen, BLACK, [[x, y], [x-100, y-50], [x-200, y], [x-100, y+50]])

































    
    
    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
