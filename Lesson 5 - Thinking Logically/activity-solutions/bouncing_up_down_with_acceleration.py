'''
Our goal: make the circle bounce up and down off the floor.
When we've finished: we want the ball to bounce diagonally off the walls.
'''

import pygame
import random
pygame.init()

# Set up the drawing window
WINDOW_WIDTH, WINDOW_HEIGHT = 700, 500
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

running = True

CIRCLE_COLOR = (0, 0, 255)
CIRCLE_RADIUS = 50
CIRCLE_X = 200
CIRCLE_Y = 250

Y_VELOCITY = 0.02
ACCELERATION = 0.0005

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, CIRCLE_COLOR, (CIRCLE_X, CIRCLE_Y), CIRCLE_RADIUS)
    pygame.display.flip()

    ''' BOUNCE BOTTOM '''
    if CIRCLE_Y + CIRCLE_RADIUS >= WINDOW_HEIGHT:
        Y_VELOCITY *= -1

    ''' Update the ball position !  '''
    CIRCLE_Y += Y_VELOCITY    

    ''' ACCELLERATION '''
    Y_VELOCITY += ACCELERATION

    
pygame.quit()