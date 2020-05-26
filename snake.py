import pygame
from gameObject import GameObject
from snakeBlock import SnakeBlock

class Snake:


    def __init__(self, screen, block_length):
        self.blocks = []
        self.block_length = block_length
        width, height = screen.get_size()
        x_pos = (width / 2) - (block_length / 2)
        y_pos = (height / 2) - (block_length / 2)
        self.blocks.append(SnakeBlock(x_pos, y_pos, block_length, (0,255,0)))
        self.num_blocks = 1


    def update_pos_by_amount(self, x, y):
        x_pos = self.blocks[0].x_pos + x
        y_pos = self.blocks[0].y_pos + y
        self.blocks[0].update_pos_to(x_pos, y_pos)


    def check_if_collided_with_edges(self, screen):
        max_x, max_y = self.blocks[0].get_max_x_and_y()
        return self.blocks[0].x_pos < 0 or max_x > screen.get_width() or self.blocks[0].y_pos < 0 or max_y > screen.get_height()


    def check_if_collided_with_self(self):
        for i in range(3, self.num_blocks):
            current_block = self.blocks[i]
            snake_max_x, snake_max_y = self.blocks[0].get_max_x_and_y()
            block_max_x, block_max_y = current_block.get_max_x_and_y()
            if self.blocks[0].x_pos < block_max_x and snake_max_x > current_block.x_pos and self.blocks[0].y_pos < block_max_y and snake_max_y > current_block.y_pos:
                return True


    def check_if_collected_fruit(self, fruit):
        snake_max_x, snake_max_y = self.blocks[0].get_max_x_and_y()
        fruit_max_x, fruit_max_y = fruit.get_max_x_and_y()

        if self.blocks[0].x_pos < fruit_max_x and snake_max_x > fruit.x_pos and self.blocks[0].y_pos < fruit_max_y and snake_max_y > fruit.y_pos:
            self.add_block()
            return True
        return False


    def add_block(self):
        last_block = self.blocks[self.num_blocks - 1]
        new_block = SnakeBlock(last_block.x_pos, last_block.y_pos, self.block_length)
        last_block.next_block = new_block
        self.blocks.append(new_block)
        self.num_blocks += 1
        

    def draw(self, pygame, screen):
        for block in self.blocks:
            block.draw(pygame, screen)


