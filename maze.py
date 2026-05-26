import numpy as np

from constants import ROWS, COLS

def create_empty_maze() -> np.ndarray:
    return np.zeros((ROWS, COLS), dtype=np.int8)
