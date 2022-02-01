import unittest
from objects import Vector3D, Matrix4x4


class TestVectors(unittest.TestCase):
    def check_vector_values(self, v, x, y, z, w):
        self.assertAlmostEqual(v.x, x)
        self.assertAlmostEqual(v.y, y)
        self.assertAlmostEqual(v.z, z)
        self.assertAlmostEqual(v.w, w)

    def test_creation(self):
        v1 = Vector3D(1, 2, 3)
        self.check_vector_values(v1, 1, 2, 3, 1)

        v2 = Vector3D(5, 6, 7, 0)
        self.check_vector_values(v2, 5, 6, 7, 0)

    def test_sum(self):
        v1 = Vector3D(3, 5, 8)
        v2 = Vector3D(1, 10, 3, 0)
        v3 = v1 + v2
        self.check_vector_values(v3, 4, 15, 11, 1)

    def test_sub(self):
        v1 = Vector3D(3, 5, 8)
        v2 = Vector3D(1, 10, 3, 0)
        v3 = v1 - v2
        self.check_vector_values(v3, 2, -5, 5, 1)

    def test_mul_by_scalar(self):
        v1 = Vector3D(3, 5, 8)
        v2 = v1.mul_by_scalar(5)
        self.check_vector_values(v2, 15, 25, 40, 1)

        v3 = Vector3D(1, 2, 3, 0)
        v4 = v3.mul_by_scalar(3)
        self.check_vector_values(v4, 3, 6, 9, 0)

    def test_mul_by_matrix(self):
        values = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        matrix = Matrix4x4(values)
        v1 = Vector3D(3, 7, 5)
        v2 = v1.mul_by_matrix(matrix)
        self.check_vector_values(v2, 96, 112, 128, 144)

        v3 = Vector3D(-100, 0, 35)
        v4 = v3.mul_by_matrix(matrix)
        self.check_vector_values(v4, 228, 164, 100, 36)

    def test_length(self):
        v1 = Vector3D(11, 21, 35)
        v2 = Vector3D(0, -1, 10)
        v3 = Vector3D(-2, -2, -4)
        self.assertAlmostEqual(v1.length(), 42.2729227756965)
        self.assertAlmostEqual(v2.length(), 10.04987562112089)
        self.assertAlmostEqual(v3.length(), 4.898979485566356)

    def test_normalize(self):
        v1 = Vector3D(7, 17, 13)
        v2 = v1.normalize()
        self.check_vector_values(v2, 0.3108809141790293, 0.7549965058633569, 0.5773502691896258, 1)

        v3 = Vector3D(-3, -5, 3)
        v4 = v3.normalize()
        self.check_vector_values(v4, -0.457495710997814, -0.7624928516630234, 0.457495710997814, 1)

    def test_cross_product(self):
        v1 = Vector3D(7, 17, 13)
        v2 = Vector3D(-3, -5, 3)
        v3 = Vector3D.cross_product(v1, v2)
        self.check_vector_values(v3, 116, -60, 16, 1)

        v4 = Vector3D(10, 11, 12, 0)
        v5 = Vector3D(3, 55, 29, 0)
        v6 = Vector3D.cross_product(v4, v5)
        self.check_vector_values(v6, -341, -254, 517, 0)

    def test_dot_product(self):
        v1 = Vector3D(7, 17, 13)
        v2 = Vector3D(-3, -5, 3)
        p = Vector3D.dot_product(v1, v2)
        self.assertEqual(p, -67)


class TestMatrices(unittest.TestCase):
    def test_creation_and_indexation(self):
        m = [[6, 8, 7, 3], [7, 1, 14, 9], [1, 2, 17, 7], [18, 15, 15, 4]]
        matrix = Matrix4x4(m)
        for i in range(4):
            for j in range(4):
                self.assertEqual(m[i][j], matrix[i][j])

    def test_mul(self):
        m1 = [[13, 2, 9, 6], [14, 3, 16, 7], [7, 18, 11, 12], [7, 1, 18, 16]]
        m2 = [[18, 12, 11, 4], [14, 10, 19, 6], [13, 8, 12, 8], [15, 12, 3, 13]]
        matrix1 = Matrix4x4(m1)
        matrix2 = Matrix4x4(m2)
        matrix3 = Matrix4x4.multiply(matrix1, matrix2)
        correct_m = [[469, 320, 307, 214], [607, 410, 424, 293], [701, 496, 587, 380], [614, 430, 360, 386]]
        self.assertEqual(matrix3._values, correct_m)


if __name__ == '__main__':
    unittest.main()
