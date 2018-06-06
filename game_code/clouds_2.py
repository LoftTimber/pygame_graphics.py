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
DARKERWHITE = (235, 245, 255) #DARKERWHITE
B = (0, 0, 0)       #BLACK
o = (255,80,0)      #DARKERORANGE
g = (34, 139, 34)   #FORESTGREEN

thunder = pygame.mixer.Sound('sounds/thunder.ogg')
pygame.mixer.music.load('sounds/rain.ogg')


p_facing_left = pygame.image.load('photos/player_facing_left.png')
p_facing_right = pygame.image.load('photos/player_facing_right.png')
p_move_left = pygame.image.load('photos/player_move_left.png')
p_move_left2 = pygame.image.load('photos/player_move_left2.png')
p_move_right = pygame.image.load('photos/player_move_right.png')
p_move_right2 = pygame.image.load('photos/player_move_right2.png')
p_jump_left = pygame.image.load('photos/player_jump_left.png')
p_jump_right = pygame.image.load('photos/player_jump_right.png')
p1_animation_list = [p_facing_left, p_facing_right, p_move_left, p_move_left2, p_move_right, p_move_right2, p_jump_left, p_jump_right]
p2_animation_list = [p_facing_left, p_facing_right, p_move_left, p_move_left2, p_move_right, p_move_right2, p_jump_left, p_jump_right]
night_surface = pygame.Surface([length, height])

night_surface.fill(B)



def rect_rect(rect1, rect2):
    left1 = rect1[0]
    right1 = rect1[0] + rect1[2]
    top1 = rect1[1]
    bottom1 = rect1[1] + rect1[3]
    
    left2 = rect2[0]
    right2 = rect2[0] + rect2[2]
    top2 = rect2[1]
    bottom2 = rect2[1] + rect2[3]


    return not (right1 <= left2 or
                right2 <= left1 or
                bottom1 <= top2 or
                bottom2 <= top1)


''' Clouds '''
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
    
    pygame.draw.ellipse(screen, DARKERWHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARKERWHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARKERWHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, DARKERWHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, DARKERWHITE, [x + 20, y + 20, 60, 40])



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


foot_on = 0
p2_foot_on = 0
bottom_ground = 400
p1_ground = bottom_ground
p2_ground = bottom_ground
lightning_count = 0
gravity = .5
p1_speed = 5
p2_speed = 5
up_force = 0

lightning_flash = False
raining = False
facing_left = True
facing_right = False
p2_facing_left = True
p2_facing_right = False

length_in_pixels = 200
size_of_pixel = length/length_in_pixels

p1_hitbox = [0, 0, 64, 68]
p1_vel = [0, 0]

p2_hitbox = [400, 0, 64, 68]
p2_vel = [0, 0]

left_wall = 0
right_wall = 800
celling = 0

    


''' walls '''
wall1 =  [300, 260, 200, 50]
wall2 =  [600, 240, 200, 50]
wall3 =  [100, 350, 50, 200]


walls = [wall1, wall2, wall3]
#

# Game loop
done = False
first = True
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                if down and p1_landed:
                    p1_vel[1] = p1_up_force
                elif p1_landed:
                    p1_vel[1] = -9.8

            if event.key == pygame.K_w:
                if holding_s and p2_landed:
                    p2_vel[1] = p2_up_force
                elif p2_landed:
                    p2_vel[1] = -9.8
                
            if event.key == pygame.K_SPACE:
                time_past = -time_past+5
            if event.key == pygame.K_m:
                time = -bottom_ground
            if event.key == pygame.K_n:
                time = bottom_ground
            if event.key == pygame.K_o:
                time_motion -= 5
            if event.key == pygame.K_p:
                time_motion += 5

            if event.key == pygame.K_r:
                raining = not raining
            if event.key == pygame.K_f:
                if raining:
                    lightning_flash = True
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_t:
                if p1_landed:
                    p1_vel[1] = up_force
                
            
            
            if event.key == pygame.K_o:
                time_motion = 0
            if event.key == pygame.K_p:
                time_motion = 0



    state = pygame.key.get_pressed()

    up = state[pygame.K_t]
    down = state[pygame.K_DOWN]
    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]

    holding_w = state[pygame.K_w]
    holding_s = state[pygame.K_s]
    holding_a = state[pygame.K_a]
    holding_d = state[pygame.K_d]

    ''' p1 '''
    if p1_hitbox[1] >= p1_ground - p1_hitbox[3]:
    
        p1_landed = True
    else:
        p1_landed = False
        p1_up_force = 0
    
    
    
    if p1_vel[0] > 0:
        p1_vel[0] -= .1

    if p1_vel[0] < 0:
        p1_vel[0] += .1
        
    ''' p2 '''
    if p2_hitbox[1] >= p2_ground - p2_hitbox[3]:
    
        p2_landed = True
    else:
        p2_landed = False
        p2_up_force = 0
    
    
    
    if p2_vel[0] > 0:
        p2_vel[0] -= .1

    if p2_vel[0] < 0:
        p2_vel[0] += .1

        



                
    if holding_s:
        gravity = gravity*10
    if holding_d:
        p2_vel[0] = p2_speed
        p2_facing_right = True
        p2_facing_left = False
    if holding_a:
        p2_vel[0] = -p2_speed
        p2_facing_right = False
        p2_facing_left = True
    
        
        
        
    
    if down:
        
                
        if p1_landed and up_force >= -p1_hitbox[3] / 16:
            up_force -= p1_hitbox[3] / 16
        elif p1_landed and up_force >= -p1_hitbox[3] / 4:
            up_force -= .1

        
    
            
            
            
        
            
        
    


            
    if down:
        if p1_landed:
            p1_vel[0] = 0
        if not p1_landed:
            gravity = gravity*10

    if not down:
    
        if right:
            p1_vel[0] = p1_speed
            facing_right = True
            facing_left = False
        if left:
            p1_vel[0] = -p1_speed
            facing_right = False
            facing_left = True
        
        
    # Game logic
    


    
    

    
    
    
    
    p1_vel[1] += gravity
    p2_vel[1] += gravity
    gravity = .5

    
    
        
    time += time_motion
    
    
    
    
    p1_ground = bottom_ground
    p2_ground = bottom_ground
    
    
    

    
    
    
        
    
    
    ''' horizontal collision '''
    #player to player
    if rect_rect(p1_hitbox, p2_hitbox):
            p1_vel[0] = (p1_vel[0] + p2_vel[0]) / 2
            p2_vel[0] = (p1_vel[0] + p2_vel[0]) / 2
            if p1_hitbox[0] > p2_hitbox[0]:
                p1_hitbox[0] = p2_hitbox[0] - p1_hitbox[2]
            if p2_hitbox[0] > p1_hitbox[0]:
                p1_hitbox[0] = p2_hitbox[0] + p2_hitbox[2]
            
             
    p1_hitbox[0] += p1_vel[0]
    p2_hitbox[0] += p2_vel[0]
    
    #wall to player1
    for w in walls:
        if rect_rect(p1_hitbox, w):        
            if p1_vel[0] > 0:
                p1_hitbox[0] = w[0] - p1_hitbox[2]
            if p1_vel[0] < 0:
                p1_hitbox[0] = w[0] + w[2]
                
    #wall to player2
    for w in walls:
        if rect_rect(p2_hitbox, w):        
            if p2_vel[0] > 0:
                p2_hitbox[0] = w[0] - p2_hitbox[2]
            if p2_vel[0] < 0:
                p2_hitbox[0] = w[0] + w[2]
                
   
    
    
    
           

    


    ''' vertical collision '''
    p1_hitbox[1] += p1_vel[1]
    p2_hitbox[1] += p2_vel[1]
    
    #wall to player1
    for w in walls:
        if rect_rect(p1_hitbox, w):
            if p1_vel[1] > 0:
                p1_hitbox[1] = w[1] - p1_hitbox[3]
                p1_ground = w[1]
                
            if p1_vel[1] < 0:
                p1_hitbox[1] = w[1] + w[3] 
                p1_vel[1] = 0

    #wall to player2
    for w in walls:
        if rect_rect(p2_hitbox, w):
            if p2_vel[1] > 0:
                p2_hitbox[1] = w[1] - p2_hitbox[3]
                p2_ground = w[1]
                
            if p2_vel[1] < 0:
                p2_hitbox[1] = w[1] + w[3] 
                p2_vel[1] = 0

    #player to player1
    if rect_rect(p1_hitbox, p2_hitbox):
        p1_vel[1] = (p1_vel[1] + p2_vel[1]) / 2
        p2_vel[1] = (p2_vel[1] + p1_vel[1]) / 2
            
                
                
            
                
    


    
                
    
        
    '''player 1'''
    
        
    if p1_hitbox[0] < left_wall:
        p1_hitbox[0] = left_wall
        
        
    if p1_hitbox[0] > right_wall-p1_hitbox[2]:
        p1_hitbox[0] = right_wall-p1_hitbox[2]
        
    
    
    
    '''player 2'''
    if p2_hitbox[0] < left_wall:
        p2_hitbox[0] = left_wall
        
        
    if p2_hitbox[0] > right_wall-p2_hitbox[2]:
        p2_hitbox[0] = right_wall-p2_hitbox[2]
        
    




    
    ''' player 1 '''
    if facing_right == True:
        p1_pose = 1
        if p1_hitbox[1] < p1_ground-p1_hitbox[3]:
            p1_pose = 7
        elif p1_vel[0] > 0:
            foot_on += 1
            if foot_on <= 20:
                p1_pose = 4
    
            else:
                p1_pose = 5
                if foot_on >= 40:
                    foot_on = 0
                
    if facing_left == True:
        p1_pose = 0
        if p1_hitbox[1] < p1_ground-p1_hitbox[3]:
            p1_pose = 6
        elif p1_vel[0] < 0:
            foot_on += 1
            if foot_on <= 20:
                p1_pose = 2
        
            else:
                p1_pose = 3
                if foot_on >= 40:
                    foot_on = 0



    ''' player 2 '''
    if p2_facing_right == True:
        p2_pose = 1
        if p2_hitbox[1] < p2_ground-p2_hitbox[3]:
            p2_pose = 7
        elif p2_vel[0] > 0:
            foot_on += 1
            if foot_on <= 20:
                p2_pose = 4
    
            else:
                p2_pose = 5
                if foot_on >= 40:
                    foot_on = 0
                
    if p2_facing_left == True:
        p2_pose = 0
        if p2_hitbox[1] < p2_ground-p2_hitbox[3]:
            p2_pose = 6
        elif p2_vel[0] < 0:
            foot_on += 1
            if foot_on <= 20:
                p2_pose = 2
        
            else:
                p2_pose = 3
                if foot_on >= 40:
                    foot_on = 0
                
    
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
    
    if p1_hitbox[1] >= p1_ground-p1_hitbox[3]:
        p1_hitbox[1] = p1_ground-p1_hitbox[3]
        p1_vel[1] = 0

    ''' p2 '''
    if p2_hitbox[1] >= p2_ground-p2_hitbox[3]:
        p2_hitbox[1] = p2_ground-p2_hitbox[3]
        p2_vel[1] = 0

    

    ''' rain '''
    for r in rain:
        r[0] -= r[2]
        r[1] += r[2]

        if r[1] > r[4]:
            r[0] = random.randrange(-10, 1600)
            r[1] = random.randrange(-600, -10)

    if rect_rect(p1_hitbox, p2_hitbox):
            
            pass
    

    
    
    
    
    
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
    pygame.draw.rect(screen, G, [0, bottom_ground, 800, 200])

    ''' fence 
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, W, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, W, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, W, [0, 410], [800, 410], 5)
    '''
    


    
    ''' player '''
    
    
    screen.blit(p1_animation_list[p1_pose], ((p1_hitbox[0]), (p1_hitbox[1])))
    


        
    ''' player2 '''
    
    
    screen.blit(p2_animation_list[p2_pose], ((p2_hitbox[0]), (p2_hitbox[1])))
    

    
    
    ''' rain '''
    if raining == True:
        pygame.mixer.music.play(-1)
        for s in rain:
            pygame.draw.ellipse(screen, S, s[0:4])

    else:
        pygame.mixer.music.stop()
        
    if sun_y<bottom_ground:
        night_surface.set_alpha(abs(sun_y/1.7)+shadow)
        if abs(sun_y/1.7)+shadow > 235:
            night_surface.set_alpha(235)
    else:
        night_surface.set_alpha(235)
        
   
    for w in walls:
        pygame.draw.rect(screen, R, w)
        
    screen.blit(night_surface,[0,0])
    
    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
