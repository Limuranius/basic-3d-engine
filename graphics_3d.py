import pygame
import time
from objects import Object3D, Vector3D, Matrix4x4, Camera3D
import models

WIDTH = 800
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    objects = []

    obj = models.Cube()
    obj.set_pos(200, 0, -500)
    obj.set_rotation_speed(0, 1, 1)
    objects.append(obj)

    obj = models.CutPyramid()
    obj.set_pos(-200, 0, -500)
    obj.set_rotation_speed(0, 1, 0)
    obj.set_scale(50)
    objects.append(obj)

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
