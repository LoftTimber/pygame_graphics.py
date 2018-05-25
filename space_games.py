# Imports
import pygame

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Space War"
screen = pygame.display.set_mode(SIZE)      ########################### work on stair case to funnel trap evode
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Images
pix1_img = pygame.image.load('space_game_stuff/images/pixel.png')
ship_img = pygame.image.load('space_game_stuff/images/player_facing_left.png')
fire_img = pygame.image.load('space_game_stuff/images/player_jump_left.png')
thunder_img = pygame.image.load('space_game_stuff/images/player_jump_right.png')




# Game classes
class Pixel(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.filled = False

    def update(self, spells1, mobs):

        hit_list = pygame.sprite.spritecollide(self, spells1, False)
        
        
        self.filled = False
        for hit in hit_list:
            self.filled = True

            
##        go_left = False
##        go_right = False
##
##        num = 5
##        for i in range(9):
##            if pixel_items[num].filled == True:
##                go_right = True
##
##            num += 12
##            
##        num = 6
##        for i in range(9):
##            if pixel_items[num].filled == True:
##                if go_right == True:
##                    go_left = go_right
##                go_right = False
##
##            num += 12
##
##            
##        num = 4
##        for i in range(9):
##            if pixel_items[num].filled == True:
##                if go_left == True:
##                    go_right = go_right
##                go_left = False
##
##            num += 12
##            
##
##        if go_left == True:
##            self.rect.x -= 15
##
##        elif go_right == True:
##            self.rect.x += 15

        

            
        
            

    
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 10
        self.shield = 1
        self.shot_range = 500

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed

    

    

    def cast_fire(self):
##        spell = Fire(fire_img)
##
##        spell.rect.centerx = self.rect.centerx
##        spell.rect.centery = self.rect.top
##        
##        spells1.add(spell)


        
        
        spell = Fire(fire_img)

        spell.rect.centerx = self.rect.centerx+100
        spell.rect.centery = self.rect.top
        
        spells1.add(spell)

        spell = Fire(fire_img)

        spell.rect.centerx = self.rect.centerx-100
        spell.rect.centery = self.rect.top
        
        spells1.add(spell)

        self.shot_range -= 30
        

    def cast_thunder(self):
        spell = Thunder(thunder_img)

        spell.rect.centerx = self.rect.centerx
        spell.rect.centery = self.rect.top
        
        spells2.add(spell)

    def update(self, bombs):
        hit_list = pygame.sprite.spritecollide(self, bombs, True)

        for hit in hit_list:
            self.shield -= 1

            
        if self.shield <= 0:
            self.kill()
            

        

    
    
class Fire(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 3

    def move_left(self, ship):
        self.rect.x -= ship.speed
        
    def move_right(self, ship):
        self.rect.x += ship.speed

    def update(self, mob1):
        self.rect.y -= self.speed

##        if mob1.rect.centerx > self.rect.centerx:
##            self.rect.x += self.speed
##
##        if mob1.rect.centerx < self.rect.centerx:
##            self.rect.x -= self.speed

        if self.rect.bottom <= 0:
            self.kill()


    

class Thunder(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 12

    def update(self):
        self.rect.y -= self.speed


    
class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 15
        self.shield = 1
        
    def move_left(self, ship):
        self.rect.x -= ship.speed
        
    def move_right(self, ship):
        self.rect.x += ship.speed

    def move(self, spells1, spells2):

        spell_to_left = False
        spell_to_right = False
        spell_to_left_far = False
        spell_to_right_far = False
        spell_to_left_very_far = False
        spell_to_right_very_far = False
        can_not_go_left = False
        can_not_go_right = False
        will_not_go_left = False
        will_not_go_right = False
        would_not_go_left = False
        would_not_go_right = False
        would_not_go_left_far = False
        would_not_go_right_far = False
        would_not_go_left_very_far = False
        would_not_go_right_very_far = False
        spell_to_far_left = False
        spell_to_far_right = False
        for spell in spells1:
            if ((spell.rect.right >= self.rect.left) and spell.rect.centerx <= self.rect.centerx) \
                and (spell.rect.top <= self.rect.bottom+(7*spell.speed) and spell.rect.bottom >= self.rect.top):
                spell_to_left = True

            if (spell.rect.centerx > self.rect.centerx and spell.rect.left <= self.rect.right) \
                and (spell.rect.top <= self.rect.bottom+(7*spell.speed) and spell.rect.bottom >= self.rect.top):
                spell_to_right = True

            if ((spell.rect.right >= self.rect.left) and spell.rect.centerx <= self.rect.centerx) \
                and (spell.rect.top <= self.rect.bottom+(28*spell.speed) and spell.rect.bottom >= self.rect.top):
                spell_to_left_far = True

            if (spell.rect.centerx > self.rect.centerx and spell.rect.left <= self.rect.right) \
                and (spell.rect.top <= self.rect.bottom+(28*spell.speed) and spell.rect.bottom >= self.rect.top):
                spell_to_right_far = True

            if ((spell.rect.right >= self.rect.left) and spell.rect.centerx <= self.rect.centerx) \
                and (spell.rect.top <= self.rect.bottom+(100*spell.speed) and spell.rect.bottom >= self.rect.top+(14*spell.speed)):
                spell_to_left_very_far = True

            if (spell.rect.centerx > self.rect.centerx and spell.rect.left <= self.rect.right) \
                and (spell.rect.top <= self.rect.bottom+(100*spell.speed) and spell.rect.bottom >= self.rect.top+(14*spell.speed)):
                spell_to_right_very_far = True

            if (spell.rect.centerx >= (self.rect.centerx)-63-self.speed and spell.rect.centerx < (self.rect.centerx)) \
                and (spell.rect.top <= self.rect.bottom+(7*spell.speed) and spell.rect.bottom >= self.rect.top):
                can_not_go_left = True

            if (spell.rect.centerx > (self.rect.centerx) and spell.rect.centerx < (self.rect.centerx)+63+self.speed) \
                and (spell.rect.top <= self.rect.bottom+(7*spell.speed) and spell.rect.bottom >= self.rect.top):
                can_not_go_right = True

            if (spell.rect.centerx >= (self.rect.centerx)-500 and spell.rect.centerx < (self.rect.centerx)-63) \
                and (spell.rect.top <= self.rect.bottom+(14*spell.speed) and spell.rect.bottom >= self.rect.top):
                will_not_go_left = True

            if (spell.rect.centerx > (self.rect.centerx)+63 and spell.rect.centerx < (self.rect.centerx)+500) \
                and (spell.rect.top <= self.rect.bottom+(14*spell.speed) and spell.rect.bottom >= self.rect.top):
                will_not_go_right = True

            if (spell.rect.centerx >= (self.rect.centerx)-200 and spell.rect.centerx < (self.rect.centerx)) \
                and (spell.rect.top <= self.rect.bottom+(7*spell.speed) and spell.rect.bottom >= self.rect.top):
                would_not_go_left = True

            if (spell.rect.centerx > (self.rect.centerx) and spell.rect.centerx < (self.rect.centerx)+200) \
                and (spell.rect.top <= self.rect.bottom+(7*spell.speed) and spell.rect.bottom >= self.rect.top):
                would_not_go_right = True

            if (spell.rect.centerx >= (self.rect.centerx)-200 and spell.rect.centerx < (self.rect.centerx)) \
                and (spell.rect.top <= self.rect.bottom+(28*spell.speed) and spell.rect.bottom >= self.rect.top+(14*spell.speed)):
                would_not_go_left_far = True  

            if (spell.rect.centerx > (self.rect.centerx) and spell.rect.centerx < (self.rect.centerx)+200) \
                and (spell.rect.top <= self.rect.bottom+(28*spell.speed) and spell.rect.bottom >= self.rect.top+(14*spell.speed)):
                would_not_go_right_far = True

            if (spell.rect.centerx >= (self.rect.centerx)-200 and spell.rect.centerx < (self.rect.centerx)) \
                and (spell.rect.top <= self.rect.bottom+(64*spell.speed) and spell.rect.bottom >= self.rect.top+(35*spell.speed)):
                would_not_go_left_very_far = True
               

            if (spell.rect.centerx > (self.rect.centerx) and spell.rect.centerx < (self.rect.centerx)+200) \
                and (spell.rect.top <= self.rect.bottom+(64*spell.speed) and spell.rect.bottom >= self.rect.top+(35*spell.speed)):
                would_not_go_right_very_far = True
               

            if ((spell.rect.right >= self.rect.left-200) and spell.rect.centerx <= self.rect.centerx) \
                and (spell.rect.top <= self.rect.bottom+(14*spell.speed) and spell.rect.bottom >= self.rect.top):
                spell_to_far_left = True

            if (spell.rect.centerx > self.rect.centerx and spell.rect.left <= self.rect.right+200) \
                and (spell.rect.top <= self.rect.bottom+(14*spell.speed) and spell.rect.bottom >= self.rect.top):
               spell_to_far_right = True

##        if can_not_go_right == True and can_not_go_left == True:
##            if spell_to_close_left == True:
##                self.rect.x += self.speed
##            if spell_to_close_right == True:
##                self.rect.x -= self.speed
        

        if (spell_to_left == True or spell_to_right == True) and can_not_go_right == True and can_not_go_left == False:
            self.rect.x -= self.speed

        elif (spell_to_left == True or spell_to_right == True) and can_not_go_left == True and can_not_go_right == False:
            self.rect.x += self.speed

        elif (spell_to_left == True or spell_to_right == True) and can_not_go_left == True and can_not_go_right == True:
            pass

        elif (spell_to_left_far == True or spell_to_right_far == True) and spell_to_far_right == True and will_not_go_right == True:
            self.rect.x -= self.speed
            
        elif (spell_to_left_far == True or spell_to_right_far == True) and spell_to_far_left == True and will_not_go_left == True:
            self.rect.x += self.speed

        elif (spell_to_left_far == True or spell_to_right_far == True) and will_not_go_right == True and will_not_go_left == False and can_not_go_left == False:
            self.rect.x -= self.speed

        elif (spell_to_left_far == True or spell_to_right_far == True) and will_not_go_left == True and will_not_go_right == False and can_not_go_right == False:
            self.rect.x += self.speed

        elif (spell_to_left_far == False or spell_to_right_far == False) and would_not_go_right == False and would_not_go_left == False\
             and would_not_go_right_far == True and would_not_go_left_far == True and would_not_go_right_very_far == True and would_not_go_left_very_far == True \
             and will_not_go_left == False:
            self.rect.x -= self.speed

        elif (spell_to_left_far == False or spell_to_right_far == False) and would_not_go_right == False and would_not_go_left == False\
             and would_not_go_right_far == True and would_not_go_left_far == True and would_not_go_right_very_far == True and would_not_go_left_very_far == True \
             and will_not_go_right == False:
            self.rect.x += self.speed

        elif (spell_to_left_very_far == True or spell_to_right_very_far == True) and would_not_go_left == True and would_not_go_right == False\
             and will_not_go_right == False and can_not_go_right == False:
            self.rect.x += self.speed

        elif (spell_to_left_very_far == True or spell_to_right_very_far == True) and would_not_go_right == True and would_not_go_left == True\
             and will_not_go_right == False and can_not_go_right == False:
            self.rect.x += self.speed

        elif (spell_to_left_very_far == True or spell_to_right_very_far == True) and would_not_go_right == True and would_not_go_left == True\
             and will_not_go_left == False and can_not_go_left == False:
            self.rect.x -= self.speed

        
 
        elif spell_to_left == True:
            self.rect.x += self.speed
        
        elif spell_to_right == True:
            self.rect.x -= self.speed
            


               
            
            

            

        

    def drop_bomb(self):
        bomb = Bomb(fire_img)

        bomb.rect.centerx = self.rect.centerx
        bomb.rect.y = self.rect.bottom
        
        bombs.add(bomb)

    def update(self, spells1, spells2):
        hit_list = pygame.sprite.spritecollide(self, spells1, True)
        
        

        for hit in hit_list:
            self.shield -= 1

        
        hit_list = pygame.sprite.spritecollide(self, spells2, True)

        for hit in hit_list:
            self.shield -= 1

        if self.shield <= 0:
            self.kill()
            
        


class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 6

    def move_left(self, ship):
        self.rect.x -= ship.speed
        
    def move_right(self, ship):
        self.rect.x += ship.speed

    def update(self):
        self.rect.y += self.speed
    
    
class Fleet:

    def __init__(self):
        pass

    def update(self):
        pass

    
metronome = 60
beat = 0

sixteenth = int((refresh_rate**2/metronome)/4)
eighth = sixteenth*2
quarter = sixteenth*4
# Make game objects
pix_num = 0
pix_line = 0
pix_type = pix1_img
pixel_items = []
for i in range(9):
    pix_num = 0
    for i in range(12):
        pixel_items.append(Pixel(pix_num, pix_line, pix_type))
        pix_num += 64
    pix_line += 64

ship = Ship(384, 536, ship_img)
mob1 = Mob(384, 64, ship_img)
##mob2 = Mob(500, 64, ship_img)




# Make sprite groups
pixels = pygame.sprite.Group()
pixels.add(pixel_items)

player = pygame.sprite.Group()
player.add(ship)

spells1 = pygame.sprite.Group()
spells2 = pygame.sprite.Group()


mobs = pygame.sprite.Group()
mobs.add(mob1)



bombs = pygame.sprite.Group()
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                ship.cast_fire()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        mob1.move_right(ship)
        for s in spells1:
            s.move_right(ship)
        for b in bombs:
            b.move_right(ship)
    elif pressed[pygame.K_RIGHT]:
        mob1.move_left(ship)
        for s in spells1:
            s.move_left(ship)
        for b in bombs:
            b.move_left(ship)

##    if pressed[pygame.K_LEFT]:
##        ship.move_left()
##    elif pressed[pygame.K_RIGHT]:
##        ship.move_right()
        
    
    # Game logic (Check for collisions, update points, etc.)
    beat += 1
##    if beat%(int(sixteenth)) == 0:
##        ship.cast_fire()
##    if beat%(int(sixteenth)) == 0:
##        ship.cast_thunder()

##    if beat%(int(quarter*4)) == 0:
##        mobs.add(Mob(500, 64, ship_img))

    pixels.update(spells1, mobs)
    player.update(bombs)
    spells1.update(mob1)

    spells2.update()
    mobs.update(spells1, spells2)
    bombs.update()

    for m in mobs:
        m.move(spells1, spells2)
        if beat%(int(quarter)) == 0:
            m.drop_bomb()

    

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(GREEN)
##    pixels.draw(screen)
    spells1.draw(screen)
    spells2.draw(screen)
    player.draw(screen)
    mobs.draw(screen)
    bombs.draw(screen)


    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
