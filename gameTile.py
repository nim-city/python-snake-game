

class GameTile:


    # State represents whether or not the tile is full
    # 0 = empty, 1 = snake, 2 = fruit
    def __init__(self, x, y, state=0):
        self.x_pos = x
        self.y_pos = y
        self.state = state