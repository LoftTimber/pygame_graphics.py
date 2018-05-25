# Imports
import pygame

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Space War"
screen = pygame.display.set_mode(SIZE)
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
ship_img = pygame.image.load('assets/images/player_facing_left.png')
fire_img = pygame.image.load('assets/images/player_jump_left.png')
thunder_img = pygame.image.load('assets/images/player_jump_right.png')


# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 3
        self.shield = 10

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed

    

    

    def cast_fire(self):
        spell = Fire(fire_img)

        spell.rect.centerx = self.rect.centerx
        spell.rect.centery = self.rect.top
        
        spells1.add(spell)
        

    def cast_thunder(self):
        spell = Thunder(thunder_img)

        spell.rect.centerx = self.rect.centerx
        spell.rect.centery = self.rect.top
        
        spells2.add(spell)

    def update(self):
        pass

    
    
class Fire(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 6

    def update(self):
        self.rect.y -= self.speed


    

class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 12

    def update(self):
        self.rect.y -= self.speed


    
class Mob:

    def __init__(self):
        pass

    def update(self):
        pass


class Bomb:
    
    def __init__(self):
        pass

    def update(self):
        pass
    
    
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
player = Ship(384, 536)
spells1 = []
spells2 = []


# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pass

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        player.move_left()
    elif pressed[pygame.K_RIGHT]:
        player.move_right()
        
    
    # Game logic (Check for collisions, update points, etc.)
    beat += 1
    if beat%(int(eighth)) == 0:
        player.cast_fire()
    if beat%(int(quarter)) == 0:
        player.cast_thunder()
        
    
    
    spells1.update()

    spells2.update()
        

    

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    spells1.draw(screen)
    spells2.draw(screen)
    player.draw(screen)


    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
