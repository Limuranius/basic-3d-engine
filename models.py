from objects import Vector3D, Object3D, Polygon


class FileObject(Object3D):
    def __init__(self, file_path: str):
        file = open(file_path, "r").read().split("\n")
        vertices = []
        indices = []
        for line in file:
            if line[0] == "v":
                line = line.split()[1:]
                line = [float(i) for i in line]
                vertices.append(Vector3D(line[0], line[1], line[2]))
            elif line[0] == "f":
                line = line.split()[1:]
                line = [int(i) - 1 for i in line]
                indices.append(line)

        polygons = []
        for i in indices:
            polygons.append(Polygon([vertices[i[0]], vertices[i[1]], vertices[i[2]]]))

        super().__init__(polygons)




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
