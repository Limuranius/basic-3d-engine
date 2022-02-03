from __future__ import annotations  # For cases when we need to specify parameter's ClassType inside ClassType's method
from typing import Union
from math import sqrt, sin, cos, tan, pi


def deg_to_rad(degrees: Union[int, float]):
    return degrees / 180 * pi


class Vector3D:
    def __init__(self, x: Union[int, float], y: Union[int, float], z: Union[int, float], w: Union[int, float] = 1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w  # 1 - point, 0 - vector

    def __add__(self, other: Vector3D) -> Vector3D:
        return Vector3D(self.x + other.x,
                        self.y + other.y,
                        self.z + other.z,
                        self.w)

    def __sub__(self, other: Vector3D) -> Vector3D:
        return Vector3D(self.x - other.x,
                        self.y - other.y,
                        self.z - other.z,
                        self.w)

    def mul_by_scalar(self, n: Union[int, float]) -> Vector3D:
        return Vector3D(self.x * n,
                        self.y * n,
                        self.z * n,
                        self.w)

    def mul_by_matrix(self, m: Matrix4x4) -> Vector3D:
        new_x = self.x * m[0][0] + self.y * m[1][0] + self.z * m[2][0] + self.w * m[3][0]
        new_y = self.x * m[0][1] + self.y * m[1][1] + self.z * m[2][1] + self.w * m[3][1]
        new_z = self.x * m[0][2] + self.y * m[1][2] + self.z * m[2][2] + self.w * m[3][2]
        new_w = self.x * m[0][3] + self.y * m[1][3] + self.z * m[2][3] + self.w * m[3][3]
        return Vector3D(new_x, new_y, new_z, new_w)

    def length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self) -> Vector3D:
        l = self.length()
        return Vector3D(self.x / l,
                        self.y / l,
                        self.z / l,
                        self.w)

    @staticmethod
    def cross_product(a: Vector3D, b: Vector3D) -> Vector3D:
        return Vector3D(a.y * b.z - a.z * b.y,
                        a.z * b.x - a.x * b.z,
                        a.x * b.y - a.y * b.x,
                        a.w)

    @staticmethod
    def dot_product(a: Vector3D, b: Vector3D) -> float:
        return a.x * b.x + a.y * b.y + a.z * b.z

    def to_string(self) -> str:
        return f'{self.x}, {self.y}, {self.z}'


class Matrix4x4:
    def __init__(self, values: list[list[Union[int, float]]] = None):
        if values is None:
            self._values = [[0 for _ in range(4)] for __ in range(4)]
        else:
            self._values = values

    def __getitem__(self, index: int) -> list[float]:
        return self._values[index]

    @staticmethod
    def multiply(a: Matrix4x4, b: Matrix4x4) -> Matrix4x4:
        res_matrix = Matrix4x4()
        for i in range(4):
            for j in range(4):
                s = 0
                for k in range(4):
                    s += a[i][k] * b[k][j]
                res_matrix[i][j] = s
        return res_matrix

    def print(self) -> None:
        for line in self._values:
            print(line)
        print()

    @staticmethod
    def get_identity_matrix():
        return Matrix4x4([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def get_rotate_x(angle: Union[int, float]) -> Matrix4x4:
        """
        Get matrix of rotation around x-axis by <angle> degrees
        :param angle: Angle of rotation in degrees
        :return: X-axis rotation matrix
        """
        angle = deg_to_rad(angle)
        return Matrix4x4([
            [1, 0, 0, 0],
            [0, cos(angle), sin(angle), 0],
            [0, -sin(angle), cos(angle), 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def get_rotate_y(angle: Union[int, float]) -> Matrix4x4:
        """
        Get matrix of rotation around y-axis by <angle> degrees
        :param angle: Angle of rotation in degrees
        :return: Y-axis rotation matrix
        """
        angle = deg_to_rad(angle)
        return Matrix4x4([
            [cos(angle), 0, -sin(angle), 0],
            [0, 1, 0, 0],
            [sin(angle), 0, cos(angle), 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def get_rotate_z(angle: Union[int, float]) -> Matrix4x4:
        """
        Get matrix of rotation around z-axis by <angle> degrees
        :param angle: Angle of rotation in degrees
        :return: Z-axis rotation matrix
        """
        angle = deg_to_rad(angle)
        return Matrix4x4([
            [cos(angle), sin(angle), 0, 0],
            [-sin(angle), cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def get_translation(dx: Union[int, float], dy: Union[int, float], dz: Union[int, float]) -> Matrix4x4:
        """
        Get translation matrix that moves point by vector (dx, dy, dz)
        :param dx: Shift along x-axis
        :param dy: Shift along y-axis
        :param dz: Shift along z-axis
        :return: Translation matrix
        """
        return Matrix4x4([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [dx, dy, dz, 1]
        ])

    @staticmethod
    def get_scale(sx: Union[int, float], sy: Union[int, float], sz: Union[int, float]) -> Matrix4x4:
        """
        Get scaling matrix that changes size of an object based on <sx>, <sy>, <sz> values
        :param sx: Size modifier along x-axis
        :param sy: Size modifier along y-axis
        :param sz: Size modifier along z-axis
        :return: Scaling matrix
        """
        return Matrix4x4([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def get_look_at(eye: Vector3D, target: Vector3D, up: Vector3D) -> Matrix4x4:
        """
        Get view matrix that changes objects' position according to the position of camera <eye>, the point <target>
        camera is looking at, and vector <up> which represents camera's "up" direction.
        :param eye: Camera's position
        :param target: Point, where camera is looking
        :param up: Camera's "up" direction
        :return: View matrix
        """
        vz = (target - eye).normalize()  # Vector "forward"
        vx = Vector3D.cross_product(up, vz).normalize()  # Vector "right"
        vy = Vector3D.cross_product(vz, vx).normalize()  # Vector "up"
        return Matrix4x4.multiply(
            Matrix4x4.get_translation(-eye.x, -eye.y, -eye.z),
            Matrix4x4([
                [vx.x, vy.x, vz.x, 0],
                [vx.y, vy.y, vz.y, 0],
                [vx.z, vy.z, vz.z, 0],
                [0, 0, 0, 1]
            ])
        )

    @staticmethod
    def get_perspective_projection(fov: Union[int, float], aspect: Union[int, float],
                                   n: Union[int, float], f: Union[int, float]) -> Matrix4x4:
        """
        :param fov: Field of view in degrees
        :param aspect: width/height of canvas
        :param n: Near
        :param f: Far
        :return: Perspective projection matrix
        """
        radians = deg_to_rad(fov)
        sx = (1 / tan(radians / 2)) / aspect
        sy = (1 / tan(radians / 2))
        sz = (f + n) / (f - n)
        dz = (-2 * f * n) / (f - n)

        return Matrix4x4([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, -1],
            [0, 0, dz, 0],
        ])
