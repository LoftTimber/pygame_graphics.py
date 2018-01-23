# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Rainy Day"
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
DARKERBLUE = (20, 0, 100)
DARKERWHITE = (200, 200, 200)
DARKERGREEN = (0, 100, 0)

#Making Clouds
num_clouds = 100
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    s = random.randint(1,3)
    loc = [x, y, s]
    clouds.append(loc)
    
def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    s = loc[2]
    
    pygame.draw.ellipse(screen, DARKERWHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARKERWHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARKERWHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, DARKERWHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, DARKERWHITE, [x + 20, y + 20, 60, 40])

#Making Rain
rain = []
for i in range(1000):
    x = -10
    y = 610
    r = random.randrange(1, 5)
    v = 5
    s = [x, y, r, r]
    rain.append(s)
   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for c in clouds:
        c[0] -= c[2]

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)


    for r in rain:
        r[0] -= r[2]
        r[1] += r[2]

        if r[1] > random.randint(400, 1200):
            r[0] = random.randrange(-10, 1600)
            r[1] = random.randrange(-600, -10)


        
    # Drawing code
    ''' sky '''
    screen.fill(DARKERBLUE)

    

    
        

    ''' grass '''
    pygame.draw.rect(screen, DARKERGREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' rain '''
    for s in rain:
        pygame.draw.ellipse(screen, BLUE, s)

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
