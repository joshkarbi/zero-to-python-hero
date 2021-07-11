'''
Activity: make the ball bounce off the window borders.
'''

import pygame
pygame.init()

# Set up the drawing window
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

running = True

CIRCLE_COLOR = (0, 0, 255)
CIRCLE_RADIUS = 50
CIRCLE_X = 250
CIRCLE_Y = 250

X_VELOCITY = 0.02
Y_VELOCITY = -0.02

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, CIRCLE_COLOR, (CIRCLE_X, CIRCLE_Y), CIRCLE_RADIUS)
    pygame.display.flip()

    '''
    Update the ball position !
    '''
    CIRCLE_X += X_VELOCITY
    CIRCLE_Y += Y_VELOCITY

pygame.quit()