import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define the maze
maze = [
    "11111111111111111111",
    "10000000000000000001",
    "10111111111111111001",
    "10000000000000001001",
    "11111111111111101001",
    "10000000000000101001",
    "10111111111000101001",
    "10000000001000101001",
    "10111111101000101001",
    "10000000101000101001",
    "11110110101110101001",
    "10000110100000101001",
    "10111110111111101001",
    "10000000000000000001",
    "11111111111111111111"
]

# Maze dimensions
cell_size = 32
cols = len(maze[0])
rows = len(maze)

# Player settings
player_pos = [1, 1]
player_size = cell_size - 4

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        new_pos = [player_pos[0] - 1, player_pos[1]]
        if maze[new_pos[1]][new_pos[0]] == "0":
            player_pos = new_pos
    if keys[pygame.K_RIGHT]:
        new_pos = [player_pos[0] + 1, player_pos[1]]
        if maze[new_pos[1]][new_pos[0]] == "0":
            player_pos = new_pos
    if keys[pygame.K_UP]:
        new_pos = [player_pos[0], player_pos[1] - 1]
        if maze[new_pos[1]][new_pos[0]] == "0":
            player_pos = new_pos
    if keys[pygame.K_DOWN]:
        new_pos = [player_pos[0], player_pos[1] + 1]
        if maze[new_pos[1]][new_pos[0]] == "0":
            player_pos = new_pos

    # Draw the maze
    win.fill(BLACK)
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == "1":
                pygame.draw.rect(win, WHITE, (col * cell_size, row * cell_size, cell_size, cell_size))

    # Draw the player
    pygame.draw.rect(win, BLUE, (player_pos[0] * cell_size + 2, player_pos[1] * cell_size + 2, player_size, player_size))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
