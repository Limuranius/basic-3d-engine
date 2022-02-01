import pygame
import time
from objects import Object3D, Vector3D, Matrix4x4

WIDTH = 800
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def create_cube():
    object_vertices = [
        Vector3D(-1, -1, -1),
        Vector3D(-1, -1, 1),
        Vector3D(-1, 1, -1),
        Vector3D(-1, 1, 1),
        Vector3D(1, -1, -1),
        Vector3D(1, -1, 1),
        Vector3D(1, 1, -1),
        Vector3D(1, 1, 1),
    ]
    object_edges = [
        (0, 1),
        (0, 2),
        (0, 4),
        (3, 1),
        (3, 2),
        (3, 7),
        (5, 1),
        (5, 4),
        (5, 7),
        (6, 2),
        (6, 4),
        (6, 7),
    ]
    return Object3D(object_vertices, object_edges)


def create_cut_pyramid():
    object_vertices = [
        Vector3D(-1, -1, -1),
        Vector3D(-1, -1, 1),
        Vector3D(-0.5, 1, -0.5),
        Vector3D(-0.5, 1, 0.5),
        Vector3D(1, -1, -1),
        Vector3D(1, -1, 1),
        Vector3D(0.5, 1, -0.5),
        Vector3D(0.5, 1, 0.5),
    ]
    object_edges = [
        (0, 1),
        (0, 2),
        (0, 4),
        (3, 1),
        (3, 2),
        (3, 7),
        (5, 1),
        (5, 4),
        (5, 7),
        (6, 2),
        (6, 4),
        (6, 7),
    ]
    return Object3D(object_vertices, object_edges)


def main():
    objects = [create_cut_pyramid()]
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        """Main Loop"""
        WIN.fill(BLACK)
        for i in range(len(objects)):
            objects[i].draw(WIN, WHITE)
            time.sleep(1/60)
        pygame.display.update()

    pygame.quit()


main()
