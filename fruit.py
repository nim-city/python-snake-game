import pygame
from random import randint
from gameObject import GameObject

class Fruit(GameObject):


    def __init__(self, length):
        super().__init__(0, 0, length, length, (255,0,0))


    def generate_random_location(self, screen, disallowed_locations=[]):
        # max_x, max_y = screen.get_size()
        # max_x -= self.width
        # max_y -= self.height

        # random_x = randint(0,max_x)
        # random_y = randint(0,max_y)

        # self.x_pos = random_x
        # self.y_pos = random_y

        # # Handle actual checking and random generation
        locations = (
            (50,50),
            (430,50),
            (430,430),
            (50,430))
        rand_index = randint(0,3)
        self.x_pos, self.y_pos = locations[rand_index]
