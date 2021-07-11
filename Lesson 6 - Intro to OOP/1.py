'''
Multiple bouncing balls using pygame.
'''

import pygame
import time
pygame.init()


class BouncingBall:
    def __init__(self, x, y, screen, color=(0,0,255), radius=50, \
        y_vel=0.02, accel=0.0005, window_height=500, window_width=700):
        '''
        Call this to create me!
        '''
        self.__x = x
        self.__y = y
        self.__screen = screen
        self.__color = color
        self.__radius = radius
        self.__y_vel = y_vel
        self.__accel = accel
        self.__window_width = window_width
        self.__window_height = window_height

    def draw(self):
        '''
        Call this to put me on the screen!
        '''
        pygame.draw.circle(self.__screen,
             self.__color, 
             (self.__x, self.__y),
             self.__radius
        )

        self.__move()

    def __move(self):
        '''
        This defines how my position changes over time.
        '''

        # BOUNCE BOTTOM
        if self.__y + self.__radius >= self.__window_height:
            self.__y_vel *= -1

        # Update the ball position !
        self.__y += self.__y_vel    

        # ACCELLERATION
        self.__y_vel += self.__accel


# Set up the drawing window
WINDOW_WIDTH, WINDOW_HEIGHT = 700, 500
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# Create as many balls as we want!!!!!
balls = [
            BouncingBall(x=200, y=250, screen=screen),
            BouncingBall(x=400, y=200, screen=screen, color=(250,100,0), radius=30),
            BouncingBall(x=600, y=300, screen=screen, color=(10,160,30), radius=70, accel=0.0008),
            BouncingBall(x=100, y=20, screen=screen, color=(153,50,204), radius=10, accel=0.0003),
            BouncingBall(x=500, y=70, screen=screen, color=(75,0,130), radius=20, accel=0.001)
        ]

# Just to flex (0 = normal speed, 1+ slow down)
SLOW_DOWN_FACTOR = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the next frame
    screen.fill((255, 255, 255))
    for ball in balls:
        ball.draw()
    time.sleep(SLOW_DOWN_FACTOR * 0.0001)
    pygame.display.flip()
    
pygame.quit()