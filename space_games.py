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



# Game classes
class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 32
        self.h = 32
        self.speed = 3
        self.shield = 10

    def move_left(self):
        self.x -= self.speed
        
    def move_right(self):
        self.x += self.speed

    def cast_fire(self):
        x = self.x + (self.w / 2) - 2
        y = self.y
        spell = Fire(x, y)
        spells.append(spell)
        print("Pew!")

    def cast_thunder(self):
        x = self.x + (self.w / 2) - 2
        y = self.y
        spell = Thunder(x, y)
        spells.append(spell)
        print("Pew!")

    def update(self):
        pass

    def draw(self):
        rect = [self.x, self.y, self.w, self.h]
        pygame.draw.rect(screen, RED, rect)
    
class Fire:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 4
        self.h = 8
        self.speed = 3

    def update(self):
        self.y -= self.speed


    def draw(self):
        rect = [self.x, self.y, self.w, self.h]
        pygame.draw.rect(screen, RED, rect)

class Thunder:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 4
        self.h = 8
        self.speed = 6

    def update(self):
        self.y -= self.speed

    def draw(self):
        rect = [self.x, self.y, self.w, self.h]
        pygame.draw.rect(screen, YELLOW, rect)


    
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
spells = []


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
        
    
    for s in spells:
        Fire.update(s)

    for s in spells:
        Thunder.update(s)

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    player.draw()

    for s in spells:
        Fire.draw(s)

    for s in spells:
        Thunder.draw(s)


    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
