# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random
import math

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
DARKERWHITE = (235, 245, 255)

num_clouds = 20

close_clouds =[]
far_clouds = []
for i in range(num_clouds):
    for t in range(2):
        x = random.randrange(0, 1600)
        y = random.randrange(-50, 200)
        s = random.randint(1,3)
        loc = [x, y, s]
        if t == 1:
            far_clouds.append(loc)
        else:
            close_clouds.append(loc)
    
def draw_close_cloud(loc):
    x = loc[0]
    y = loc[1]
    s = loc[2]
    
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])


def draw_far_cloud(loc):
    x = loc[0]
    y = loc[1]
    s = loc[2]
    
    pygame.draw.ellipse(screen, DARKERWHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARKERWHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARKERWHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, DARKERWHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, DARKERWHITE, [x + 20, y + 20, 60, 40])


time = 575
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for c in close_clouds:
        c[0] -= 3
    
        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    for f in far_clouds:
        f[0] -= 2
    
        if f[0] < -100:
            f[0] = random.randrange(800, 1600)
            f[1] = random.randrange(-50, 200)

            
    # Drawing code
    ''' sky '''
    screen.fill(BLUE)

    ''' sun '''
    sun_y = int((64-t**2)**(1/2))
    if 
    pygame.draw.ellipse(screen, YELLOW, [t, 75 + sun_y , 100, 100])
    t +=1
    ''' clouds '''
    for f in far_clouds:
        draw_far_cloud(f)
        
    for c in close_clouds:
        draw_close_cloud(c)

    
      

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
