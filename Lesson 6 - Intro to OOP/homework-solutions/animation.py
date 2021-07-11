'''
A class Animation that runs the full animation.
'''

import pygame, random, time

class Ball():
    def __init__(self, x, y, screen, color=(0,0,255), radius=50, \
        y_vel=0.02, x_vel=0, accel=0.0005, window_height=500, \
        window_width=700, is_tracking=False):
        '''
        Call this to create me!
        '''
        self.__x = x
        self.__y = y
        self.__screen = screen
        self.__color = color
        self.__radius = radius
        self.__x_vel = x_vel
        self.__y_vel = y_vel
        self.__accel = accel
        self.__window_width = window_width
        self.__window_height = window_height
        self.__is_tracking = is_tracking
        self.__path_points = []

    def draw(self):
        '''
        Call this to put me on the screen!
        '''
        if self.__is_tracking:
            self.__path_points.append(
                (self.__x, self.__y)
            )
            if len(self.__path_points) == 700:
                self.__path_points = self.__path_points[1:]
            if len(self.__path_points) >= 2:
                pygame.draw.lines(
                    self.__screen, (0,0,0), False, self.__path_points
                )
                
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
        # Bounce when hitting the bottom border
        if self.__y + self.__radius >= self.__window_height:
            self.__y_vel *= -1

        # Bounce off left/right borders
        if self.__x + self.__radius >= self.__window_width or \
            self.__x - self.__radius <= 0:
            self.__x_vel *= -1

        # Move the ball, accelerate downwards
        self.__y += self.__y_vel    
        self.__y_vel += self.__accel
        self.__x += self.__x_vel

class Rectangle():
    def __init__(self, x, y, screen, color=(0,0,255), width=50, height=20, \
        y_vel=0.02, x_vel=0.05, accel=0.0005, window_height=500, window_width=700):
        '''
        Call this to create me!
        '''
        self.__x_vel = x_vel

        self.__x = x
        self.__y = y
        self.__screen = screen
        self.__color = color
        self.__width = width
        self.__height = height
        self.__y_vel = y_vel
        self.__accel = accel
        self.__window_width = window_width
        self.__window_height = window_height

    def draw(self):
        '''
        Call this to put me on the screen!
        '''
        pygame.draw.rect(self.__screen,
             self.__color, 
             pygame.Rect(self.__x, self.__y, self.__width, self.__height)
        )

        self.__move()

    def __move(self):
        '''
        This defines how my position changes over time.
        '''

        if self.__y + self.__height >= self.__window_height:
            self.__y_vel *= -1
        self.__y += self.__y_vel    
        self.__y_vel += self.__accel

        # Move left/right
        if self.__x + self.__width >= self.__window_width or \
            self.__x <= 0:
            self.__x_vel *= -1
        self.__x += self.__x_vel

class Animation:
    def __init__(self, width, height):
        pygame.init()
        self.__width = width
        self.__height = height
        self.__shapes = []
        self.screen = pygame.display.set_mode([self.__width, self.__height])
    
    def add_shape(self, shape):
        self.__shapes.append(shape)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw the next frame
            self.screen.fill((255, 255, 255))
            for shape in self.__shapes:
                shape.draw()
            pygame.display.flip()
    

        pygame.quit()


animation = Animation(700, 500)

animation.add_shape( Ball(x=200, y=250, screen=animation.screen) )
animation.add_shape( Ball(x=400, y=250, color=(0, 255, 0), x_vel=0.04, screen=animation.screen) )
animation.add_shape( Ball(x=300, y=250, color=(200, 100, 0), x_vel=-0.04, radius=20, screen=animation.screen,
                             is_tracking=True) )
animation.add_shape( Rectangle( x=100, y=50, color=(100, 200, 0), \
                    width=50, height=50, x_vel=-0.06, y_vel=0.08, screen=animation.screen) )
animation.add_shape( Rectangle( x=500, y=30, color=(255, 51, 153), \
                    width=30, height=30, x_vel=-0, y_vel=0.07, screen=animation.screen) )
animation.add_shape( Rectangle( x=550, y=300, color=(255, 102, 0), \
                    width=70, height=20, x_vel=-0, y_vel=0.001, screen=animation.screen) )
animation.run()
