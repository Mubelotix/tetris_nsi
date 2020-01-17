from square import *

def display_grid(window, textures, grid):
    """
    Draw every squares of the grid to the window.
    """
    for x in range(10):
        for y in range(20):
            grid[x][y].display(window, textures)

def can_squares_move(grid, squares, direction):
    """
    Take the grid, an array of squares and a direction number.
    Direction is number 1 for down, 2 for for left and 3 for right.
    Return true if every square is able to move in the direction.
    """
    for square in squares:
        if square.can_move(grid, direction) == False:
            return False
    return True

def move_squares(squares, direction):
    """
    Take the grid, an array of squares and a direction number.
    Direction is number 1 for down, 2 for for left and 3 for right.
    Squares will be moved in the array, the actualised array will be returned.
    THE MOVE MUST BE POSSIBLE, NO CHECK IN THIS FUNCTION.
    """
    for square in squares:
        square.move(direction)
    return squares

def put_squares_on_grid(grid, squares):
    for square in squares:
        grid = square.put_on_grid(grid)


def display_squares(window, textures, squares):
    for square in squares:
        square.display(window, textures)

def load_textures():
    """
    Return an array of 7 colored block textures + 1 background.
    """
    import pygame;
    red = pygame.image.load("textures/red_square.png")
    blue = pygame.image.load("textures/blue_square.png")
    green = pygame.image.load("textures/green_square.png")
    yellow = pygame.image.load("textures/yellow_square.png")
    cyan = pygame.image.load("textures/cyan_square.png")
    purple = pygame.image.load("textures/purple_square.png")
    orange = pygame.image.load("textures/orange_square.png")
    background = pygame.image.load("textures/background.png")
    return [red, blue, green, yellow, cyan, purple, orange, background]

import time

print("Loading texture")
textures = load_textures()
grid = []
falling = [Square(5, 5, 5), Square(5, 6, 5)]
timer = time.time()
for x in range(10):
    temp = []
    for y in range(20):
        temp.append(Square(7,x,y))
    grid.append(temp)

print("Creating window")
import pygame
import time
pygame.init()
window = pygame.display.set_mode((50*10+50*7, 50*20))

print("Starting loop")
ingame = True
last_move_date=time.time()
while ingame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ingame = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if can_squares_move(grid, falling, 2):
                    move_squares(falling, 2)
            if event.key == pygame.K_RIGHT:
                if can_squares_move(grid, falling, 3):
                    move_squares(falling, 3)
            if event.key == pygame.K_DOWN:
                if can_squares_move(grid, falling, 1):
                    move_squares(falling, 1)

    now = time.time()
    if now - timer > 1:
        timer = now
        if can_squares_move(grid, falling, 1):
            move_squares(falling, 1)
        else:
            put_squares_on_grid(grid, falling)
            falling = [Square(5, 5, 5), Square(5, 6, 5)]

    window.fill((0,0,0))
    window.blit(textures[7], (0,0))
    display_grid(window, textures, grid)
    display_squares(window, textures, falling)
    pygame.display.flip()

print("Exiting")
pygame.quit()
