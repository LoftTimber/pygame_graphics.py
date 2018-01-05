# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
height = 600
leight = 800
SIZE = (leight, height)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
r = (255, 0, 0) #RED
g = (0, 255, 0) #GREEN
f = (34, 139, 34) #FORESTGREEN
b = (0, 0, 255) #BLUE
w = (255, 255, 255) #WHITE
B = (0, 0, 0) #BLACK
o = (255, 125, 0) #ORANGE
y = (255, 255, 0) #YELLOW
s = (139, 69, 19) #SADDLEBROWN
    

# Game loop
done = False



while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(w)
    #44
    #29
    #69
    #135
    

    
    leight_in_pixels = 50
    size_of_pixel = leight/leight_in_pixels
    
    grid_line = 0
    line = 0

    
    line1 = [w,w,w,w,w,w,w,w,y,y]
    line2 = [w,w,w,w,w,y,y,w,y,y,w,y,y]
    line3 = [w,w,w,w,w,y,y,y,y,y,y,y,y]
    line4 = [w,w,w,y,y,y,y,s,s,s,s,y,y,y]
    line5 = [w,w,w,y,y,y,s,s,s,s,s,s,y,y]
    line6 = [w,w,w,w,y,s,s,s,s,s,s,s,s,y]
    line7 = [w,w,y,y,y,s,s,s,s,s,s,s,s,y,y,y]
    line8 = [w,w,y,y,y,s,s,s,s,s,s,s,s,y,y,y]
    line9 = [w,w,w,w,y,s,s,s,s,s,s,s,s,y]
    line10= [w,w,y,y,y,y,s,s,s,s,s,s,y,y,y,y]
    line11= [g,g,g,g,y,y,y,s,s,s,s,y,y,y,y,y]
    line12= [g,g,f,f,g,y,y,y,y,y,y,y,y]
    line13= [g,g,g,g,f,y,y,w,y,y,w,y,y]
    line14= [w,g,g,g,g,f,g,g,y,y]
    line15= [w,g,g,g,g,g,f,g,f,w,w,g,g,g,w,w,g]
    line16= [w,w,g,g,g,g,f,g,f,w,g,g,g,g,g,g,g]
    line17= [w,w,w,g,g,g,f,g,f,g,g,g,g,g,g,g,g]
    line18= [w,w,w,w,w,g,g,f,f,g,g,f,f,f,g,g,g]
    line19= []
        
    
    line_colors = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19]

    
    for i in range(0, len(line_colors)):
        position = 0
        current_line = line_colors[line]
        for i in range(0, len(current_line)):
            color_picked = current_line[position]
            pygame.draw.rect(screen, color_picked, [position*size_of_pixel, line*size_of_pixel, size_of_pixel, size_of_pixel])
            
            position += 1

        line += 1





    
    ''' makes grid '''
    
    while grid_line <= (leight_in_pixels-1)*size_of_pixel:
        pygame.draw.line(screen, B, [grid_line, 0], [grid_line, height])
        grid_line += size_of_pixel
    grid_line = 0
    while grid_line <= (leight_in_pixels-1)*size_of_pixel:
        pygame.draw.line(screen, B, [0, grid_line], [leight, grid_line])
        grid_line += size_of_pixel
   

    
    
    

    

    
    
    
    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
