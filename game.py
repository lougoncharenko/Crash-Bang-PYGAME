# Import and initialize pygame
import pygame
pygame.init()
from random import randint
clock = pygame.time.Clock()

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


class GameObject(pygame.sprite.Sprite):
    """
    This class extends pygame.sprite.Sprite.
    Defines 3 parameters: x, y, and image
    It stores three attributes: self.surf, self.x, and self.y.
    """
    def __init__(self, x_position, y_position, image):
        super(GameObject, self).__init__()
        load_image= pygame.image.load(image) 
        self.surf = pygame.transform.scale(load_image, (50,50)) #controls images height
        self.dimension = pygame.Surface((50, 50))
        self.x_position = x_position
        self.y_position = y_position
        self.reset()
    
    def move(self):
        self.x_position += 1
        self.y_position += 1
        if self.y_position > 500: 
            self.reset()

    def reset(self): 
        self.x_position = randint(50, 400)
        self.y_position = -64



    def render (self, screen):
        """
        This method is responsible for drawing the GameObject's surface to the screen.
        """
        screen.blit(self.surf, (self.x_position, self.y_position))

apple = GameObject(0, 250, 'images/apple.png')
mario = GameObject(50, 300, 'images/mario.jpeg')
mushroom = GameObject(300, 500, 'images/mushroom.jpeg')

#game loop
GAME_RUNNING = True
while GAME_RUNNING:
    #look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUNNING = False
    screen.fill (WHITE)
    mushroom.render(screen)
    apple.move()
    apple.render(screen)
    mario.move()
    mario.render(screen)
    pygame.display.flip()
    clock.tick(60)