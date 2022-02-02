from objects import Vector3D, Object3D, Polygon


class Cube(Object3D):
    def __init__(self):
        polygons = [
            Polygon([Vector3D(-1, -1, -1), Vector3D(-1, -1, 1), Vector3D(-1, 1, -1)]),
            Polygon([Vector3D(-1, 1, 1), Vector3D(-1, 1, -1), Vector3D(-1, -1, 1)]),
            Polygon([Vector3D(-1, -1, -1), Vector3D(-1, 1, -1), Vector3D(1, -1, -1)]),
            Polygon([Vector3D(1, 1, -1), Vector3D(1, -1, -1), Vector3D(-1, 1, -1)]),
            Polygon([Vector3D(1, 1, -1), Vector3D(1, -1, 1), Vector3D(1, -1, -1)]),
            Polygon([Vector3D(1, -1, 1), Vector3D(1, 1, -1), Vector3D(1, 1, 1)]),
            Polygon([Vector3D(-1, -1, 1), Vector3D(1, -1, 1), Vector3D(1, 1, 1)]),
            Polygon([Vector3D(1, 1, 1), Vector3D(-1, 1, 1), Vector3D(-1, -1, 1)]),
            Polygon([Vector3D(1, -1, 1), Vector3D(-1, -1, 1), Vector3D(-1, -1, -1)]),
            Polygon([Vector3D(-1, -1, -1), Vector3D(1, -1, -1), Vector3D(1, -1, 1)]),
            Polygon([Vector3D(-1, 1, -1), Vector3D(-1, 1, 1), Vector3D(1, 1, -1)]),
            Polygon([Vector3D(1, 1, 1), Vector3D(1, 1, -1), Vector3D(-1, 1, 1)]),
        ]
        super().__init__(polygons)


class CutPyramid(Object3D):
    def __init__(self):
        polygons = [
            Polygon([Vector3D(-1, -1, -1), Vector3D(-1, -1, 1), Vector3D(-0.5, 1, -0.5)]),
            Polygon([Vector3D(-0.5, 1, 0.5), Vector3D(-0.5, 1, -0.5), Vector3D(-1, -1, 1)]),
            Polygon([Vector3D(-1, -1, -1), Vector3D(-0.5, 1, -0.5), Vector3D(1, -1, -1)]),
            Polygon([Vector3D(0.5, 1, -0.5), Vector3D(1, -1, -1), Vector3D(-0.5, 1, -0.5)]),
            Polygon([Vector3D(0.5, 1, -0.5), Vector3D(1, -1, 1), Vector3D(1, -1, -1)]),
            Polygon([Vector3D(1, -1, 1), Vector3D(0.5, 1, -0.5), Vector3D(0.5, 1, 0.5)]),
            Polygon([Vector3D(-1, -1, 1), Vector3D(1, -1, 1), Vector3D(0.5, 1, 0.5)]),
            Polygon([Vector3D(0.5, 1, 0.5), Vector3D(-0.5, 1, 0.5), Vector3D(-1, -1, 1)]),
            Polygon([Vector3D(1, -1, 1), Vector3D(-1, -1, 1), Vector3D(-1, -1, -1)]),
            Polygon([Vector3D(-1, -1, -1), Vector3D(1, -1, -1), Vector3D(1, -1, 1)]),
            Polygon([Vector3D(-0.5, 1, -0.5), Vector3D(-0.5, 1, 0.5), Vector3D(0.5, 1, -0.5)]),
            Polygon([Vector3D(0.5, 1, 0.5), Vector3D(0.5, 1, -0.5), Vector3D(-0.5, 1, 0.5)]),
        ]
        super().__init__(polygons)
