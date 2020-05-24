import pygame
from math import *
from cmath import *
import time


class Mandelbrot:

    def __init__(self, window, color, backgroundColor, size, coords, zoomfactor):
        self.window = window
        self.width, self.height = size
        self.xmin, self.xmax, self.ymin, self.ymax = coords
        self.zoomfactor = zoomfactor
        self.backgroundColor = backgroundColor
        # --------------------
        self.color = color
        self.max_iteration = 50

    # --------------------------------------------------------------

    def draw(self):
        n = 0
        progression = 0
        time_ = time.time()

        for x in range(self.width):
            for y in range(self.height):
                i = 0
                n += 1

                if n % ((self.width * self.height) // 100) == 0:
                    progression += 1
                    print(f"Loading... {progression}%")

                # Transforming the size of the box to fit the complex plane
                cx = x * (self.xmax - self.xmin) / self.width + self.xmin
                cy = y * (self.ymax - self.ymin) / self.width + self.ymin
                xn = 0
                yn = 0

                while (xn**2 + yn**2) < 4 and i < self.max_iteration:
                    tmp_x = xn
                    tmp_y = yn
                    xn = tmp_x**2 - tmp_y**2 + cx
                    yn = 2 * tmp_x * tmp_y + cy
                    i += 1

                if i == self.max_iteration:
                    self.window.set_at((x, y), self.color)
                else:
                    self.window.set_at((x, y), (
                        i * self.backgroundColor[0] / self.max_iteration, i * self.backgroundColor[1] / self.max_iteration, i * self.backgroundColor[2] / self.max_iteration)
                    )

        print(f"Mandelbrot fractal successfully generated in {round(time.time() - time_, 2)}s")


    # ---------- Util functions -----------------------------------

    def complex_transform(self, grid_position, size, max, min):
        return grid_position / (size / (max - min)) + min

    def interpolate(self, start, end, interpolation):
        return start + ((end - start) * interpolation)

    # --------------------------------------------------------------