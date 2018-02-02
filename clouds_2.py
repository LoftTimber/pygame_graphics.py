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
height = 600 #600
length = 800 #800
SIZE = (length, height)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
R = (255, 0, 0)     #RED
G = (0, 175, 0)     #GREEN
W = (255, 255, 255) #WHITE
b = (75, 200, 255)  #BLUE
Y = (255, 255, 175) #YELLOW
w = (235, 245, 255) #DARKERWHITE
B = (0, 0, 0)       #BLACK
O = (255, 165, 0)   #ORANGE
o = (255,80,0)      #DARKERORANGE
g = (34, 139, 34)   #FORESTGREEN

night_surface = pygame.Surface([length, height])

night_surface.fill(B)


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
    
    pygame.draw.ellipse(screen, W, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, W, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, W, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, W, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, W, [x + 20, y + 20, 60, 40])


def draw_far_cloud(loc):
    x = loc[0]
    y = loc[1]
    s = loc[2]
    
    pygame.draw.ellipse(screen, w, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, w, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, w, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, w, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, w, [x + 20, y + 20, 60, 40])

def draw_player():
    line1 = [0,0,0,0,0,0,0,B,B]
    line2 = [0,0,B,0,0,0,B,O,O,B,0,0,0,B]
    line3 = [0,B,O,B,0,B,O,O,O,O,B,0,B,o,B]
    line4 = [0,B,O,O,B,O,O,O,O,O,O,B,O,O,B]
    line5 = [B,O,O,O,O,O,O,O,O,O,O,O,O,O,o,B]
    line6 = [B,O,O,O,B,B,O,O,O,B,B,O,O,O,o,B]
    line7 = [B,O,O,B,O,O,B,O,B,O,O,B,O,O,o,B]
    line8 = [B,O,O,O,O,O,O,O,O,O,O,O,O,o,o,B]
    line9 = [0,B,O,O,O,O,O,O,O,O,O,O,O,o,B]
    line10= [0,0,B,o,O,O,O,O,O,O,o,o,o,B]
    line11= [0,0,0,B,B,o,o,o,o,o,o,B,B]
    line12= [0,0,0,0,0,B,B,B,B,B,B]
    line13= [0,0,B,B,B,0,B,G,g,B,B,B,B]
    line14= [0,B,G,G,g,B,B,G,g,B,G,G,g,B]
    line15= [B,G,G,G,G,g,B,G,B,G,G,G,G,g,B]
    line16= [B,g,g,g,g,g,B,B,B,g,g,g,g,g,B]
    line17= [0,B,B,B,B,B,0,0,0,B,B,B,B,B]

    
    line_colors = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17]
    return line_colors


    
time = -500
player_x_pos = 0
player_y_pos = 0

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                time = -400
            elif event.key == pygame.K_UP:
                player_y_pos -= 100
            elif event.key == pygame.K_DOWN:
                player_y_pos += 100
            elif event.key == pygame.K_RIGHT:
                player_x_pos += 100
            elif event.key == pygame.K_LEFT:
                player_x_pos -= 100

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

    sun_y = (1/20*time)**2
    if sun_y<400:
        sky = (75-abs(sun_y/20), 200-abs(sun_y/20), 255-abs(sun_y/20))
    else:
        sky = 0

    sunset = (-abs(time))+700
    if sunset<300:
        sunset = 
    # Drawing code
   
    
    ''' sky '''
    screen.fill(sky)
    
    ''' sun '''
    
    
    pygame.draw.ellipse(screen, Y, [time+400, 75 + sun_y , 100, 100])
    time +=5
    
    ''' clouds '''
    for f in far_clouds:
        draw_far_cloud(f)
        
    for c in close_clouds:
        draw_close_cloud(c)

    
    ''' sunset '''
    pygame.draw.rect(screen, G, [0, sunset, 800, 200])

    ''' grass '''
    pygame.draw.rect(screen, G, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, W, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, W, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, W, [0, 410], [800, 410], 5)

    ''' player '''
    length_in_pixels = 200
    size_of_pixel = length/length_in_pixels
    
    line_colors = draw_player()
    line = 0
    for i in range(len(line_colors)):
        position = 0
        current_line = line_colors[line]
        
        for i in range(len(current_line)):
            color_picked = current_line[position]
            if color_picked == 0:
                pass
            else:
                pygame.draw.rect(screen, color_picked, [(player_x_pos)+position*size_of_pixel, (player_y_pos)+line*size_of_pixel, size_of_pixel, size_of_pixel])
                
            position += 1

        line += 1

    if sun_y<400:
        night_surface.set_alpha(abs((sun_y/1.7)))
    else:
        night_surface.set_alpha(abs((400/1.7)))
   

        
    screen.blit(night_surface,[0,0])
    
    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
