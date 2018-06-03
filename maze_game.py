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
TITLE = "My maze game, but it is not finished yet."
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







f = (34, 139, 34)
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





''' player 1 '''
def p1_look_up():
    global p1_facing_up, p1_facing_down, p1_facing_right, p1_facing_left
    p1_facing_up = True
    p1_facing_down = False
    p1_facing_right = False
    p1_facing_left = False

def p1_look_down():
    global p1_facing_up, p1_facing_down, p1_facing_right, p1_facing_left
    p1_facing_up = False
    p1_facing_down = True
    p1_facing_right = False
    p1_facing_left = False

def p1_look_right():
    global p1_facing_up, p1_facing_down, p1_facing_right, p1_facing_left
    p1_facing_up = False
    p1_facing_down = False
    p1_facing_right = True
    p1_facing_left = False

def p1_look_left():
    global p1_facing_up, p1_facing_down, p1_facing_right, p1_facing_left
    p1_facing_up = False
    p1_facing_down = False
    p1_facing_right = False
    p1_facing_left = True

''' player 2 '''
def p2_look_up():
    global p2_facing_up, p2_facing_down, p2_facing_right, p2_facing_left
    p2_facing_up = True
    p2_facing_down = False
    p2_facing_right = False
    p2_facing_left = False

def p2_look_down():
    global p2_facing_up, p2_facing_down, p2_facing_right, p2_facing_left
    p2_facing_up = False
    p2_facing_down = True
    p2_facing_right = False
    p2_facing_left = False

def p2_look_right():
    global p2_facing_up, p2_facing_down, p2_facing_right, p2_facing_left
    p2_facing_up = False
    p2_facing_down = False
    p2_facing_right = True
    p2_facing_left = False

def p2_look_left():
    global p2_facing_up, p2_facing_down, p2_facing_right, p2_facing_left
    p2_facing_up = False
    p2_facing_down = False
    p2_facing_right = False
    p2_facing_left = True


    


foot_on = 0
p2_foot_on = 0








facing_left = True
facing_right = False
p2_facing_left = True
p2_facing_right = False

p1_look_up()

p2_look_up()

pixel_size = 10

p1_hitbox = [0, 0, pixel_size, pixel_size]
p1_vel = [0, 0]

p2_hitbox = [0, 0, pixel_size, pixel_size]
p2_vel = [0, 0]

left_wall = 0
right_wall = 800
celling = 0
ground = 600

metronome = 120
beat = 0
p1_hp = 10
p2_hp = 10

timer = 60

level = 1

p1_weapon_lenght = p1_hitbox[2]/2
p1_weapon_weigth = p1_hitbox[3]/2

p2_weapon_lenght = p2_hitbox[2]/2
p2_weapon_weigth = p2_hitbox[3]/2

p1_weapon_cooldown = 0
p2_weapon_cooldown = 0

start_screen = True
end_screen = False


    


''' walls '''
def level_1():
    
    block_line1 = [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line2 = [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line3 = [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line4 = [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line5 = [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line6 = [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line7 = [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line8 = [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line9 = [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line10= [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line11= [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line12= [R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R]
    block_line13= ["Front"]
    block_line14= [0,0,0,0,0,0,0,B,B]
    block_line15= [0,0,B,0,0,0,B,O,O,B,0,0,0,B]
    block_line16= [0,B,O,B,0,B,O,O,O,O,B,0,B,o,B]
    block_line17= [0,B,O,O,B,O,O,O,O,O,O,B,O,O,B]
    block_line18= [B,O,O,O,O,O,O,O,O,O,O,O,O,O,o,B]
    block_line19= [B,O,O,O,B,B,O,O,O,B,B,O,O,O,o,B]
    block_line20= [B,O,O,B,O,O,B,O,B,O,O,B,O,O,o,B]
    block_line21= [B,O,O,O,O,O,O,O,O,O,O,O,O,o,o,B]
    block_line22= [0,B,O,O,O,O,O,O,O,O,O,O,O,o,B]
    block_line23= [0,0,B,o,O,O,O,O,O,O,o,o,o,B]
    block_line24= [0,0,0,B,B,o,o,o,o,o,o,B,B]
    block_line25= [0,0,0,0,0,B,B,B,B,B,B]
    
    
    
    level_1_layout = [block_line1,block_line2,block_line3,block_line4,block_line5,block_line6,block_line7,block_line8,block_line9,block_line10,block_line11,block_line12,block_line13,block_line14,block_line15,block_line16,block_line17,block_line18,block_line19,block_line20,block_line21,block_line22,block_line23,block_line24,block_line25]
    return level_1_layout

def level_2():
    
    block_line1 = [O,O,O,O,O,O,O]
    block_line2 = [R,R,R,R,R]
    
    
    
    level_2_layout = [block_line1,block_line2]
    return level_2_layout

level_layout_list = [level_1(), level_2()]



#





def create_level(level_layout_list, level_on):
        global level_walls
        
        
        
        
        
        
        
            
        level_walls = []
        line = 0
        line2 = 0
        
        
    
        level_on_layout = level_layout_list[level_on-1]
        
        
        
        
        for i in range(len(level_on_layout)):
            pos = 0
            current_line = level_on_layout[line]
            if current_line == ["Front"]:
                line2 = line +1
                
            else:
                
            
                for i in range(len(current_line)):
                    block_type = current_line[pos]
                    if block_type == 0:
                        pass
                    else:
                        level_walls += [(pos*pixel_size), ((line-line2)*pixel_size), (pixel_size), (pixel_size), block_type],
                        
                    pos += 1

            line += 1


            
        
''' levels '''
def begin_level_1():
    global p1_hitbox, p2_hitbox
    
    p1_hitbox[0] = 0
    p1_hitbox[1] = 0
    p1_look_down()

    p2_hitbox[0] = 500
    p2_hitbox[1] = 50
    p2_look_up()

    
def begin_level_2():
    global p1_hitbox, p2_hitbox
    
    p1_hitbox[0] = 300
    p1_hitbox[1] = 50
    p1_look_right()

    p2_hitbox[0] = 450
    p2_hitbox[1] = 50
    p2_look_left()

class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 0
        self.hp = 10
        self.damage = 1
        self.weapon = "sword"
        
    def attack(self, other):
        if rect_rect(self.weapon, other):
            other.hp -= 1

    def move(self):
        if up:
            self.y -= self.speed
        if down:
            self.y += self.speed
        if right:
            self.x += self.speed
        if left:
            self.x -= self.speed

p1 = Player(0, 0, 3)
p2 = Player(400, 0, 3)

class Weapon:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.weapon_lenght = 25
        self.weapon_weigth = 25
        self.weapon_damage = 1
        self.weapon_cooldown = 2

sword = Weapon
        

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
                if start_screen == True:
                    level_on = 1
                    create_level(level_layout_list, level_on)
                    start_screen = False
                elif end_screen == True:
                    end_screen = False
                    start_screen = True
                else:
                    level_on = abs(level_on-3)
                    create_level(level_layout_list, level_on)

            
                    
        if event.type == pygame.KEYUP:
            pass

    if start_screen:
        print("Press space went ready")
        screen.fill(B)
        begin_level_1()
        p1_hp = 10
        p2_hp = 10
        
        

        timer = 60
        

        
        
    if not (start_screen or end_screen):
        
        sixteenth = int((refresh_rate**2/metronome)/4)
        eighth = sixteenth*2
        quarter = sixteenth*4
        
        
        
        
        
        
        p1_beat = sixteenth
        p2_beat = quarter

        
        
        
        
        
        
        
        state = pygame.key.get_pressed()

        up = False
        down = False
        left = False
        right = False
        
        #eighth beat
        if (beat)%(int(p1_beat)) == 0:
            p1_attack = False
            up = state[pygame.K_UP]
            down = state[pygame.K_DOWN]
            left = state[pygame.K_LEFT]
            right = state[pygame.K_RIGHT]
            p1_attack = state[pygame.K_PAGEDOWN]


        holding_w = False
        holding_s = False
        holding_a = False
        holding_d = False
        
        #quarter beat
        if beat%(int(p2_beat)) == 0:
            p2_attack = False
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

        
        


        
        for w in level_walls:
            if w[4] != R:
                # p2 is below
                if is_below(w, p2_hitbox):
                    p2_below_wall = True
                # p2 is above
                if is_above(w, p2_hitbox):
                    p2_above_wall = True
                # p2 to left
                if to_left(w, p2_hitbox):
                    p2_left_wall = True        
                # p2 to right
                if to_right(w, p2_hitbox):
                    p2_right_wall = True        
                # p1 is below            
                if is_below(w, p1_hitbox):
                    p1_below_wall = True      
                # p1 is above            
                if is_above(w, p1_hitbox):
                    p1_above_wall = True        
                # p1 to left
                if to_left(w, p1_hitbox):
                    p1_left_wall = True    
                # p1 to right
                if to_right(w, p1_hitbox):
                    p1_right_wall = True



        p2_go_up = (holding_w and p2_facing_up and p2_below_wall == False)
        



        if (not is_below(p2_hitbox, p1_hitbox)) or (p2_go_up or \
            (holding_d and p2_facing_right and p2_left_wall == False) or (holding_a and p2_facing_left and p2_right_wall == False)):
            can_up = True
        else:
            can_up = False

        if (not is_above(p2_hitbox, p1_hitbox)) or ((holding_s and p2_facing_down and p2_above_wall == False) or \
            (holding_d and p2_facing_right and p2_left_wall == False) or (holding_a and p2_facing_left and p2_right_wall == False)):
            can_down = True
        else:
            can_down = False

        if (not to_left(p2_hitbox, p1_hitbox)) or (p2_go_up or \
            (holding_s and p2_facing_down and p2_above_wall == False) or (holding_d and p2_facing_right and p2_left_wall == False)):
            can_right = True
        else:
            can_right = False

        if (not to_right(p2_hitbox, p1_hitbox)) or (p2_go_up or \
            (holding_s and p2_facing_down and p2_above_wall == False) or (holding_a and p2_facing_left and p2_right_wall == False)):
            can_left = True
        else:
            can_left = False

        if (not is_below(p1_hitbox, p2_hitbox)) or ((up and p1_facing_up and p1_below_wall == False) or \
            (right and p1_facing_right and p1_left_wall == False) or (left and p1_facing_left and p1_right_wall == False)):
            can_holding_w = True
        else:
            can_holding_w = False

        if (not is_above(p1_hitbox, p2_hitbox)) or ((down and p1_facing_down and p1_above_wall == False) or \
            (right and p1_facing_right and p1_left_wall == False) or (left and p1_facing_left and p1_right_wall == False)):
            can_holding_s = True
        else:
            can_holding_s = False

        if (not to_left(p1_hitbox, p2_hitbox)) or ((up and p1_facing_up and p1_below_wall == False) or \
            (down and p1_facing_down and p1_above_wall == False) or (right and p1_facing_right and p1_left_wall == False)):
            can_holding_d = True
        else:
            can_holding_d = False

        if (not to_right(p1_hitbox, p2_hitbox)) or ((up and p1_facing_up and p1_below_wall == False) or \
            (down and p1_facing_down and p1_above_wall == False) or (left and p1_facing_left and p1_right_wall == False)):
            can_holding_a = True
        else:
            can_holding_a = False
                

            
        #eighth beat
        if (beat)%(int(p1_beat)) == 0:
            
            
                
            
            if up:
                if not p1_attack:
                
                    if can_up:
                        if p1_facing_up:
                             p1_vel[1] = -p1_hitbox[2]
                    else:
                        print("hit")
                p1_look_up()
                    
                
            
            if (down and not up):
                if not p1_attack:
                    
                
                    if can_down:
                        if p1_facing_down:
                            p1_vel[1] = p1_hitbox[2]
                    else:
                        print("hit")
                p1_look_down()
                    

            if (right and not (up or down)):
                if not p1_attack:
                
                    if can_right:
                        if p1_facing_right:
                            p1_vel[0] = p1_hitbox[2]
                    else:
                        print("hit")
                p1_look_right()
                    

            if (left and not (up or down or right)):
                if not p1_attack:
                    
                
                    if can_left:
                        if p1_facing_left:
                            p1_vel[0] = -p1_hitbox[2]
                    else:
                        print("hit")
                p1_look_left()
                
        
        if beat%(int(eighth)) == 0:
            p1_weapon_cooldown -= 1
            if p1_weapon_cooldown <= 0:
                if p1_attack:
                    if p1_facing_up:
                        p1_weapon_hitbox = [p1_hitbox[0], p1_hitbox[1] - p1_weapon_lenght, p1_weapon_weigth, p1_weapon_lenght]
                    if p1_facing_down:
                        p1_weapon_hitbox = [p1_hitbox[0], p1_hitbox[1] + p1_hitbox[3], p1_weapon_weigth, p1_weapon_lenght]
                    if p1_facing_right:
                        p1_weapon_hitbox = [p1_hitbox[0] + p1_hitbox[2], p1_hitbox[1], p1_weapon_lenght, p1_weapon_weigth]
                    if p1_facing_left:
                        p1_weapon_hitbox = [p1_hitbox[0] - p1_weapon_lenght, p1_hitbox[1], p1_weapon_lenght, p1_weapon_weigth]
                        
                    p1_weapon_cooldown = 2
                else:
                    p1_weapon_hitbox = [0,0,0,0]
            else:
                p1_weapon_hitbox = [0,0,0,0]

                

        
            #quarter beat
        if beat%(int(p2_beat)) == 0:

            
            
            if holding_w:
                if not p2_attack:
                
                    if can_holding_w:
                        if p2_facing_up:
                             p2_vel[1] = -p2_hitbox[2]
                    else:
                        print("hit")
                p2_look_up()
                    
                
            
            if (holding_s and not holding_w):
                if not p2_attack:
                    
                
                    if can_holding_s:
                        if p2_facing_down:
                            p2_vel[1] = p2_hitbox[2]
                    else:
                        print("hit")
                p2_look_down()
                    

            if (holding_d and not (holding_w or holding_s)):
                if not p2_attack:
                
                    if can_holding_d:
                        if p2_facing_right:
                            p2_vel[0] = p2_hitbox[2]
                    else:
                        print("hit")
                p2_look_right()
                    

            if (holding_a and not (holding_w or holding_s or holding_d)):
                if not p2_attack:
                    
                
                    if can_holding_a:
                        if p2_facing_left:
                            p2_vel[0] = -p2_hitbox[2]
                    else:
                        print("hit")
                p2_look_left()

        if beat%(int(eighth)) == 0:
            p2_weapon_cooldown -= 1
            if p2_weapon_cooldown <= 0:
                if p2_attack:
                    if p2_facing_up:
                        p2_weapon_hitbox = [p2_hitbox[0], p2_hitbox[1] - p2_weapon_lenght, p2_weapon_weigth, p2_weapon_lenght]
                    if p2_facing_down:
                        p2_weapon_hitbox = [p2_hitbox[0], p2_hitbox[1] + p2_hitbox[3], p2_weapon_weigth, p2_weapon_lenght]
                    if p2_facing_right:
                        p2_weapon_hitbox = [p2_hitbox[0] + p2_hitbox[2], p2_hitbox[1], p2_weapon_lenght, p2_weapon_weigth]
                    if p2_facing_left:
                        p2_weapon_hitbox = [p2_hitbox[0] - p2_weapon_lenght, p2_hitbox[1], p2_weapon_lenght, p2_weapon_weigth]
                        
                    p2_weapon_cooldown = 2
                else:
                    p2_weapon_hitbox = [0,0,0,0]
            else:
                p2_weapon_hitbox = [0,0,0,0]


            
                    
        
        beat += 1
        
            
        # Game logic
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
            
        
        
        ''' horizontal collision '''
        
                
                
                 
        p1_hitbox[0] += p1_vel[0]
        p2_hitbox[0] += p2_vel[0]

        p1_hitbox[1] += p1_vel[1]
        p2_hitbox[1] += p2_vel[1]

        
            
                
            
        
        #wall to player1
        for w in level_walls:
            if w[4] != R:
                if rect_rect(p1_hitbox, w):        
                    if p1_facing_right:
                        p1_hitbox[0] = w[0] - p1_hitbox[2]
                    if p1_facing_left:
                        p1_hitbox[0] = w[0] + w[2]
                    
        #wall to player2
        for w in level_walls:
            if w[4] != R:
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
                
            

            elif p2_vel[0] < 0:
                p2_hitbox[0] = p2_hitbox[0] + p2_hitbox[2]
            else:
                p2_hitbox[0] = p2_hitbox[0] - p2_hitbox[2]

                
    ##        elif p2_facing_right:
    ##            p2_hitbox[0] = p1_hitbox[0] - p2_hitbox[2]
    ##        elif p2_facing_left:
    ##            p2_hitbox[0] = p1_hitbox[0] + p1_hitbox[2]
       
        
        
        
               

        


        ''' vertical collision '''
        

        
        
        #wall to player1
        for w in level_walls:
            if w[4] != R:
                if rect_rect(p1_hitbox, w):
                    if p1_facing_down:
                        p1_hitbox[1] = w[1] - p1_hitbox[3] 
                    if p1_facing_up:
                        p1_hitbox[1] = w[1] + w[3] 
                        p1_vel[1] = 0

        #wall to player2
        for w in level_walls:
            if w[4] != R:
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

        
                
                    
                    
        if (beat)%(int(eighth)) == 0:
            if rect_rect(p1_hitbox, p2_weapon_hitbox):
                p1_hp -= 1

            if rect_rect(p1_weapon_hitbox, p2_hitbox):
                p2_hp -= 1
           
        


        
##        print(p1_hp, p2_hp, timer)

        if p1_hp == 0 and p2_hp == 0:
            winner = "It is a tie"
            end_screen = True
        elif p1_hp == 0:
            winner = "p2 wins"
            end_screen = True

        elif p2_hp == 0:
            winner = "p1 wins"
            end_screen = True
        
            
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
        
        
        
        for w in level_walls:
            pygame.draw.rect(screen, w[4], [w[0], w[1], w[2], w[3]])

        
        ''' player '''
        
        
        pygame.draw.rect(screen, V, p1_hitbox)

        
        


            
        ''' player2 '''
        
        
        pygame.draw.rect(screen, G, p2_hitbox)
        



        pygame.draw.rect(screen, l, p1_weapon_hitbox)
        
        pygame.draw.rect(screen, l, p2_weapon_hitbox)
        

        
        
        
            
        
            
        
        
        
                
                    

            
##        if timer == 0:
##            create_level(level_layout_list, level_on)
                
##        if beat%(int(quarter)) == 0:
##            timer -= 1
        
    
    if end_screen:
        print(winner)
        screen.fill(B)
         
        
    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

   
