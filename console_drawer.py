import os


class ConsoleDrawer:
    def __init__(self):
        self.surface: list[list[str]] = []
        self.width: int = 0
        self.height: int = 0

    def clear(self):
        for i in range(self.height):
            for j in range(self.width):
                self.surface[i][j] = " "

    def set_size(self, width: int, height: int):
        self.width = width
        self.height = height
        self.surface = [[" " for _ in range(self.width)] for __ in range(self.height)]

    def draw_line(self, p1: tuple[float, float], p2: tuple[float, float], color: str = "@"):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        steps = abs(int(dx + dy)) + 1
        x_inc = dx / steps
        y_inc = dy / steps
        for i in range(steps):
            x_index = round(p1[0] + i * x_inc)
            y_index = round(p1[1] + i * y_inc)
            if 0 <= x_index < self.width and 0 <= y_index < self.height:
                self.surface[y_index][x_index] = color

    def fill_triangle(self, p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float], color: str):
        # Dividing triangle into two parts
        vertices = sorted([p1, p2, p3], key=lambda v: v[1])
        low = vertices[0]
        mid_1 = vertices[1]
        high = vertices[2]

        dx_l_h = high[0] - low[0]
        dy_l_h = high[1] - low[1]
        if dy_l_h == 0:
            dy_l_h = 1
        r_l_h = dx_l_h / dy_l_h

        dy_l_m2 = mid_1[1] - low[1]
        mid_2 = (low[0] + r_l_h * dy_l_m2, mid_1[1])

        # Drawing lower triangle
        dx_l_m1 = mid_1[0] - low[0]
        dy_l_m1 = mid_1[1] - low[1]
        if dy_l_m1 == 0:
            dy_l_m1 = 1
        r_l_m1 = dx_l_m1 / dy_l_m1
        for dy in range(0, int(dy_l_m2 + 1)):
            y = low[1] + dy
            x1 = low[0] + r_l_m1 * dy
            x2 = low[0] + r_l_h * dy
            self.draw_line((x1, y), (x2, y), color)

        # Drawing upper triangle
        dx_m1_h = high[0] - mid_1[0]
        dy_m1_h = high[1] - mid_1[1]
        if dy_m1_h == 0:
            dy_m1_h = 1
        r_m1_h = dx_m1_h / dy_m1_h
        for dy in range(0, int(dy_m1_h + 1)):
            y = mid_1[1] + dy
            x1 = mid_1[0] + r_m1_h * dy
            x2 = mid_2[0] + r_l_h * dy
            self.draw_line((x1, y), (x2, y), color)

    def print_surface(self):
        print("".join(["".join(self.surface[i]) for i in range(len(self.surface))]), end="")

    @staticmethod
    def get_char_by_brightness(brightness: float) -> str:
        """
        Returns ASCII character according to brigtness level
        :param brightness: Real number in range [0; 1]
        :return: character
        """
        chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`\'."
        return chars[-int(len(chars) * brightness)]
