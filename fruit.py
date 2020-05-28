import pygame
from random import randint
from gameObject import GameObject

class Fruit(GameObject):


    # Value represents by how much the snake grows when consumed
    def __init__(self, x_pos, y_pos, length, value=1):
        super().__init__(x_pos, y_pos, length, length, (255,0,0))
        self.value = value


    # def generate_random_location(self, screen, snake):
    #     blocks = snake.blocks
    #     max_x = screen.get_width() - snake.block_length
    #     max_y = screen.get_height() - snake.block_length

    #     block_length = snake.block_length
    #     possible_locations = []
    #     for x in range(0,max_x,block_length):
    #         for y in range(0,max_y,block_length):
    #             possible_locations.append((x,y))
    #             for block in snake.block:
    #                 if block.x_pos == x and block.y_pos == y:
    #                     possible_locations.pop()


    #     # max_x, max_y = screen.get_size()
    #     # max_x -= self.width
    #     # max_y -= self.height

    #     # random_x = randint(0,max_x)
    #     # random_y = randint(0,max_y)

    #     # self.x_pos = random_x
    #     # self.y_pos = random_y

    #     # # Handle actual checking and random generation
    #     locations = (
    #         (60,60),
    #         (440,60),
    #         (440,440),
    #         (60,440))
    #     rand_index = randint(0,3)
    #     self.x_pos, self.y_pos = locations[rand_index]
