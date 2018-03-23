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




##p_facing_left = pygame.image.load('photos/player_facing_left.png')
##p_facing_right = pygame.image.load('photos/player_facing_right.png')
##p_move_left = pygame.image.load('photos/player_move_left.png')
##p_move_left2 = pygame.image.load('photos/player_move_left2.png')
##p_move_right = pygame.image.load('photos/player_move_right.png')
##p_move_right2 = pygame.image.load('photos/player_move_right2.png')
##p_jump_left = pygame.image.load('photos/player_jump_left.png')
##p_jump_right = pygame.image.load('photos/player_jump_right.png')
##p1_animation_list = [p_facing_left, p_facing_right, p_move_left, p_move_left2, p_move_right, p_move_right2, p_jump_left, p_jump_right]
##p2_animation_list = [p_facing_left, p_facing_right, p_move_left, p_move_left2, p_move_right, p_move_right2, p_jump_left, p_jump_right]
##night_surface = pygame.Surface([length, height])





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

def to_left(rect1, rect2):
    left1 = rect1[0]
    right1 = rect1[0] + rect1[2]
    top1 = rect1[1]
    bottom1 = rect1[1] + rect1[3]
    
    left2 = rect2[0]
    right2 = rect2[0] + rect2[2] +1
    top2 = rect2[1]
    bottom2 = rect2[1] + rect2[3]


    return not (right1 <= left2 or
                right2 <= left1 or
                bottom1 <= top2 or
                bottom2 <= top1)


def to_right(rect1, rect2):
    left1 = rect1[0]
    right1 = rect1[0] + rect1[2] +1
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
    

def is_above(rect1, rect2):   
    left1 = rect1[0]
    right1 = rect1[0] + rect1[2]
    top1 = rect1[1]
    bottom1 = rect1[1] + rect1[3]
    
    left2 = rect2[0]
    right2 = rect2[0] + rect2[2]
    top2 = rect2[1]
    bottom2 = rect2[1] + rect2[3] +1


    return not (right1 <= left2 or
                right2 <= left1 or
                bottom1 <= top2 or
                bottom2 <= top1)


def is_below(rect1, rect2):
    left1 = rect1[0]
    right1 = rect1[0] + rect1[2]
    top1 = rect1[1]
    bottom1 = rect1[1] + rect1[3] +1
    
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

p1_facing_up = True
p1_facing_down = False
p1_facing_right = False
p1_facing_left = False

p2_facing_up = True
p2_facing_down = False
p2_facing_right = False
p2_facing_left = False

length_in_pixels = 200
size_of_pixel = length/length_in_pixels

p1_hitbox = [0, 0, 25, 25]
p1_vel = [0, 0]

p2_hitbox = [400, 0, 25, 25]
p2_vel = [0, 0]

left_wall = 0
right_wall = 800
celling = 0
ground = 600

metronome = 120
beat = 0
p1_hp = 10
p2_hp = 10

    


''' walls '''
wall1 =  [300, 250, 200, 50]
wall2 =  [600, 150, 200, 50]
wall3 =  [100, 300, 50, 200]
wall4 =  [0, -1, 800, 1]
wall5 =  [-1, 0, 1, 600]
wall6 =  [0, 600, 800, 1]
wall7 =  [800, 0, 1, 600]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]
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
            
    sixteenth = int((refresh_rate**2/metronome)/4)
    eighth = sixteenth*2
    quarter = sixteenth*4
    
    
    
    
    
    
    p1_beat = quarter
    p2_beat = quarter

    
    
    
    
    
    
    
    state = pygame.key.get_pressed()

    up = False
    down = False
    left = False
    right = False
    p1_attack = False
    #eighth beat
    if (beat)%(int(p1_beat)) == 0:
        up = state[pygame.K_UP]
        down = state[pygame.K_DOWN]
        left = state[pygame.K_LEFT]
        right = state[pygame.K_RIGHT]
        p1_attack = state[pygame.K_PAGEDOWN]


    holding_w = False
    holding_s = False
    holding_a = False
    holding_d = False
    p2_attack = False
    #quarter beat
    if beat%(int(p2_beat)) == 0:
        holding_w = state[pygame.K_w]
        holding_s = state[pygame.K_s]
        holding_a = state[pygame.K_a]
        holding_d = state[pygame.K_d]
        p2_attack = state[pygame.K_e]

    p1_vel[0] = 0
    p1_vel[1] = 0

    p2_vel[0] = 0
    p2_vel[1] = 0
        
    ground = ground



    
    #sixteenth beat
    

    p2_above_wall = False
    p2_below_wall = False
    p2_right_wall = False
    p2_left_wall = False
    p1_below_wall = False
    p1_above_wall = False
    p1_left_wall = False
    p1_right_wall = False

    can_up = False
    can_down = False
    can_left = False
    can_right = False

    can_holding_w = False
    can_holding_s = False
    can_holding_a = False
    can_holding_d = False
    


    
    for w in walls:
        #p2 is below
        if is_below(w, p2_hitbox):
            p2_below_wall = True


    for w in walls:
        #p2 is above
        if is_above(w, p2_hitbox):
            p2_above_wall = True
            

    for w in walls:
        #p2 to left
        if to_left(w, p2_hitbox):
            p2_left_wall = True


    for w in walls:
        # p2 to right
        if to_right(w, p2_hitbox):
            p2_right_wall = True


    for w in walls:
        # p1 is below
        if is_below(w, p1_hitbox):
            p1_below_wall = True


    for w in walls:
        #  p1 is above
        if is_above(w, p1_hitbox):
            p1_above_wall = True


    for w in walls:
        # p1 to left
        if to_left(w, p1_hitbox):
            p1_left_wall = True


    for w in walls:
        # p1 to right
        if to_right(w, p1_hitbox):
            p1_right_wall = True



    if (not is_below(p2_hitbox, p1_hitbox)) or ((holding_w and p2_below_wall == False) or \
        (holding_d and p2_left_wall == False) or (holding_a and p2_right_wall == False)):
        can_up = True

    if (not is_above(p2_hitbox, p1_hitbox)) or ((holding_s and p2_above_wall == False) or \
        (holding_d and p2_left_wall == False) or (holding_a and p2_right_wall == False)):
        can_down = True

    if (not to_left(p2_hitbox, p1_hitbox)) or ((holding_w and p2_below_wall == False) or \
        (holding_s and p2_above_wall == False) or (holding_d and p2_left_wall == False)):
        can_right = True

    if (not to_right(p2_hitbox, p1_hitbox)) or ((holding_w and p2_below_wall == False) or \
        (holding_s and p2_above_wall == False) or (holding_a and p2_right_wall == False)):
        can_left = True

    if (not is_below(p1_hitbox, p2_hitbox)) or ((up and p1_below_wall == False) or \
        (right and p1_left_wall == False) or (left and p1_right_wall == False)):
        can_holding_w = True

    if (not is_above(p1_hitbox, p2_hitbox)) or ((down and p1_above_wall == False) or \
        (right and p1_left_wall == False) or (left and p1_right_wall == False)):
        can_holding_s = True

    if (not to_left(p1_hitbox, p2_hitbox)) or ((up and p1_below_wall == False) or \
        (down and p1_above_wall == False) or (right and p1_left_wall == False)):
        can_holding_d = True

    if (not to_right(p1_hitbox, p2_hitbox)) or ((up and p1_below_wall == False) or \
        (down and p1_above_wall == False) or (left and p1_right_wall == False)):
        can_holding_a = True
            

        
    #eighth beat
    if (beat)%(int(p1_beat)) == 0:######################################################################## make weapon hitbox ###
        weapon_swing = False
        if p1_attack:
            weapon_swing = True
            if is_below(p2_hitbox, p1_hitbox) or is_above(p2_hitbox, p1_hitbox) or to_left(p2_hitbox, p1_hitbox) or to_right(p2_hitbox, p1_hitbox):
                print("attack")
            
        
        if (up and not p1_attack):
            p1_facing_up = True
            p1_facing_down = False
            p1_facing_right = False
            p1_facing_left = False
            if can_up:
                 p1_vel[1] = -p1_hitbox[2]
            else:
                print("hit")
            
        
        if (down and not (up or p1_attack)):
            p1_facing_up = False
            p1_facing_down = True
            p1_facing_right = False
            p1_facing_left = False
            if can_down:
                p1_vel[1] = p1_hitbox[2]
            else:
                print("hit")
                

        if (right and not (up or down or p1_attack)):
            p1_facing_up = False
            p1_facing_down = False
            p1_facing_right = True
            p1_facing_left = False
            if can_right:
                p1_vel[0] = p1_hitbox[2]
            else:
                print("hit")
                

        if (left and not (up or down or right or p1_attack)):
            p1_facing_up = False
            p1_facing_down = False
            p1_facing_right = False
            p1_facing_left = True
            if can_left:
                p1_vel[0] = -p1_hitbox[2]
            else:
                print("hit")

    
        #quarter beat
    if beat%(int(p2_beat)) == 0:

        if p2_attack:
            print("attack")
        
        if holding_w and not p2_attack:
            p2_facing_up = True
            p2_facing_down = False
            p2_facing_right = False
            p2_facing_left = False
            if can_holding_w:
                p2_vel[1] = -p2_hitbox[2]
            else:
                print("hit")


        if (holding_s and not (holding_w or p2_attack)):
            p2_facing_up = False
            p2_facing_down = True
            p2_facing_right = False
            p2_facing_left = False
            if can_holding_s:
                p2_vel[1] = p2_hitbox[2]
            else:
                print("hit")


        if (holding_d and not (holding_w or holding_s or p2_attack)):
            p2_facing_up = False
            p2_facing_down = False
            p2_facing_right = True
            p2_facing_left = False
            if can_holding_d:
                p2_vel[0] = p2_hitbox[2]
            else:
                print("hit")
                

        if (holding_a and not (holding_w or holding_s or holding_d or p2_attack)):
            p2_facing_up = False
            p2_facing_down = False
            p2_facing_right = False
            p2_facing_left = True
            if can_holding_a:
                p2_vel[0] = -p2_hitbox[2]
            else:
               print("hit")


        
                
    
    beat += 1
    
        
    # Game logic
    

    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
        
    
    
    ''' horizontal collision '''
    
            
            
             
    p1_hitbox[0] += p1_vel[0]
    p2_hitbox[0] += p2_vel[0]

    p1_hitbox[1] += p1_vel[1]
    p2_hitbox[1] += p2_vel[1]

    
        
            
        
    
    #wall to player1
    for w in walls:
        if rect_rect(p1_hitbox, w):        
            if p1_facing_right:
                p1_hitbox[0] = w[0] - p1_hitbox[2]
            if p1_facing_left:
                p1_hitbox[0] = w[0] + w[2]
                
    #wall to player2
    for w in walls:
        if rect_rect(p2_hitbox, w):        
            if p2_facing_right:
                p2_hitbox[0] = w[0] - p2_hitbox[2]
            if p2_facing_left:
                p2_hitbox[0] = w[0] + w[2]


    #player to player
    if rect_rect(p1_hitbox, p2_hitbox):
        print("no")
        
        
        
        

        if p2_vel[0] > 0:
            p2_hitbox[0] = p2_hitbox[0] - p2_hitbox[2]
            
        

        if p2_vel[0] < 0:
            p2_hitbox[0] = p2_hitbox[0] + p2_hitbox[2]

            
##        elif p2_facing_right:
##            p2_hitbox[0] = p1_hitbox[0] - p2_hitbox[2]
##        elif p2_facing_left:
##            p2_hitbox[0] = p1_hitbox[0] + p1_hitbox[2]
   
    
    
    
           

    


    ''' vertical collision '''
    

    
    
    #wall to player1
    for w in walls:
        if rect_rect(p1_hitbox, w):
            if p1_facing_down:
                p1_hitbox[1] = w[1] - p1_hitbox[3]
                
                
            if p1_facing_up:
                p1_hitbox[1] = w[1] + w[3] 
                p1_vel[1] = 0

    #wall to player2
    for w in walls:
        if rect_rect(p2_hitbox, w):
            if p2_facing_down:
                p2_hitbox[1] = w[1] - p2_hitbox[3]
                
                
            if p2_facing_up:
                p2_hitbox[1] = w[1] + w[3] 
                p2_vel[1] = 0


    #player to player1
    if rect_rect(p1_hitbox, p2_hitbox):
        print("no")
        
        
        if p2_facing_down:
            p2_hitbox[1] = p1_hitbox[1] - p2_hitbox[3]
        if p2_facing_up:
            p2_hitbox[1] = p1_hitbox[1] + p1_hitbox[3]

    
            
                
                
            
                
    


    
                
    
        
    '''player 1'''
    
        
##    if p1_hitbox[0] < left_wall:
##        p1_hitbox[0] = left_wall
##        
##        
##    if p1_hitbox[0] > right_wall-p1_hitbox[2]:
##        p1_hitbox[0] = right_wall-p1_hitbox[2]
##        
##    
##    
##    
##    '''player 2'''
##    if p2_hitbox[0] < left_wall:
##        p2_hitbox[0] = left_wall
##        
##        
##    if p2_hitbox[0] > right_wall-p2_hitbox[2]:
##        p2_hitbox[0] = right_wall-p2_hitbox[2]
        
    




    
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
                
    
    

        
##    '''player 1'''
##    
##    if p1_hitbox[1] >= ground-p1_hitbox[3]:
##        p1_hitbox[1] = ground-p1_hitbox[3]
##        p1_vel[1] = 0
##
##    ''' p2 '''
##    if p2_hitbox[1] >= ground-p2_hitbox[3]:
##        p2_hitbox[1] = ground-p2_hitbox[3]
##        p2_vel[1] = 0

    

    

    
    

    
    
    
    
    
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

   
