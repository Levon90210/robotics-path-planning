import pygame

from constants import CELL_SIZE, COLOR_FREE, COLOR_GRID_LINE, COLS, GRID_LINE_WIDTH, ROWS

def draw_grid(screen: pygame.Surface) -> None:
    for row in range(ROWS):
        for col in range(COLS):

            rect = pygame.Rect(
                col * CELL_SIZE, 
                row * CELL_SIZE, 
                CELL_SIZE, 
                CELL_SIZE
            )

            pygame.draw.rect(screen, COLOR_FREE, rect)
            pygame.draw.rect(screen, COLOR_GRID_LINE, rect, GRID_LINE_WIDTH)
