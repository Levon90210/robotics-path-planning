import pygame

from visualization import draw_grid
from maze import create_empty_maze
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, COLOR_BG, FPS

SCREEN_CAPTION = "Robotics Project"

def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(SCREEN_CAPTION)

    clock = pygame.time.Clock()
    running = True

    maze = create_empty_maze()
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(COLOR_BG)
        draw_grid(screen, maze)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()

