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
    Direction is number 0 for no movement, 1 for down, 2 for for left and 3 for right.
    Squares will be moved in the array, the actualised array will be returned.
    THE MOVE MUST BE POSSIBLE, NO CHECK IN THIS FUNCTION.
    """
    for square in squares:
        square.move(direction)
    return squares

def put_squares_on_grid(grid, squares):
    for square in squares:
        grid = square.put_on_grid(grid)
    return grid

def display_squares(window, textures, squares):
    for square in squares:
        square.display(window, textures)

def score(number_of_deleted_lines, level):
    """
    n is the level
           1 Line          2 Line          3 Line          4 Line
    n	40 * (n + 1)	100 * (n + 1)	300 * (n + 1)	1200 * (n + 1)

    """
    if 1 == number_of_deleted_lines:
        score = 40*(level+1)
        return score
    elif 2 == number_of_deleted_lines:
        score = 100*(level+1)
        return score
    elif 3 == number_of_deleted_lines:
        score = 300*(level+1)
        return score
    elif 4 == number_of_deleted_lines:
        score = 1200*(level+1)
        return score

def generate_square():
    """
    Randomly generate a piece from the list below:

    0 = Red     [][]
                  [][]

    1 = Blue    []
                [][][]

    2 = Green     [][]
                [][]

    3 = Yellow  [][]
                [][]

    4 = Cyan    [][][][]


    5 = Purple    []
                [][][]

    6 = Orange      []
                [][][]

    """
    from random import randrange

    choice = randrange(0,8)

    if choice == 0:
       return [Square(choice, 4, 0), Square(choice, 5, 0), Square(choice, 5, 1), Square(choice, 6, 1)]

    elif choice == 1:
        return [Square(choice, 4, 0), Square(choice, 4, 1), Square(choice, 5, 1), Square(choice, 6, 1)]

    elif choice == 2:
        return [Square(choice, 6, 0), Square(choice, 5, 0), Square(choice, 5, 1), Square(choice, 4, 1)]

    elif choice == 3:
        return [Square(choice, 4, 0), Square(choice, 5, 0), Square(choice, 5, 1), Square(choice, 4, 1)]

    elif choice == 4:
        return [Square(choice, 6, 0), Square(choice, 5, 0), Square(choice, 4, 0), Square(choice, 3, 0)]

    elif choice == 5:
        return [Square(choice, 5, 0), Square(choice, 6, 1), Square(choice, 5, 1), Square(choice, 4, 1)]

    elif choice == 6:
        return [Square(choice, 5, 0), Square(choice, 5, 1), Square(choice, 4, 1), Square(choice, 3, 1)]

    elif choice == 7:
        return [Square(choice, 5,0)]

def rotate_squares(squares):
    xmin = 10
    xmax = 0
    ymin = 20
    ymax = 0

    for square in squares:
        if square.x < xmin:
            xmin = square.x
        if square.y < ymin:
            ymin = square.y
        if square.x > xmax:
            xmax = square.x
        if square.y > ymax:
            ymax = square.y

    array2d = []
    for x in range(xmax - xmin + 1):
        temp = []
        for y in range(ymax - ymin + 1):
            v = 8
            for square in squares:
                if square.x - xmin == x and square.y - ymin == y:
                    v = square.color_number
            temp.append(v)
        array2d.append(temp)

    array2d = list(zip(*array2d[::-1]))

    array2 = []

    for x in range(ymax - ymin + 1):
        for y in range(xmax - xmin + 1):
            if array2d[x][y] != 8:
                array2.append(Square(array2d[x][y], x+xmin, y+ymin))

    return array2

def load_textures():
    """
    Return an array of 8 colored block textures + 1 background.
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
    raimbow = pygame.image.load("textures/raimbow_square.png")
    return [red, blue, green, yellow, cyan, purple, orange, raimbow, background]

def delete_completed_lines(grid):
    """
    Delete completed lines on the grid, return the grid and the number of deleted lines.
    """

    total_line_values = []
    for y in range(20):
        total_line_values.append(True)

    for x in range(10):
        for y in range(20):
            if total_line_values[y] and grid[x][y].get_color() == 8:
                total_line_values[y] = False

    go_down_numbers = []
    for y in range(20):
        number = 0
        for y2 in range(y, 20):
            if total_line_values[y2]:
                number += 1
        go_down_numbers.append(number)

    for y in range(20):
        for x in range(10):
            for i in range(go_down_numbers[y]):
                grid[x][y].move(1)

    number = 0
    for y in range(20):
        if total_line_values[y]:
            number += 1
            for x in range(10):
                grid[x].pop(y)
                grid[x].insert(0, Square(8,x,0))

    return (grid, number)

def get_displayable_next_falling_squares(squares):
    for _i in range(8):
        squares = move_squares(squares, 3)
    squares = move_squares(squares, 1)
    return squares

import time
from copy import deepcopy

print("Loading texture")
textures = load_textures()
falling = generate_square()
next_falling = generate_square()
displayable_next_falling = get_displayable_next_falling_squares(deepcopy(next_falling))
timer = time.time()

print("Creating window")
import pygame
import time
pygame.init()
window = pygame.display.set_mode((50*10+50*7, 50*20))
pygame.key.set_repeat(103)

grid = []
for x in range(10):
    temp = []
    for y in range(20):
        temp.append(Square(7,x,y))
    grid.append(temp)

for y in range(20):
    for x in range(10):
        grid[x][y] = Square(8,x,y)
    window.fill((0,0,0))
    window.blit(textures[8], (0,0))
    display_grid(window, textures, grid)
    pygame.display.flip()

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
            if event.key == pygame.K_UP:
                rotated = rotate_squares(falling)
                if can_squares_move(grid, rotated, 0):
                    falling = rotated
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
            grid = put_squares_on_grid(grid, falling)
            falling = next_falling
            next_falling = generate_square()
            displayable_next_falling = get_displayable_next_falling_squares(deepcopy(next_falling))
            if can_squares_move(grid, falling, 0) == False:
                print("game over")
                ingame = 0
                grid = []
                for x in range(10):
                    temp = []
                    for y in range(20):
                        temp.append(Square(8,x,y))
                    grid.append(temp)

                for y in range(20):
                    for x in range(10):
                        grid[x][y] = Square(7,x,y)
                    window.fill((0,0,0))
                    window.blit(textures[8], (0,0))
                    display_grid(window, textures, grid)
                    pygame.display.flip()

                pygame.quit()

    if ingame:
        (grid, number_of_deleted_lines) = delete_completed_lines(grid)

        window.fill((0,0,0))
        window.blit(textures[8], (0,0))
        display_grid(window, textures, grid)
        display_squares(window, textures, falling)
        display_squares(window, textures, displayable_next_falling)
        pygame.display.flip()

print("Exiting")
pygame.quit()
