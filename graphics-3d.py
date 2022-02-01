import pygame
import time
from objects import Object3D, Vector3D, Matrix4x4, Camera3D
from models import create_cut_pyramid, create_cube

WIDTH = 800
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    objects = [create_cut_pyramid(
        (0, 0, -1000),
        (0, 0, 5),
        (0, 0, 0),
        (0, 1, 3)
    )]
    camera = Camera3D(Vector3D(0, 0, 0), Vector3D(0, 0, -1), Vector3D(0, 1, 0))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        """Main Loop"""
        WIN.fill(BLACK)
        for i in range(len(objects)):
            objects[i].draw(WIN, WHITE, camera)
            time.sleep(1 / 60)
        pygame.display.update()

    pygame.quit()


main()
