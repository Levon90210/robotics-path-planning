import pygame
import numpy as np

from robot import Robot
from astar import Position
from constants import (
    CELL_SIZE,
    COLOR_FREE,
    COLOR_GOAL,
    COLOR_GRID_LINE,
    COLOR_ROBOT,
    COLOR_WALL,
    COLOR_UNKNOWN,
    COLOR_PATH,
    COLS,
    GRID_LINE_WIDTH,
    ROWS,
    WALL,
    UNKNOWN,
)


def draw_grid(
    screen: pygame.Surface, maze: np.ndarray, offset_x: int = 0, offset_y: int = 0
) -> None:
    for row in range(ROWS):
        for col in range(COLS):
            cell = maze[row][col]
            if cell == UNKNOWN:
                color = COLOR_UNKNOWN
            elif cell == WALL:
                color = COLOR_WALL
            else:
                color = COLOR_FREE
            rect = pygame.Rect(
                offset_x + col * CELL_SIZE,
                offset_y + row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, COLOR_GRID_LINE, rect, GRID_LINE_WIDTH)


def draw_robot(
    screen: pygame.Surface, robot: Robot, offset_x: int = 0, offset_y: int = 0
) -> None:
    center_x = offset_x + robot.col * CELL_SIZE + CELL_SIZE // 2
    center_y = offset_y + robot.row * CELL_SIZE + CELL_SIZE // 2
    radius = CELL_SIZE // 3
    pygame.draw.circle(screen, COLOR_ROBOT, (center_x, center_y), radius)


def draw_goal(
    screen: pygame.Surface, goal: Position, offset_x: int = 0, offset_y: int = 0
) -> None:
    row, col = goal
    rect = pygame.Rect(
        offset_x + col * CELL_SIZE, offset_y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE
    )
    pygame.draw.rect(screen, COLOR_GOAL, rect)


def draw_path(
    screen: pygame.Surface, path: list[Position], offset_x: int = 0, offset_y: int = 0
) -> None:
    for row, col in path:
        rect = pygame.Rect(
            offset_x + col * CELL_SIZE + CELL_SIZE // 4,
            offset_y + row * CELL_SIZE + CELL_SIZE // 4,
            CELL_SIZE // 2,
            CELL_SIZE // 2,
        )
        pygame.draw.rect(screen, COLOR_PATH, rect)
