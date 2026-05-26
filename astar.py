import numpy as np

Position = tuple[int, int]

def astar(maze: np.ndarray, start: Position, goal: Position) -> list[Position]:
    """
    Returns a list of (row, col) from start to goal inclusive.
    If no path exists, return empty list.
    """
    raise NotImplementedError("A* not implemented yet")
