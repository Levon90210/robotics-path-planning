import numpy as np

from constants import ROWS, COLS, WALL

def create_empty_maze() -> np.ndarray:
    maze = np.zeros((ROWS, COLS), dtype=np.int8)

    maze[0, :] = WALL
    maze[-1, :] = WALL
    maze[:, 0] = WALL
    maze[:, -1] = WALL

    maze[10, 5:20] = WALL
    maze[20, 10:25] = WALL

    return maze

