import pygame
from gameObject import GameObject

class SnakeBlock(GameObject):


    def __init__(self, x_pos, y_pos, length, colour=(0,0,255)):
        super().__init__(x_pos, y_pos, length, length, colour)
        self.blocks = []
        self.next_block = None


    def update_pos_to(self, x, y):
        if self.next_block != None:
            self.next_block.update_pos_to(self.x_pos, self.y_pos)
        self.x_pos = x
        self.y_pos = y
