'''
Classic Snake game.
'''

import pygame
import random
import time
from dataclasses import dataclass
from typing import List, Tuple
from enum import Enum

class CellContent(Enum):
    NOTHING=0
    SNAKE=1
    FOOD=2

class SnakeMovement(Enum):
    NOTHING=0
    LEFT=1
    RIGHT=2
    DOWN=3
    UP=4

@dataclass
class SnakeBodyPart:
    x: int
    y: int
    x_vol: int
    y_vol: int
    move: SnakeMovement

@dataclass
class Food:
    x: int
    y: int

class Snake:
    '''
    Used to keep track of the snake body and where its going.
    '''

    def __init__(self, num_cells):
        self.NUM_CELLS = num_cells
        
        self.parts = [SnakeBodyPart(
            x=10, y=10, 
            x_vol=1, y_vol=0,
            move=SnakeMovement.NOTHING
        )]

        self.last_move_time = int(time.time())
        self.last_food_x = None
        self.last_food_y = None

    def update_positions(self):
        '''
        Apply movement.
        '''
        for i, part in enumerate(self.parts):
            # Set velocities.
            if part.move == SnakeMovement.LEFT:
                part.x_vol = -1
                part.y_vol = 0
            elif part.move == SnakeMovement.RIGHT:
                part.x_vol = 1
                part.y_vol = 0
            elif part.move == SnakeMovement.UP:
                part.x_vol = 0
                part.y_vol = -1
            elif part.move == SnakeMovement.DOWN:
                part.x_vol = 0
                part.y_vol = 1
            
            # Move the parts
            part.x += part.x_vol
            if part.x < 0:
                part.x = self.NUM_CELLS - 1
            elif part.x > self.NUM_CELLS - 1:
                part.x = 0
            part.y += part.y_vol
            if part.y < 0:
                part.y = self.NUM_CELLS - 1
            elif part.y > self.NUM_CELLS - 1:
                part.y = 0

        # After moving all the parts, propagate movements
        # From back to front, the parts get the move of the part in front of it.
        for i, part in reversed(list(enumerate(self.parts))):
            if i == 0:
                break
            self.parts[i].move = self.parts[i -1].move

    def get_position(self) -> List[Tuple[int, int]]:
        '''
        Return all the indices of where it is.
        '''
        PERIOD = 100*1e-3
        if time.time() - self.last_move_time > PERIOD:
            # update positions
            self.update_positions()
            self.last_move_time = time.time()
        return [(part.x, part.y) for part in self.parts]

    def eat_food(self, food: Food) -> bool:
        '''
        Check if we should eat the food right now.
        If so grow in length and return True.
        '''
        eating = self.parts[0].x == food.x and \
            self.parts[0].y == food.y and \
            not(food.x == self.last_food_x and food.y == self.last_food_y)
        if eating:
            self.grow()
            self.last_food_x = food.x
            self.last_food_y = food.y
            return True
        return False

    def grow(self):
        '''
        Append a new body part.
        '''
        tail = self.parts[-1]
        new_x = tail.x - tail.x_vol
        new_y = tail.y - tail.y_vol
        self.parts.append(
            SnakeBodyPart(
                x=new_x, y=new_y, 
                x_vol=tail.x_vol, y_vol=tail.y_vol,
               move=SnakeMovement.NOTHING
            )
        )

    def handle_key(self, key):
        '''
        Set the movement of the head
        '''
        if key == pygame.K_LEFT and self.parts[0].x_vol == 0:
            self.parts[0].move = SnakeMovement.LEFT
        elif key == pygame.K_RIGHT and self.parts[0].x_vol == 0:
            self.parts[0].move = SnakeMovement.RIGHT
        elif key == pygame.K_UP and self.parts[0].y_vol == 0:
            self.parts[0].move = SnakeMovement.UP
        elif key == pygame.K_DOWN and self.parts[0].y_vol == 0:
            self.parts[0].move = SnakeMovement.DOWN

class SnakeGame:
    def __init__(self, screen, window_height=500, window_width=500):
        
        self.__screen = screen
        self.__window_width = window_width
        self.__window_height = window_height
        self.__snake_color = (0, 255, 0)
        self.__food_color = (255, 0, 0)
        self.__cell_color = (0, 0, 0)
        self.__num_cells = 20
        self.__cell_width = self.__window_width / self.__num_cells
        self.__cell_height = self.__window_height / self.__num_cells

        self.blank_board = lambda: [[CellContent.NOTHING for _ in range(self.__num_cells)] for __ in range(self.__num_cells)]

        # State.
        self.content = self.blank_board()
        self.snake = Snake(self.__num_cells)
        self.food = Food(x=4, y=14)
        self.is_over = False

    def update_food(self):
        '''
        Pick a new location for food.
        '''
        while True:
            self.food.x = random.randint(0, self.__num_cells - 1)
            self.food.y = random.randint(0, self.__num_cells - 1)
            if (self.food.x, self.food.y) not in self.snake.get_position():
                break
    
    def update(self):
        '''
        Move things.
        '''
        if not self.is_over:
            self.content = self.blank_board()
            seen_snake_parts = set()
            for x, y in self.snake.get_position():
                if (x,y) in seen_snake_parts:
                    self.is_over=True
                seen_snake_parts.add((x,y))
                self.content[x][y] = CellContent.SNAKE
            self.content[self.food.x][self.food.y] = CellContent.FOOD
            ate = self.snake.eat_food(self.food)
            if ate:
                self.update_food()

    def draw(self):
        '''
        Draw the game on every frame.
        '''
        self.update()

        for i, row in enumerate(self.content):
            for j, cell in enumerate(row):
                cell_x = i * self.__cell_width
                cell_y = j * self.__cell_height
                draw_cell = lambda color: pygame.draw.rect(self.__screen,
                        color, 
                        pygame.Rect(cell_x, cell_y, self.__cell_width, self.__cell_height),
                        1
                    )
                if cell == CellContent.NOTHING:
                    draw_cell(self.__cell_color)
                elif cell == CellContent.SNAKE:
                    draw_cell(self.__snake_color)
                    pygame.draw.rect(self.__screen,
                        self.__snake_color, 
                        pygame.Rect(cell_x, cell_y, self.__cell_width, self.__cell_height),
                    )
                elif cell == CellContent.FOOD:
                    draw_cell(self.__food_color)
                    pygame.draw.rect(self.__screen,
                        self.__food_color, 
                        pygame.Rect(cell_x, cell_y, self.__cell_width, self.__cell_height),
                    )

    def handle_game_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.snake.handle_key(event.key)
            

def run_game():
    pygame.init()
    WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    pygame.display.set_caption('Snake!')

    game = SnakeGame(screen)
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