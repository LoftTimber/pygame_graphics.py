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


lightning_count = 0




lightning_flash = False
raining = False
facing_left = True
facing_right = False
p2_facing_left = True
p2_facing_right = False

length_in_pixels = 200
size_of_pixel = length/length_in_pixels

p1_hitbox = [0, 0, 50, 50]
p1_vel = [0, 0]

p2_hitbox = [400, 0, 50, 50]
p2_vel = [0, 0]

left_wall = 0
right_wall = 800
celling = 0
ground = 600

metronome = 160
count = 0

    


''' walls '''
wall1 =  [300, 250, 200, 50]
wall2 =  [600, 150, 200, 50]
wall3 =  [100, 300, 50, 200]


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
            pass
                
            

            
                    
        if event.type == pygame.KEYUP:
            pass
            
            
    beat = (metronome/refresh_rate)
    
    

    
    
    
    state = pygame.key.get_pressed()

    up = state[pygame.K_UP]
    down = state[pygame.K_DOWN]
    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]

    holding_w = state[pygame.K_w]
    holding_s = state[pygame.K_s]
    holding_a = state[pygame.K_a]
    holding_d = state[pygame.K_d]

    p1_vel[0] = 0
    p1_vel[1] = 0

    p2_vel[0] = 0
    p2_vel[1] = 0
        
    ground = ground
    if int(refresh_rate/beat) == count:
        
        count = 0
        

        ''' p1 up '''
        at_wall = False
        for w in walls:
                if p2_hitbox[1] == w[1]+w[3]:
                    at_wall == True
                    print("at_wall")
        if not(p1_hitbox[1] == p2_hitbox[1] + p2_hitbox[3] and p1_hitbox[0] == p2_hitbox[0]) or holding_w:
            
                    
            if up and at_wall == False:
                p1_vel[1] = -50
        elif up:
            print("hit")


            
        ''' p1 down '''
        if not(p1_hitbox[1] == p2_hitbox[1] - p1_hitbox[3] and p1_hitbox[0] == p2_hitbox[0]) or (holding_s and not (p2_hitbox[1]+p2_hitbox[3] == wall1[1] or p2_hitbox[1]+p2_hitbox[3] == wall3[1])):
            if down:
                p1_vel[1] = 50
        elif down:
            print("hit")



        ''' p1 right '''
        if not(p1_hitbox[0] == p2_hitbox[0] - p1_hitbox[2] and p1_hitbox[1] == p2_hitbox[1]) or (holding_d and not (p2_hitbox[0]+p2_hitbox[2] == wall1[0] or p2_hitbox[0]+p2_hitbox[2] == wall3[0])):
            if not(up or down):
                if right:
                    p1_vel[0] = 50
        elif right:
            print("hit")



        ''' p1 left '''    
        if not(p1_hitbox[0] == p2_hitbox[0] + p2_hitbox[2] and p1_hitbox[1] == p2_hitbox[1]) or (holding_a and not (p2_hitbox[0] == wall1[0]+wall1[2] or p2_hitbox[0] == wall3[0]+wall3[2])):
            if not(up or down):
                if left:
                    p1_vel[0] = -50
        elif left:
            print("hit")



        ''' p2 up '''
        if not(p1_hitbox[1] == p2_hitbox[1] - p1_hitbox[3] and p1_hitbox[0] == p2_hitbox[0]) or (up and not (p1_hitbox[1] == wall1[1]+wall1[3] or p1_hitbox[1] == wall3[1]+wall3[3])):
            if holding_w:
                p2_vel[1] = -50
        elif holding_w:
            print("hit")



        ''' p2 down '''
        if not(p1_hitbox[1] == p2_hitbox[1] + p2_hitbox[3] and p1_hitbox[0] == p2_hitbox[0]) or (down and not (p1_hitbox[1]+p1_hitbox[3] == wall1[1] or p1_hitbox[1]+p1_hitbox[3] == wall3[1])):
            if holding_s:
                p2_vel[1] = 50
        elif holding_s:
            print("hit")



        ''' p2 right '''
        if not(p1_hitbox[0] == p2_hitbox[0] + p2_hitbox[2] and p1_hitbox[1] == p2_hitbox[1]) or (right and not (p1_hitbox[0]+p1_hitbox[2] == wall1[0] or p1_hitbox[0]+p1_hitbox[2] == wall3[0])):
            if not(holding_w or holding_s):
                if holding_d:
                    p2_vel[0] = 50
        elif holding_d:
            print("hit")



        ''' p2 left '''
        if not(p1_hitbox[0] == p2_hitbox[0] - p1_hitbox[2] and p1_hitbox[1] == p2_hitbox[1]) or (left and not (p1_hitbox[0] == wall1[0]+wall1[2] or p1_hitbox[0] == wall3[0]+wall3[2])):
            if not(holding_w or holding_s):
                if holding_a:
                    p2_vel[0] = -50
        elif holding_a:
            print("hit")
                
    
    count += 1
        
    # Game logic
    

    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
        
    
    
    ''' horizontal collision '''
    
            
            
             
    p1_hitbox[0] += p1_vel[0]
    p2_hitbox[0] += p2_vel[0]

    #player to player
    if rect_rect(p1_hitbox, p2_hitbox):
        
        if p1_vel[0] > 0:
            p1_hitbox[0] = p2_hitbox[0] - p1_hitbox[2]
        elif p1_vel[0] < 0:
            p1_hitbox[0] = p2_hitbox[0] + p2_hitbox[2]
        elif p2_vel[0] > 0:
            p2_hitbox[0] = p1_hitbox[0] - p2_hitbox[2]
        elif p2_vel[0] < 0:
            p2_hitbox[0] = p1_hitbox[0] + p1_hitbox[2]
            
        
    
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

    #player to player1
    if rect_rect(p1_hitbox, p2_hitbox):
        if p1_vel[1] > 0:
            p1_hitbox[1] = p2_hitbox[1] - p1_hitbox[3]
        if p1_vel[1] < 0:
            p1_hitbox[1] = p2_hitbox[1] + p2_hitbox[3]
        if p2_vel[1] > 0:
            p2_hitbox[1] = p1_hitbox[1] - p2_hitbox[3]
        if p2_vel[1] < 0:
            p2_hitbox[1] = p1_hitbox[1] + p1_hitbox[3]
    
    #wall to player1
    for w in walls:
        if rect_rect(p1_hitbox, w):
            if p1_vel[1] > 0:
                p1_hitbox[1] = w[1] - p1_hitbox[3]
                
                
            if p1_vel[1] < 0:
                p1_hitbox[1] = w[1] + w[3] 
                p1_vel[1] = 0

    #wall to player2
    for w in walls:
        if rect_rect(p2_hitbox, w):
            if p2_vel[1] > 0:
                p2_hitbox[1] = w[1] - p2_hitbox[3]
                
                
            if p2_vel[1] < 0:
                p2_hitbox[1] = w[1] + w[3] 
                p2_vel[1] = 0

    
            
                
                
            
                
    


    
                
    
        
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
        if p1_hitbox[1] < ground-p1_hitbox[3]:
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
        if p1_hitbox[1] < ground-p1_hitbox[3]:
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
        if p2_hitbox[1] < ground-p2_hitbox[3]:
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
        if p2_hitbox[1] < ground-p2_hitbox[3]:
            p2_pose = 6
        elif p2_vel[0] < 0:
            foot_on += 1
            if foot_on <= 20:
                p2_pose = 2
        
            else:
                p2_pose = 3
                if foot_on >= 40:
                    foot_on = 0
                
    
    

        
    '''player 1'''
    
    if p1_hitbox[1] >= ground-p1_hitbox[3]:
        p1_hitbox[1] = ground-p1_hitbox[3]
        p1_vel[1] = 0

    ''' p2 '''
    if p2_hitbox[1] >= ground-p2_hitbox[3]:
        p2_hitbox[1] = ground-p2_hitbox[3]
        p2_vel[1] = 0

    

    

    
    

    
    
    
    
    
    # Drawing code
   
     
    ''' sky '''
    screen.fill(B)
    
    
    


    
    ''' player '''
    
    
    pygame.draw.rect(screen, V, [p1_hitbox[0], p1_hitbox[1], p1_hitbox[2], p1_hitbox[3]])
    


        
    ''' player2 '''
    
    
    pygame.draw.rect(screen, G, [p2_hitbox[0], p2_hitbox[1], p2_hitbox[2], p2_hitbox[3]])
    

    
    
    
        
    
        
   
    for w in walls:
        pygame.draw.rect(screen, R, w)
        
    
    
    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
