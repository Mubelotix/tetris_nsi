def display_square(window, textures, square_color_number, x, y):
    """
    Draw a single square on the window. Coords 0;0 is the square to the top left.
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
    if square_color_number < 7 and square_color_number > 0:
        window.blit(textures[square_color_number], (50+x*50, y*50))

def display_grid(window, textures, grid):
    """
    Draw every squares of the grid to the window.
    """
    for x in range(10):
        for y in range(20):
            display_square(window, textures, grid[x][y], x, y)

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

print("Loading texture")
textures = load_textures()
grid = [
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,5],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
]

print("Creating window")
import pygame
pygame.init()
window = pygame.display.set_mode((50*10+50*7, 50*20))

print("Starting loop")
ingame = True
while ingame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ingame = 0

    display_grid(window, textures, grid)
    pygame.display.flip()

print("Exiting")
pygame.quit()
