import pygame
from random import randint
from snake import Snake
from gameTile import GameTile
from fruit import Fruit

class GameWorld:


    def __init__(self, screen, block_length):
        tiles = []
        self.width =  screen.get_width()
        self.height = screen.get_height()
        for y in range(0,self.height,block_length):
            for x in range(0,self.width,block_length):
                game_tile = GameTile(x,y,0)
                tiles.append(game_tile)
        self.tiles = tiles
        self.block_length = block_length
        self.snake = Snake(screen, block_length)
        self.generate_new_fruit()
        self.score = 0


    def change_block_state(self, x, y, to_state):
        num_rows = self.width / self.block_length
        col = x / self.block_length
        row = y / self.block_length
        index = int((row * num_rows) + col)
        self.tiles[index].state = to_state


    def get_free_tiles(self):
        free_tiles = []
        for tile in self.tiles:
            if tile.state == 0:
                free_tiles.append(tile)
        return free_tiles


    def generate_new_fruit(self):
        free_tiles = self.get_free_tiles()
        random_index = randint(0,len(free_tiles))
        random_tile = free_tiles[random_index]
        self.fruit = Fruit(random_tile.x_pos, random_tile.y_pos, self.block_length)


    def check_if_game_over(self):
        return self.snake.check_if_collided_with_edges(self.width, self.height) or self.snake.check_if_collided_with_self()


    def update(self, snake_x_change, snake_y_change):
        # Update snake status
        self.snake.update_pos_by_amount(snake_x_change, snake_y_change)
        self.change_block_state(self.snake.blocks[0].x_pos, self.snake.blocks[0].y_pos, 1)
        self.change_block_state(self.snake.blocks[-1].x_pos, self.snake.blocks[-1].y_pos, 0)
        # Check for fruit collisions
        if self.snake.check_if_collected_fruit(self.fruit):
            self.score += self.fruit.value
            self.generate_new_fruit()
    


    




