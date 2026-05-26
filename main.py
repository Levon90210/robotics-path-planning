import pygame
import numpy as np

from robot import Robot
from astar import astar, Position
from maze import create_empty_maze
from visualization import draw_grid, draw_robot
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, COLOR_BG, FPS, ROWS, COLS

SCREEN_CAPTION = "Robotics Project"

def get_path(maze: np.ndarray, start: Position, goal: Position):
    return [start, (start[0], start[1] + 1), (start[0] + 1, start[1] + 1), goal]

def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(SCREEN_CAPTION)

    clock = pygame.time.Clock()
    running = True

    maze = create_empty_maze()

    robot = Robot(row=1, col=1)

    goal = (ROWS - 2, COLS - 2)

    path = get_path(maze, (robot.row, robot.col), goal)

    path_index = 0

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if path_index < len(path):
            robot.row, robot.col = path[path_index]
            path_index += 1

        screen.fill(COLOR_BG)

        draw_grid(screen, maze)
        draw_robot(screen, robot)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()

