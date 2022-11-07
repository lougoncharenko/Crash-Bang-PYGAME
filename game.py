# Import and initialize pygame
import pygame 
pygame.init()

#configure the screen
screen = pygame.display.set_mode([500,500])

#Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
FUSCHIA = (255, 0, 255)
GRAY = (100, 100, 100)
ORANGE = (250, 141, 7)
LIGHTGREEN = (25, 184, 22)

# game loop
running = True
while running:
    #look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear the screen
    screen.fill((WHITE))
    #draw a circle
    position1 = (250, 250) # x, y position
    pygame.draw.circle(screen, YELLOW, position1, 50) #75 is the radius
    position2 =  (50,50)
    pygame.draw.circle(screen, RED, position2, 50) #75 is the radius
    position3 =  (450,50)
    pygame.draw.circle(screen, ORANGE, position3, 50) #75 is the radius
    position4 =  (50, 450)
    pygame.draw.circle(screen, LIGHTGREEN, position4, 50) #75 is the radius
    position5 =  (450, 450)
    pygame.draw.circle(screen, CYAN, position5, 50) #75 is the radius
    #update display
    pygame.display.flip()