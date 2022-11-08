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
    def __init__(self, x, y, width, height, color):
        super(GameObject, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill ((color))
        self.rect = self.surf.get_rect()
        self.x = x
        self.y = y

    def render (self, screen):
        """
        This method is responsible for drawing the GameObject's surface to the screen.
        """
        screen.blit(self.surf, (self.x, self.y))

# game loop
running = True
while running:
    #look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Make an instance of GameObject
    box = GameObject(120, 300, 50, 50, FUSCHIA)
    box2 = GameObject(90, 40, 50, 50, BLUE )
    screen.fill (WHITE)
    box.render(screen)
    box2.render(screen)
    #update display
    pygame.display.flip()


