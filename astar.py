import heapq
import numpy as np
from constants import WALL, FREE, DIRECTIONS

Position = tuple[int, int]

def astar(maze: np.ndarray, start: Position, goal: Position) -> list[Position]:
    """
    Returns a list of (row, col) from start to goal inclusive.
    If no path exists, return empty list.
    """
    rows, cols = maze.shape

    if not (0 <= start[0] < rows and 0 <= start[1] < cols): return []
    if not (0 <= goal[0] < rows and 0 <= goal[1] < cols): return []
    if maze[start[0], start[1]] == constants.WALL or maze[goal[0], goal[1]] == constants.WALL:
        return []

    def heuristic(p1: Position, p2: Position) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    open_set = []
    count = 0
    heapq.heappush(open_set, (0, count, start))
    
    in_open = {start}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        current = heapq.heappop(open_set)[2]
        in_open.remove(current)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1] 

        for dr, dc in constants.DIRECTIONS:
            neighbor = (current[0] + dr, current[1] + dc)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
            
                if maze[neighbor[0], neighbor[1]] == constants.FREE:
                    
                    test_g_score = g_score[current] + 1

                    if test_g_score < g_score.get(neighbor, float('inf')):
                        came_from[neighbor] = current
                        g_score[neighbor] = test_g_score
                        f_score[neighbor] = test_g_score + heuristic(neighbor, goal)

                        if neighbor not in in_open:
                            count += 1
                            heapq.heappush(open_set, (f_score[neighbor], count, neighbor))
                            in_open.add(neighbor)

    return []