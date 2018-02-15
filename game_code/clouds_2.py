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
O = (255, 165, 0)   #ORANGE
Y = (255, 255, 0)   #YELLOW
G = (0, 128, 0)     #GREEN
S = (0,0,255)       #BLUE
I = (75,0,130)      #INDIGO
V = (238,130,238)   #VIOLET








W = (255, 255, 255) #WHITE
b = (75, 200, 255)  #SKYBLUE
l = (176, 196, 222) #LIGHTSTEELBLUE
w = (235, 245, 255) #DARKERWHITE
B = (0, 0, 0)       #BLACK
o = (255,80,0)      #DARKERORANGE
g = (34, 139, 34)   #FORESTGREEN

thunder = pygame.mixer.Sound('sounds/thunder.ogg')
pygame.mixer.music.load('sounds/rain.ogg')


player_facing_left = pygame.image.load('photos/player_facing_left.png')
player_facing_right = pygame.image.load('photos/player_facing_right.png')
player_move_left = pygame.image.load('photos/player_move_left.png')
player_move_left2 = pygame.image.load('photos/player_move_left2.png')
player_move_right = pygame.image.load('photos/player_move_right.png')
player_move_right2 = pygame.image.load('photos/player_move_right2.png')
player_jump_left = pygame.image.load('photos/player_jump_left.png')
player_jump_right = pygame.image.load('photos/player_jump_right.png')
player_animation_list = [player_facing_left, player_facing_right, player_move_left, player_move_left2, player_move_right, player_move_right2, player_jump_left, player_jump_right]

night_surface = pygame.Surface([length, height])

night_surface.fill(B)


num_clouds = 100

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



def draw_rainbow():
    rainbow_list = []
    rainbow_color = R
    rainbow_line = 0
    red_val = 255
    green_val= 0
    blue_val = 0
    while rainbow_color != O:
        rainbow_list += rainbow_color
        red_val +=1
        

    line_colors = []
    return line_colors


#Making Rain
rain = []
for i in range(1000):
    x = -10
    y = 610
    r = random.randrange(1, 5)
    e = random.randint(400, 800)
    s = [x, y, r, r, e]
    rain.append(s)


    
time = -500
time_past = 5
time_motion = 0
player_x_pos = 0
player_y_pos = 0
x_motion = 0
y_motion = 0
player2_x_pos = 0
player2_y_pos = 0
x2_motion = 0
y2_motion = 0
foot_on = 0
ground = 400
lightning_count = 0
lightning_flash = False
raining = False
facing_left = True
facing_right = False


length_in_pixels = 200
size_of_pixel = length/length_in_pixels


# Game loop
done = False
first = True
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                time_past = -time_past+5
            if event.key == pygame.K_m:
                time = -400
            if event.key == pygame.K_n:
                time = 400
            if event.key == pygame.K_o:
                time_motion -= 5
            if event.key == pygame.K_p:
                time_motion += 5

            if event.key == pygame.K_r:
                raining = not raining
            if event.key == pygame.K_f:
                if raining:
                    lightning_flash = True
            
            if event.key == pygame.K_UP:
                if player_y_pos == ground:
                    y_motion -= 9.8
                    
            if event.key == pygame.K_DOWN:
                y_motion += 19.6
            if event.key == pygame.K_RIGHT:
                x_motion = 5
                facing_right = True
                facing_left = False
            if event.key == pygame.K_LEFT:
                x_motion = -5
                facing_right = False
                facing_left = True
            
            
            if event.key == pygame.K_w:
                if player2_y_pos == ground:
                    y2_motion -= 9.8
            if event.key == pygame.K_s:
                y2_motion += 19.6
            if event.key == pygame.K_d:
                x2_motion = 5
            if event.key == pygame.K_a:
                x2_motion = -5

                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_motion = 0
            if event.key == pygame.K_DOWN:
                y_motion = 0
            if event.key == pygame.K_RIGHT:
                x_motion = 0
            if event.key == pygame.K_LEFT:
                x_motion = 0

        
            if event.key == pygame.K_w:
                y2_motion = 0
            if event.key == pygame.K_s:
                y2_motion = 0
            if event.key == pygame.K_d:
                x2_motion = 0
            if event.key == pygame.K_a:
                x2_motion = 0

            
            if event.key == pygame.K_o:
                time_motion = 0
            if event.key == pygame.K_p:
                time_motion = 0

    '''player 1'''
    if player_y_pos < ground-200:
        y_motion = 9.8
        
    if player_x_pos < 0:
        player_x_pos = 0
        
    if player_x_pos+64 > 800:
        player_x_pos = 800-64
        
    player_x_pos += x_motion
    player_y_pos += y_motion
    
    '''player 2'''
    if player2_y_pos < ground-200:
        y2_motion = 9.8
        
    if player2_x_pos < 0:
        player2_x_pos = 0
        
    if player2_x_pos+64 > 800:
        player2_x_pos = 800-64
        
    player2_x_pos += x2_motion
    player2_y_pos += y2_motion




    
        
    if facing_right == True:
        player_pose = 1
        if player_y_pos < ground:
            player_pose = 7
        elif x_motion > 0:
            foot_on += 1
            if foot_on <= 20:
                player_pose = 4
    
            else:
                player_pose = 5
                if foot_on >= 40:
                    foot_on = 0
                
    if facing_left == True:
        player_pose = 0
        if player_y_pos < ground:
            player_pose = 6
        elif x_motion < 0:
            foot_on += 1
            if foot_on <= 20:
                player_pose = 2
        
            else:
                player_pose = 3
                if foot_on >= 40:
                    foot_on = 0
                
    

    time += time_motion
    
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
    
    if abs(sun_y)+300>400:
        sunset = 300
    else:
        sunset = 1000
    '''player 1'''
    if y_motion == 0:
    
        if player_y_pos < ground:
            player_y_pos += 9.8
    if player_y_pos > ground:
        player_y_pos = ground

    '''player 2'''
    if y2_motion == 0:
    
        if player2_y_pos < ground:
            player2_y_pos += 9.8
    if player2_y_pos > ground:
        player2_y_pos = ground

    ''' rain '''
    for r in rain:
        r[0] -= r[2]
        r[1] += r[2]

        if r[1] > r[4]:
            r[0] = random.randrange(-10, 1600)
            r[1] = random.randrange(-600, -10)

            
    # Drawing code
   
     
    ''' sky '''
    screen.fill(sky)
    shadow = 0
    


    
    ''' rainbow '''
    for y in range(height):
        red_val = int(b[0] + (R[0] - b[0]) * y/height)
        green_val = int(b[1] + (R[1] - b[1]) * y/height)
        blue_val = int(b[2] + (R[2] - b[2]) * y/height)

        pygame.draw.line(screen, [red_val, green_val, blue_val], [0,y], [length,y])    
        
    if raining == True:
        screen.fill(l)
        shadow = 100
     
    ''' sun '''
    pygame.draw.ellipse(screen, Y, [time+400, 75 + sun_y , 100, 100])
    time += time_past
    if time >= 1000:
        time = -999
    if time <= -1000:
        time = 999


    '''lightning'''
    if raining:
        random_lightning = random.randrange(1,100)
        if random_lightning == 50:
            lightning_flash = True
        if lightning_flash == True:
            lightning_count +=1
            screen.fill(W)
            if lightning_count == 5:
                lightning_flash = False
                lightning_count = 0
                thunder.play()
    
    
    ''' clouds '''
    cloud_counter = 0
    for f in far_clouds:
        cloud_counter +=1
        if raining == True:
            draw_far_cloud(f)
        elif cloud_counter%5 == 0:
            draw_far_cloud(f)
        
    for c in close_clouds:
        cloud_counter +=1
        if raining == True:
            draw_close_cloud(c)
        elif cloud_counter%5 == 0:
            draw_close_cloud(c)

    
    ''' sunset '''
    '''
    pygame.draw.rect(screen, R, [0, sunset, 800, 200])
    '''

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
    
    
    screen.blit(player_animation_list[player_pose], ((player_x_pos), (player_y_pos)))
    


        
    ''' player2 '''
    
    
    screen.blit(player_animation_list[player_pose], ((player_x_pos), (player_y_pos)))
    

    
    
    ''' rain '''
    if raining == True:
        pygame.mixer.music.play(-1)
        for s in rain:
            pygame.draw.ellipse(screen, S, s[0:4])

    else:
        pygame.mixer.music.stop()
        
    if sun_y<400:
        night_surface.set_alpha(abs(sun_y/1.7)+shadow)
        if abs(sun_y/1.7)+shadow > 235:
            night_surface.set_alpha(235)
    else:
        night_surface.set_alpha(235)
        
   

        
    screen.blit(night_surface,[0,0])
    
    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
