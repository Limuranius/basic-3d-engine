from objects import Vector3D, Object3D


def create_cube(pos: tuple, speed: tuple, rotation: tuple, rotation_speed: tuple):
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
    obj = Object3D(object_vertices, object_edges, pos)
    obj.set_speed(speed[0], speed[1], speed[2])
    obj.set_rotation(rotation[0], rotation[1], rotation[2])
    obj.set_rotation_speed(rotation_speed[0], rotation_speed[1], rotation_speed[2])
    return obj


def create_cut_pyramid(pos: tuple, speed: tuple, rotation: tuple, rotation_speed: tuple):
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
    obj = Object3D(object_vertices, object_edges, pos)
    obj.set_speed(speed[0], speed[1], speed[2])
    obj.set_rotation(rotation[0], rotation[1], rotation[2])
    obj.set_rotation_speed(rotation_speed[0], rotation_speed[1], rotation_speed[2])
    return obj
