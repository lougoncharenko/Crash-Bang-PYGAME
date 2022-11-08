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


#Game Object class that draws a rectangle
class GameObject(pygame.sprite.Sprite):
    """
    This class extends pygame.sprite.Sprite.
    Defines four parameters: x, y, width, and height.
    It stores three attributes: self.surf, self.x, and self.y.
    """
    def __init__(self, x_position, y_position, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image) # ADD!
        self.x_position = x_position
        self.y_position = y_position

    def render (self, screen):
        """
        This method is responsible for drawing the GameObject's surface to the screen.
        """
        screen.blit(self.surf, (self.x_position, self.y_position))

# game loop
running = True
while running:
    #look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Make an instance of GameObject
    apple = GameObject(200, 300, 'images/apple.png')
    strawberry= GameObject(400, 70, 'images/strawberry.png')
    mushroom = GameObject(300, 150,'images/mushroom.jpeg')
    screen.fill (WHITE)
    apple.render(screen)
    strawberry.render(screen)
    mushroom.render(screen)
    
    
    #update display
    pygame.display.flip()


