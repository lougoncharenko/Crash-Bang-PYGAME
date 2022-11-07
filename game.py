# Import and initialize pygame
import pygame 
pygame.init()

#configure the screen
screen = pygame.display.set_mode([500,500])


RED = (255, 0, 0)
GREEN = (0, 255, 0)

# game loop
running = True
while running:
    #look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear the screen
    screen.fill((255, 255, 255))
    #draw a circle
    color = (255, 0, 255) #rgb values
    position = (250, 250) # x, y position
    pygame.draw.circle(screen, color, position, 75) #75 is the radius
    #update display
    pygame.display.flip()