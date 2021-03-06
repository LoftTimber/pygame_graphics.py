# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
height = 600
lenght = 800
SIZE = (lenght, height)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
r = (255, 0, 0)     #RED
g = (0, 255, 0)     #GREEN
f = (34, 139, 34)   #FORESTGREEN
b = (0, 0, 255)     #BLUE
w = (255, 255, 255) #WHITE
B = (0, 0, 0)       #BLACK
O = (255, 165, 0)   #ORANGE
y = (255, 255, 0)   #YELLOW
s = (139, 69, 19)   #SADDLEBROWN
o = (255,80,0)     #DARKERORANGE

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
    def sunflower():
        line1 = [0,0,0,0,0,0,0,0,y,y]
        line2 = [0,0,0,0,0,y,y,0,y,y,0,y,y]
        line3 = [0,0,0,0,0,y,y,y,y,y,y,y,y]
        line4 = [0,0,0,y,y,y,y,s,s,s,s,y,y,y]
        line5 = [0,0,0,y,y,y,s,s,s,s,s,s,y,y]
        line6 = [0,0,0,0,y,s,s,s,s,s,s,s,s,y]
        line7 = [0,0,y,y,y,s,s,s,s,s,s,s,s,y,y,y]
        line8 = [0,0,y,y,y,s,s,s,s,s,s,s,s,y,y,y]
        line9 = [0,0,0,0,y,s,s,s,s,s,s,s,s,y]
        line10= [0,0,y,y,y,y,s,s,s,s,s,s,y,y,y,y]
        line11= [g,g,g,g,y,y,y,s,s,s,s,y,y,y,y,y]
        line12= [g,g,f,f,g,y,y,y,y,y,y,y,y]
        line13= [g,g,g,g,f,y,y,w,y,y,0,y,y]
        line14= [0,g,g,g,g,f,g,g,y,y]
        line15= [0,g,g,g,g,g,f,g,f,0,0,g,g,g,0,0,g]
        line16= [0,0,g,g,g,g,f,g,f,0,g,g,g,g,g,g,g]
        line17= [0,0,0,g,g,g,f,g,f,g,g,g,g,g,g,g,g]
        line18= [0,0,0,0,0,g,g,f,f,g,g,f,f,f,g,g,g]
        line19= [0,0,0,0,0,0,f,f,f,g,f,g,g,g,g,g,g]
        line20= [0,0,0,0,0,0,0,f,f,f,g,g,g,g,g]    
        line21= [0,0,0,0,0,0,0,f,f,0,0,g,g,g]
        
        line_colors = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21]


        
    def fire_flower():
        line1 = [0,0,0,0,0,0,0,B,B]
        line2 = [0,0,B,0,0,0,B,O,O,B,0,0,0,B]
        line3 = [0,B,O,B,0,B,O,O,O,O,B,0,B,o,B]
        line4 = [0,B,O,O,B,O,O,O,O,O,O,B,O,O,B]
        line5 = [B,O,O,O,O,O,O,O,O,O,O,O,O,O,o,B]
        line6 = [B,O,O,O,B,B,O,O,O,B,B,O,O,O,o,B]
        line7 = [B,O,O,B,O,O,B,O,B,O,O,B,O,O,o,B]
        line8 = [B,O,O,O,O,O,O,O,O,O,O,O,O,o,o,B]
        line9 = [0,B,O,O,O,O,O,O,O,O,O,O,O,o,B]
        line10= [0,0,B,o,O,O,O,O,O,O,o,o,o,B]
        line11= [0,0,0,B,B,o,o,o,o,o,o,B,B]
        line12= [0,0,0,0,0,B,B,B,B,B,B]
        line13= [0,0,B,B,B,0,B,g,f,B,B,B,B]
        line14= [0,B,g,g,f,B,B,g,f,B,g,g,f,B]
        line15= [B,g,g,g,g,f,B,g,B,g,g,g,g,f,B]
        line16= [B,f,f,f,f,f,B,B,B,f,f,f,f,f,B]
        line17= [0,B,B,B,B,B,0,0,0,B,B,B,B,B]


        
    #Draws flower
    lenght_in_pixels = 200
    size_of_pixel = lenght/lenght_in_pixels
    grid_line = 0
    flower_num = 0
    
    for i in range(100):
        line = 0
        sunflower()
    
    
    
        
        
        line_colors = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17]
        
        for i in range(len(line_colors)):
            position = 0
            current_line = line_colors[line]
            for i in range(len(current_line)):
                color_picked = current_line[position]
                if color_picked == 0:
                    pass
                else:
                    pygame.draw.rect(screen, color_picked, [(flower_num*size_of_pixel)+position*size_of_pixel, (50*size_of_pixel)+line*size_of_pixel, size_of_pixel, size_of_pixel])
                
                position += 1

            line += 1


        flower_num += 10


    
    ''' makes grid '''
    '''
    while grid_line <= (lenght_in_pixels-1)*size_of_pixel:
        pygame.draw.line(screen, B, [grid_line, 0], [grid_line, height])
        grid_line += size_of_pixel
    grid_line = 0
    while grid_line <= (lenght_in_pixels-1)*size_of_pixel:
        pygame.draw.line(screen, B, [0, grid_line], [lenght, grid_line])
        grid_line += size_of_pixel
   
'''
    
    
    

    

    
    
    
    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
