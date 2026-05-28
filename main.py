import pygame
import numpy as np

from robot import Robot
from astar import astar
from maze import generate_maze
from visualization import draw_grid, draw_robot
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, COLOR_BG, FPS, ROWS, COLS, MOVE_DELAY

SCREEN_CAPTION = "Robotics Project"


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(SCREEN_CAPTION)

    clock = pygame.time.Clock()
    running = True

    maze = generate_maze(ROWS, COLS)

    robot = Robot(row=1, col=1)
    goal = (ROWS - 2, COLS - 2)
    path = astar(maze, (robot.row, robot.col), goal)
    path_index = 0
    last_move_time = pygame.time.get_ticks()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()
        if current_time - last_move_time > MOVE_DELAY:
            if path and path_index < len(path):
                robot.row, robot.col = path[path_index]
                path_index += 1
            last_move_time = current_time

        screen.fill(COLOR_BG)

        draw_grid(screen, maze)
        draw_robot(screen, robot)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
