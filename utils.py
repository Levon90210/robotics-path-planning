import numpy as np

from constants import WALL


def is_valid_cell(maze: np.ndarray, row: int, col: int) -> bool:
    rows, cols = maze.shape

    if row < 0 or row >= rows:
        return False

    if col < 0 or col >= cols:
        return False

    if maze[row][col] == WALL:
        return False

    return True
