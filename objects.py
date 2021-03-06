from __future__ import annotations  # For cases when we need to specify parameter's ClassType inside ClassType's method
from typing import Union
from math_objects import Matrix4x4, Vector3D
from console_drawer import ConsoleDrawer
import pygame
import copy


class Polygon:
    def __init__(self, points: list[Vector3D]):
        self.points = points

    def get_normal(self) -> Vector3D:
        t1 = self.points[0] - self.points[1]
        t2 = self.points[1] - self.points[2]
        normal = Vector3D.cross_product(t1, t2).normalize()
        return normal

    def apply_matrix(self, matrix: Matrix4x4):
        for i in range(3):
            self.points[i] = self.points[i].mul_by_matrix(matrix)

    def is_visible(self, camera: Camera3D) -> bool:
        camera_direction_vector = (self.points[0] - camera.get_pos()).normalize()  # Vector from camera to point
        d_prod = Vector3D.dot_product(self.get_normal(), camera_direction_vector)
        if d_prod < 0:  # angle between camera and normal < 90
            return True
        else:
            return False

    def get_white_hue_for_light(self, light_source: Vector3D) -> tuple[int, int, int]:
        norm = self.get_normal()
        dp = Vector3D.dot_product(norm, light_source)
        cos_angle = abs(dp / (light_source.length() * norm.length()))
        c = int(cos_angle * 255)
        color = (c, c, c)
        return color

    def get_mean_z(self):
        s = self.points[0].z + self.points[1].z + self.points[2].z
        return s / 3

    def draw(self, surface: pygame.Surface, color: tuple[int, int, int]):
        p1 = self.points[0]
        p2 = self.points[1]
        p3 = self.points[2]

        width = surface.get_width() / 2
        height = surface.get_height() / 2

        p1.x = p1.x / p1.w * width
        p2.x = p2.x / p2.w * width
        p3.x = p3.x / p3.w * width

        p1.y = p1.y / p1.w * width
        p2.y = p2.y / p2.w * width
        p3.y = p3.y / p3.w * width

        color = self.get_white_hue_for_light(Vector3D(0, 0, -1))

        pygame.draw.polygon(surface, color,
                            [Object3D.center_coords(surface, p1.x, p1.y),
                             Object3D.center_coords(surface, p2.x, p2.y),
                             Object3D.center_coords(surface, p3.x, p3.y)])

    def draw_console(self, console_drawer: ConsoleDrawer):
        p1 = self.points[0]
        p2 = self.points[1]
        p3 = self.points[2]

        width = console_drawer.width / 2
        height = console_drawer.height / 2

        p1.x = p1.x / p1.w * width + width
        p2.x = p2.x / p2.w * width + width
        p3.x = p3.x / p3.w * width + width

        p1.y = p1.y / p1.w * height + height
        p2.y = p2.y / p2.w * height + height
        p3.y = p3.y / p3.w * height + height

        color = ConsoleDrawer.get_char_by_brightness(self.get_white_hue_for_light(Vector3D(0, 0, -1))[0] / 255)

        console_drawer.fill_triangle((p1.x, p1.y),
                                     (p2.x, p2.y),
                                     (p3.x, p3.y), color)


class Object3D:
    def __init__(self, polygons: list[Polygon]):
        self.polygons = polygons

        self.x = 0
        self.y = 0
        self.z = 0
        self.vx = 0
        self.vy = 0
        self.vz = 0

        self.x_rot = 0
        self.y_rot = 0
        self.z_rot = 0
        self.vx_rot = 0
        self.vy_rot = 0
        self.vz_rot = 0

        self.scale = 100

    def set_pos(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set_speed(self, vx, vy, vz):
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def set_rotation(self, x_rot, y_rot, z_rot):
        self.x_rot = x_rot
        self.y_rot = y_rot
        self.z_rot = z_rot

    def set_rotation_speed(self, vx_rot, vy_rot, vz_rot):
        self.vx_rot = vx_rot
        self.vy_rot = vy_rot
        self.vz_rot = vz_rot

    def set_scale(self, scale):
        self.scale = scale

    def update_rotation(self):
        self.x_rot += self.vx_rot
        self.y_rot += self.vy_rot
        self.z_rot += self.vz_rot

    def update_movement(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def update(self):
        self.update_rotation()
        self.update_movement()

    def get_transform_matrix(self, camera: Camera3D) -> Matrix4x4:
        transform_matrix = Matrix4x4.get_scale(self.scale, self.scale, self.scale)
        transform_matrix = Matrix4x4.multiply(transform_matrix, Matrix4x4.get_rotate_x(self.x_rot))
        transform_matrix = Matrix4x4.multiply(transform_matrix, Matrix4x4.get_rotate_y(self.y_rot))
        transform_matrix = Matrix4x4.multiply(transform_matrix, Matrix4x4.get_rotate_z(self.z_rot))
        transform_matrix = Matrix4x4.multiply(transform_matrix, Matrix4x4.get_translation(self.x, self.y, self.z))
        transform_matrix = Matrix4x4.multiply(transform_matrix, camera.get_camera_matrix())
        return transform_matrix

    def draw(self, surface: pygame.Surface, color: tuple[int, int, int], camera: Camera3D):
        """
        Draw object on surface <surface> with color <color> according to position and angle of camera <camera>
        :param surface: pygame surface that we draw on
        :param color: RGB color of object
        :param camera: camera object in 3D space
        """
        transform_matrix = self.get_transform_matrix(camera)
        obj_polygons = copy.deepcopy(self.polygons)  # Creating a copy of list of polygons

        for i in range(len(obj_polygons)):  # Applying matrix to every polygon
            obj_polygons[i].apply_matrix(transform_matrix)

        obj_polygons = sorted(obj_polygons, key=lambda x: x.get_mean_z(), reverse=True)  # Sorting by z-coordinate
        for polygon in obj_polygons:  # Drawing polygons
            if polygon.is_visible(camera):
                polygon.draw(surface, color)
        self.update()

    def draw_console(self, console_drawer: ConsoleDrawer, camera: Camera3D):
        transform_matrix = self.get_transform_matrix(camera)
        obj_polygons = copy.deepcopy(self.polygons)  # Creating a copy of list of polygons

        for i in range(len(obj_polygons)):  # Applying matrix to every polygon
            obj_polygons[i].apply_matrix(transform_matrix)

        obj_polygons = sorted(obj_polygons, key=lambda x: x.get_mean_z(), reverse=True)  # Sorting by z-coordinate
        for polygon in obj_polygons:  # Drawing polygons
            if polygon.is_visible(camera):
                polygon.draw_console(console_drawer)
        self.update()

    @staticmethod
    def center_coords(surface, x, y):
        return x + surface.get_width() / 2, y + surface.get_height() / 2


class Camera3D:
    def __init__(self, pos: Vector3D, target: Vector3D, up: Vector3D):
        self.pos = pos
        self.target = target
        self.up = up

        self.fov = 90
        self.aspect_ratio = 1
        self.near = -1
        self.far = -1000

        self.camera_matrix = Matrix4x4()
        self.update_camera_matrix()

    def update_camera_matrix(self):
        view_matrix = Matrix4x4.get_look_at(self.pos, self.target, self.up)
        projection_matrix = Matrix4x4.get_perspective_projection(self.fov, self.aspect_ratio, self.near, self.far)
        self.camera_matrix = Matrix4x4.multiply(view_matrix, projection_matrix)

    def get_camera_matrix(self):
        return self.camera_matrix

    def move_to(self, pos: Vector3D):
        direction_vector = self.get_direction_vector()
        self.pos = pos
        self.target = self.pos + direction_vector
        self.update_camera_matrix()

    def move_by(self, d_pos: Vector3D):
        self.pos += d_pos
        self.target += d_pos
        self.update_camera_matrix()

    # WIP
    # def turn_left(self, scale: Union[int, float]):
    #     cross_prod = Vector3D.cross_product(self.get_direction_vector(), self.up).normalize()
    #     new_direction_vector = cross_prod.mul_by_scalar(scale)
    #     self.target = self.pos + new_direction_vector
    #     self.update_camera_matrix()

    def get_pos(self) -> Vector3D:
        return self.pos

    def get_direction_vector(self):
        return (self.target - self.pos).normalize()

    def set_up(self, up: Vector3D):
        self.up = up
        self.update_camera_matrix()

    def set_fov(self, fov: float):
        self.fov = fov
        self.update_camera_matrix()

    def set_aspect_ratio(self, aspect_ratio: float):
        self.aspect_ratio = aspect_ratio
        self.update_camera_matrix()


def main():
    v1 = Vector3D(1, 0, 0)
    v2 = Vector3D(0, 1, 0)
    print(Vector3D.cross_product(v2, v1).to_string())


if __name__ == "__main__":
    main()
