import pygame
import numpy as np

from robot import Robot
from constants import (
    CELL_SIZE,
    COLOR_FREE,
    COLOR_GRID_LINE,
    COLOR_ROBOT,
    COLOR_WALL,
    COLS,
    GRID_LINE_WIDTH,
    ROWS,
    WALL,
)


def draw_grid(screen: pygame.Surface, maze: np.ndarray) -> None:
    for row in range(ROWS):
        for col in range(COLS):

            cell = maze[row][col]
            if cell == WALL:
                color = COLOR_WALL
            else:
                color = COLOR_FREE

            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, COLOR_GRID_LINE, rect, GRID_LINE_WIDTH)


def draw_robot(screen: pygame.Surface, robot: Robot) -> None:
    center_x = robot.col * CELL_SIZE + CELL_SIZE // 2
    center_y = robot.row * CELL_SIZE + CELL_SIZE // 2

    radius = CELL_SIZE // 3

    pygame.draw.circle(screen, COLOR_ROBOT, (center_x, center_y), radius)
