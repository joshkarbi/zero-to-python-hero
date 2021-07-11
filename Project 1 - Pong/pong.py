import pygame, random, time
from dataclasses import dataclass
from typing import Tuple

@dataclass
class PongBall:
    x: float
    y: float
    x_velocity: float
    y_velocity: float
    radius: int
    color: Tuple[int, int, int]

@dataclass
class Paddle:
    x: float
    y: float
    width: float
    height: float
    x_velocity: float=0

class PongGame:
    def __init__(self, screen, color=(0,0,0), y_vel=0.17, x_vel=0.17, 
        window_height=500, window_width=700):
        '''
        Call this to create me!
        '''
        self.__screen = screen
        self.__window_width = window_width
        self.__window_height = window_height

        self.ball = PongBall(
            x = window_width-100, y=window_height/2,
            x_velocity=x_vel, y_velocity=y_vel, 
            radius=int(window_width*0.01), color=color
        )

        self.PADDLE_MOVE_SPEED = 0.15
        self.paddles = [
                Paddle(
                    x=50, y=30, width=100, height=10
                ),
                Paddle(
                    x=window_width-300, y=window_height-50, width=100, height=10
                )
        ]

        self.score = [0, 0]

    def draw(self):
        # The ball
        pygame.draw.circle(self.__screen,
             self.ball.color, 
             (self.ball.x, self.ball.y),
             self.ball.radius
        )
        # The paddles
        for paddle in self.paddles:
            pygame.draw.rect(self.__screen,
                self.ball.color, 
                pygame.Rect(paddle.x, paddle.y, paddle.width, paddle.height)
            )

        self.__draw_score()
        self.__move_ball()
        self.__move_paddles()

    def __draw_score(self):
        score_str = f"{self.score[0]} - {self.score[1]}"
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        text = font.render(score_str, True, BLACK, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (200, 200)
        self.__screen.blit(text, text_rect)

    def handle_game_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.paddles[1].x_velocity = -1 * self.PADDLE_MOVE_SPEED
            elif event.key == pygame.K_RIGHT:
                self.paddles[1].x_velocity = self.PADDLE_MOVE_SPEED
            
            elif event.key == pygame.K_a:
                self.paddles[0].x_velocity = -1 * self.PADDLE_MOVE_SPEED
            elif event.key == pygame.K_d:
                self.paddles[0].x_velocity = self.PADDLE_MOVE_SPEED

    def __reset_game(self):
        time.sleep(1)
        self.ball.x = self.__window_width/2
        self.ball.y = self.__window_height/2
        
        self.__screen.fill((255, 255, 255))
        pygame.draw.circle(self.__screen,
             self.ball.color, 
             (self.ball.x, self.ball.y),
             self.ball.radius
        )
        for paddle in self.paddles:
            pygame.draw.rect(self.__screen,
                self.ball.color, 
                pygame.Rect(paddle.x, paddle.y, paddle.width, paddle.height)
            )
        self.__draw_score()
        pygame.display.flip()
        time.sleep(1)

    def __move_ball(self):
        # Update scoring
        if self.ball.y + self.ball.radius >= self.__window_height:
            self.score[0] += 1
            self.__reset_game()
        elif self.ball.y - self.ball.radius <= 0:
            self.score[1] += 1
            self.__reset_game()

        # Bounce off left/right borders
        if self.ball.x + self.ball.radius >= self.__window_width or \
            self.ball.x - self.ball.radius <= 0:
            self.ball.x_velocity *= -1

        # Bounce of paddles
        if int(self.ball.y - self.ball.radius + 3) == \
            int(self.paddles[0].y+self.paddles[0].height) and  \
            self.ball.x <= self.paddles[0].x+self.paddles[0].width and \
            self.ball.x >= self.paddles[0].x:
            self.ball.y_velocity *= -1
        elif int(self.ball.y + self.ball.radius - 5) == \
            int(self.paddles[1].y) and \
            self.ball.x <= self.paddles[1].x+self.paddles[1].width and \
            self.ball.x >= self.paddles[1].x:
            self.ball.y_velocity *= -1

        # Move the ball, accelerate downwards
        self.ball.y += self.ball.y_velocity   
        self.ball.x += self.ball.x_velocity

    def __move_paddles(self):       
        for paddle in self.paddles:
            if not (paddle.x <= 0 and paddle.x_velocity < 0) and \
                not (paddle.x + paddle.width >= \
                self.__window_width and paddle.x_velocity > 0):

                paddle.x += paddle.x_velocity


def run_game():
    pygame.init()
    WINDOW_WIDTH, WINDOW_HEIGHT = 700, 500
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    pygame.display.set_caption('Pong!')

    game = PongGame(screen)
    running = True

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        else:
            game.handle_game_event(event)
        
        screen.fill((255, 255, 255))
        game.draw()
        pygame.display.flip()
        
    pygame.quit()

run_game()