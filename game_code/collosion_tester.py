import pygame


# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Collision Tester"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Shape definitions
circle = [375, 275, 50]
rectangle = [350, 275, 100, 50]


def point_circle(point, circle):
    a = point[0] - circle[0]
    b = point[1] - circle[1]
    r = circle[2]

    return a**2 + b**2 <= r**2 
    
def point_rect(point, rect):
    x = point[0]
    y = point[1]

    left = rect[0]
    right = rect[0] + rect[2]
    top = rect[1]
    bottom = rect[1] + rect[3]
    
    return left <= x <= right and top <= y <= bottom

def circle_circle(circle1, circle2):
    a = circle1[0] - circle2[0]
    b = circle1[1] - circle2[1]
    radius_sum = circle1[2] + circle2[2]

    return a**2 + b**2 <= radius_sum**2

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


# Select test case
'''
1 = point-circle
2 = point-rectangle
3 = circle-circle
4 = rectangle-rectangle
'''
case = 1

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic             
    mouse_pos = pygame.mouse.get_pos()
    circle2 = [mouse_pos[0], mouse_pos[1], 50]
    rectangle2 = [mouse_pos[0], mouse_pos[1], 100, 50]

    if case == 1:
        if point_circle(mouse_pos, circle):
            color = RED
        else:
            color = WHITE
    elif case == 2:
        if point_rect(mouse_pos, rectangle):
            color = RED
        else:
            color = WHITE
    elif case == 3:
        if circle_circle(circle, circle2):
            color = RED
        else:
            color = WHITE
    elif case == 4:
        if rect_rect(rectangle, rectangle2):
            color = RED
        else:
            color = WHITE

    # Drawing code
    screen.fill(BLACK)

    if case == 1:
        pygame.draw.circle(screen, color, [circle[0], circle[1]], circle[2])
    elif case == 2:
        pygame.draw.rect(screen, color, [rectangle[0], rectangle[1], rectangle[2], rectangle[3]])
    elif case == 3:
        pygame.draw.circle(screen, color, [circle[0], circle[1]], circle[2])
        pygame.draw.circle(screen, WHITE, [circle2[0], circle2[1]], circle2[2])
    elif case == 4:
        pygame.draw.rect(screen, color, [rectangle[0], rectangle[1], rectangle[2], rectangle[3]])
        pygame.draw.rect(screen, WHITE, [rectangle2[0], rectangle2[1], rectangle2[2], rectangle2[3]])

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
