import numpy as np
import random


def generate_maze(rows: int, cols: int) -> np.ndarray:

    maze = np.ones((rows, cols), dtype=np.int8)

    start_r, start_c = 1, 1
    maze[start_r][start_c] = 0

    stack = [(start_r, start_c)]

    while stack:
        r, c = stack[-1]

        neighbors = []
        for dr, dc in ((-2, 0), (2, 0), (0, -2), (0, 2)):
            nr, nc = r + dr, c + dc
            if 1 <= nr < rows - 1 and 1 <= nc < cols - 1 and maze[nr][nc] == 1:
                neighbors.append((nr, nc, dr, dc))

        if neighbors:
            nr, nc, dr, dc = random.choice(neighbors)
            maze[r + dr // 2][c + dc // 2] = 0
            maze[nr][nc] = 0
            stack.append((nr, nc))
        else:
            stack.pop()

    goal_r, goal_c = rows - 2, cols - 2
    maze[goal_r][goal_c] = 0

    if goal_r % 2 == 0:
        maze[goal_r - 1][goal_c] = 0
    if goal_c % 2 == 0:
        maze[goal_r][goal_c - 1] = 0

    return maze

# maze = generate_maze(21, 21)
# for row in maze:
#     for cell in row:
#         print("█" if cell == 1 else " ", end="")
#     print()