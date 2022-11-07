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
    color = (255, 0, 255) #rgb values
    position = (250, 250) # x, y position
    pygame.draw.circle(screen, color, position, 75) #75 is the radius
    #update display
    pygame.display.flip()