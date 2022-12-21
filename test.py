import pygame
import numpy as np

# Set the dimensions of the grid
WIDTH = 800
HEIGHT = 600

# Set the size of each cell in the grid
CELL_SIZE = 20

# Set the number of rows and columns in the grid
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Set the colors for the cells
DEAD_COLOR = (128, 128, 128)
ALIVE_COLOR = (255, 255, 255)

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Set the window size and title
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")

# Create a 2D array to store the state of each cell
grid = np.zeros((ROWS, COLS))

# Set the initial state of the cells
# You can change this to create different starting patterns
grid[21, 21] = 1
grid[22, 22] = 1
grid[22, 23] = 1
grid[21, 23] = 1
grid[20, 23] = 1
grid[21, 24] = 1
# Set the running flag to True to start the game loop
running = True

# Start the game loop
while running:
    clock.tick(10)
    # Check for any events
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == pygame.QUIT:
            running = False

    # Update the state of the cells using the Game of Life rules
    # Create a copy of the grid to use for calculating the next state
    new_grid = grid.copy()
    for row in range(ROWS-1):
        for col in range(COLS-1):
            # Count the number of live neighbors for the current cell
            live_neighbors = (
                grid[row-1, col-1] + grid[row-1, col] + grid[row-1, col+1]
                + grid[row, col-1] + grid[row, col+1]
                + grid[row+1, col-1] + grid[row+1, col] + grid[row+1, col+1]
            )

            # Apply the Game of Life rules to determine the next state of the cell
            if grid[row, col] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[row, col] = 0
            else:
                if live_neighbors == 3:
                    new_grid[row, col] = 1

    # Update the grid with the new state
    grid = new_grid

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the cells on the screen
    for row in range(ROWS):
        for col in range(COLS):
            color = DEAD_COLOR if grid[row, col] == 0 else ALIVE_COLOR
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

            # Update the display
    pygame.display.flip()

        # Quit pygame
pygame.quit()
