import pygame
import numpy as np

from constants import CELL_SIZE, COLOR_FREE, COLOR_GRID_LINE, COLS, GRID_LINE_WIDTH, ROWS, WALL

def draw_grid(screen: pygame.Surface, maze: np.ndarray) -> None:
    for row in range(ROWS):
        for col in range(COLS):

            cell = maze[row][col]
            if cell == WALL:
                color = (0, 0, 0)
            else:
                color = COLOR_FREE

            rect = pygame.Rect(
                col * CELL_SIZE, 
                row * CELL_SIZE, 
                CELL_SIZE, 
                CELL_SIZE
            )

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, COLOR_GRID_LINE, rect, GRID_LINE_WIDTH)
