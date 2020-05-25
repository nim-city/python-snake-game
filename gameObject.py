

class GameObject:


    def __init__(self, x_pos, y_pos, width, height, colour):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.colour = colour


    def get_max_x_and_y(self):
        return ((self.x_pos + self.width), (self.y_pos + self.height))


    def draw(self, pygame, screen):
        pygame.draw.rect(screen, self.colour, (self.x_pos, self.y_pos, self.width, self.height), 0)