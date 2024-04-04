import pygame
import sys
from pygame.locals import *

# Constants
BOARD_SIZE = 3
TILE_SIZE = 150
WINDOW_WIDTH = BOARD_SIZE * TILE_SIZE
WINDOW_HEIGHT = BOARD_SIZE * TILE_SIZE + 40  # Increased height for the moves counter
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Game initialization
pygame.init()
fps_clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('8 Puzzle')

# Set icon
icon = pygame.image.load('icon.png')  # Replace 'icon.png' with your icon file path
pygame.display.set_icon(icon)

# Font
font = pygame.font.Font(None, 36)

# Board setup
board = [[4, 1, 3],[ 7, 2, 5], [8, 0, 6]]
empty_tile_pos = (2, 1)
move_counter = 0
solved = False

# Sound effects
move_sound = pygame.mixer.Sound('move_sound.wav')
solved_sound = pygame.mixer.Sound('solved_sound.wav')

# Helper function to check if a tile is movable
def is_movable(row, col):
    case1 = (abs(row - empty_tile_pos[0]) == 1 and col == empty_tile_pos[1]) 
    case2 = (row == empty_tile_pos[0] and abs(col - empty_tile_pos[1]) == 1)
    return case1 or case2

# Function to check if the board is solved
def is_solved():
    cnt = -1
    bouns = 0
    for i in range(0, 3):
        for j in range(0, 3):
            cnt += 1
            if board[i][j] == (cnt + 1):
                bouns += 1
    return bouns == 8

# Game loop
while True:
    window_surface.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and not solved:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // TILE_SIZE #floor division
            row = mouse_y // TILE_SIZE
            if is_movable(row, col):
                board[empty_tile_pos[0]][empty_tile_pos[1]], board[row][col] = board[row][col], board[empty_tile_pos[0]][empty_tile_pos[1]]
                empty_tile_pos = (row, col)
                move_counter += 1
                move_sound.play()
                if is_solved():
                    solved = True
                    print("Solved")
                    solved_sound.play()
            print(board)

    # Draw the board with borders
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            tile_number = board[row][col]
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(window_surface, BLACK, rect, 1)  # Draw border
            if tile_number != 0:
                pygame.draw.rect(window_surface, BLUE, rect)  # Fill tile with color
                text = font.render(str(tile_number), True, WHITE)
                text_rect = text.get_rect(center=(col * TILE_SIZE + TILE_SIZE / 2, row * TILE_SIZE + TILE_SIZE / 2))
                window_surface.blit(text, text_rect)

    # Draw move counter at the bottom of the window
    counter_text = font.render("Moves: " + str(move_counter), True, BLACK)
    window_surface.blit(counter_text, (10, WINDOW_HEIGHT - 40))

    # Draw solved text
    if solved:
        solved_text = font.render("Solved!", True, BLACK)
        window_surface.blit(solved_text, (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2))

    pygame.display.update()
    fps_clock.tick(FPS)
