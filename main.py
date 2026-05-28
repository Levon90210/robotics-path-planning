import pygame
import numpy as np
from typing import Optional

from robot import Robot
from maze import generate_maze
from astar import Position, astar
from visualization import draw_grid, draw_robot, draw_goal, draw_path
from constants import (
    LIDAR_RADIUS,
    PANEL_WIDTH,
    UNKNOWN,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    COLOR_BG,
    FPS,
    ROWS,
    COLS,
    WALL,
    MOVE_DELAY,
    DIRECTIONS,
)


def lidar_scan(real_maze: np.ndarray, known_maze: np.ndarray, robot: Robot) -> None:
    r0, c0 = robot.row, robot.col
    known_maze[r0][c0] = real_maze[r0][c0]
    for dr, dc in DIRECTIONS:
        for dist in range(1, LIDAR_RADIUS + 1):
            r = r0 + dr * dist
            c = c0 + dc * dist
            if not (0 <= r < ROWS and 0 <= c < COLS):
                break
            known_maze[r][c] = real_maze[r][c]
            if real_maze[r][c] == WALL:
                break


def main() -> None:
    pygame.init()

    pygame.display.set_caption("Robotics Path Planning")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    clock = pygame.time.Clock()
    running = True

    maze = generate_maze(ROWS, COLS)
    known_maze = np.full((ROWS, COLS), UNKNOWN, dtype=np.int8)
    robot = Robot(row=1, col=1)
    goal = (ROWS - 2, COLS - 2)

    last_move_time = pygame.time.get_ticks()
    path: Optional[list[Position]] = None
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()
        if current_time - last_move_time > MOVE_DELAY:
            lidar_scan(maze, known_maze, robot)
            path = astar(known_maze, (robot.row, robot.col), goal)
            if path and len(path) > 1:
                robot.row, robot.col = path[1]
            last_move_time = current_time

        screen.fill(COLOR_BG)

        draw_grid(screen, maze, offset_x=0)
        draw_grid(screen, known_maze, offset_x=PANEL_WIDTH)
        draw_goal(screen, goal, offset_x=0)
        draw_goal(screen, goal, offset_x=PANEL_WIDTH)
        if path:
            draw_path(screen, path, offset_x=PANEL_WIDTH)
        draw_robot(screen, robot, offset_x=0)
        draw_robot(screen, robot, offset_x=PANEL_WIDTH)
        pygame.draw.line(
            screen, (255, 255, 255), (PANEL_WIDTH, 0), (PANEL_WIDTH, WINDOW_HEIGHT), 5
        )

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
