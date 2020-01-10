def display_slab(window, slab_color_number, x, y):
    """
    Draw a single square on the window. Coords 0;0 is the square to the top left.
    """
    pass

def display_grid(window, grid):
    """
    Draw every squares of the grid to the window.
    """
    # Utiliser la fonction display_slab()
    pass

def can_squares_move(grid, squares, direction):
    """
    Take the grid, an array of squares and a direction number.
    Direction is number 1 for down, 2 for for left and 3 for right.
    Return true if every square is able to move in the direction.
    """
    pass

def move_squares(grid, squares, direction):
    """
    Take the grid, an array of squares and a direction number.
    Direction is number 1 for down, 2 for for left and 3 for right.
    Squares will be moved in the array, the actualised array will be returned.
    THE MOVE MUST BE POSSIBLE, NO CHECK IN THIS FUNCTION.
    """
    pass

def load_textures():
    """
    Return an array of 7 colored block textures.
    """
    import pygame;
    red = pygame.image.load("textures/red_square.png")
    blue = pygame.image.load("textures/blue_square.png")
    green = pygame.image.load("textures/green_square.png")
    yellow = pygame.image.load("textures/yellow_square.png")
    cyan = pygame.image.load("textures/cyan_square.png")
    purple = pygame.image.load("textures/purple_square.png")
    orange = pygame.image.load("textures/orange_square.png")
    return [red, blue, green, yellow, cyan, purple, orange]
