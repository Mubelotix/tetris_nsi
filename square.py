class Square:
    """
    A class representing a square.
    """
    color_number = 7
    x = 0
    y = 0

    def __init__(self, color_number, x, y):
        """
        Coords 0;0 is the square to the top left.
        Square colors:
            0 => red,
            1 => blue,
            2 => green,
            3 => yellow,
            4 => cyan,
            5 => purple,
            6 => orange,
            7 => empty
        """
        self.color_number = color_number
        self.x = x
        self.y = y

    def display(self, window, textures):
        """
        Display the square.
        """
        if self.color_number < 7 and self.color_number > 0:
            window.blit(textures[self.color_number], (50+self.x*50, self.y*50))

    def get_color(self):
        return self.color_number

    def can_move(self, grid, direction):
        """
        Return true if the square can move in a direction.
        Direction:
            1 => Down,
            2 => Left,
            _ => Right
        """
        if direction == 1:
            if self.y < 19:
                if grid[self.x][self.y + 1].get_color() == 7:
                    return True
        elif direction == 2:
            if self.x > 0:
                if grid[self.x - 1][self.y].get_color() == 7:
                    return True
        else:
            if self.x < 9:
                if grid[self.x + 1][self.y].get_color() == 7:
                    return True
        return False

    def move(self, direction):
        if direction == 1:
            self.y += 1
        elif direction == 2:
            self.x -= 1
        else:
            self.x += 1

    def put_on_grid(self, grid):
        grid[self.x][self.y] = self
        return grid