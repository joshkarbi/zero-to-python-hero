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

X_VELOCITY = 0.05
Y_VELOCITY = 0.05

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, CIRCLE_COLOR, (CIRCLE_X, CIRCLE_Y), CIRCLE_RADIUS)
    pygame.display.flip()

    '''
    BOUNCE TOP/BOTTOM
    '''
    if CIRCLE_Y + CIRCLE_RADIUS >= WINDOW_HEIGHT or \
        CIRCLE_Y - CIRCLE_RADIUS <= 0:
        Y_VELOCITY *= -1

    if CIRCLE_X + CIRCLE_RADIUS >= WINDOW_WIDTH or \
        CIRCLE_X - CIRCLE_RADIUS <= 0:
        X_VELOCITY *= -1

    '''
    Update the ball position !
    '''
    CIRCLE_X += X_VELOCITY
    CIRCLE_Y += Y_VELOCITY    
    
pygame.quit()