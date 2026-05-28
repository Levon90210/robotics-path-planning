import numpy as np

from constants import COLS, ROWS, WALL


def is_valid_cell(maze: np.ndarray, row: int, col: int) -> bool:
    if row < 0 and row >= ROWS:
        return False

    if col < 0 and col >= COLS:
        return False

    if maze[row][col] == WALL:
        return False

    return True
