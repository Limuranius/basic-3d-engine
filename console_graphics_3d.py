from objects import Vector3D, Matrix4x4, Camera3D
import models
import os
from console_drawer import ConsoleDrawer


def main():
    obj = models.FileObject("untitled.obj")
    obj.set_pos(0, 0, -300)
    obj.set_scale(20)
    obj.set_rotation_speed(0, 0.3, 0)

    camera = Camera3D(Vector3D(0, 0, 0), Vector3D(0, 0, -1), Vector3D(0, 1, 0))
    camera.set_fov(45)

    console_drawer = ConsoleDrawer()
    console_size = tuple(os.get_terminal_size())
    console_drawer.set_size(console_size[0], console_size[1])
    console_drawer.clear()
    camera.set_aspect_ratio(console_size[0] / console_size[1])

    old_size = console_size
    run = True
    while run:
        # Resizing image if needed
        curr_size = tuple(os.get_terminal_size())
        if curr_size != old_size:
            console_drawer.set_size(curr_size[0], curr_size[1])
            camera.set_aspect_ratio(curr_size[0] / curr_size[1])

        # Drawing objects
        console_drawer.clear()

        obj.draw_console(console_drawer, camera)

        console_drawer.print_surface()


main()
