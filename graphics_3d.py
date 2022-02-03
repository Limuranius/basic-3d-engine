import pygame
import time
from objects import Object3D, Vector3D, Matrix4x4, Camera3D
import models

WIDTH = 1400
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    objects = []

    # obj = models.Cube()
    # obj.set_pos(200, 0, -500)
    # obj.set_rotation_speed(0, 1, 1)
    # objects.append(obj)
    # #
    # obj = models.CutPyramid()
    # obj.set_pos(-200, 0, -500)
    # obj.set_rotation_speed(0, 1, 0)
    # obj.set_scale(50)
    # objects.append(obj)

    obj = models.FileObject("untitled.obj")
    obj.set_pos(0, 0, -300)
    obj.set_scale(20)
    obj.set_rotation_speed(0, 1, 0)
    objects.append(obj)

    camera = Camera3D(Vector3D(0, 0, 0), Vector3D(0, 0, -1), Vector3D(0, 1, 0))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:  # Move forward
            camera.move_by(Vector3D(0, 0, -2))
        if keys_pressed[pygame.K_s]:  # Move backward
            camera.move_by(Vector3D(0, 0, 2))
        if keys_pressed[pygame.K_a]:  # Move left
            camera.move_by(Vector3D(-2, 0, 0))
        if keys_pressed[pygame.K_d]:  # Move right
            camera.move_by(Vector3D(2, 0, 0))

        if keys_pressed[pygame.K_SPACE]:  # Move up
            camera.move_by(Vector3D(0, 2, 0))
        if keys_pressed[pygame.K_LSHIFT]:  # Move down
            camera.move_by(Vector3D(0, -2, 0))

        # WIP
        # if keys_pressed[pygame.K_d]:  # Turn up
        #     camera.turn_up(2)
        # if keys_pressed[pygame.K_d]:  # Turn down
        #     camera.turn_down(2)
        # if keys_pressed[pygame.K_LEFT]:  # Turn left
        #     camera.turn_left(2)
        # if keys_pressed[pygame.K_d]:  # Turn right
        #     camera.turn_right(2)

        """Main Loop"""
        WIN.fill(BLACK)
        for i in range(len(objects)):
            objects[i].draw(WIN, WHITE, camera)
        time.sleep(1 / 60)
        pygame.display.update()

    pygame.quit()


main()
