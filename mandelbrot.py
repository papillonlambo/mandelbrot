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

                cx = self.complex_transform(x, self.width, self.xmax, self.xmin)
                cy = self.complex_transform(y, self.width, self.ymax, self.ymin)
                c = complex(cx, cy)
                z = 0
                
                while abs(z) < 2 and i < self.max_iteration:
                    z = z**2 + c
                    i+=1

                if i == self.max_iteration:
                    self.window.set_at((x, y), self.color)
                else:
                    self.window.set_at((x, y), (
                        i * self.backgroundColor[0] / self.max_iteration, i * self.backgroundColor[1] / self.max_iteration, i * self.backgroundColor[2] / self.max_iteration)
                    )

        print(f"Mandelbrot fractal successfully generated in {round(time.time() - time_, 2)}s")

    
    # --------------------------------------------------------------

    def zoom(self, pos, zoomtype):

        # Transforming pygame coordinates to complex plan values
        mouseRealPart = self.complex_transform(pos[0], self.width, self.xmax, self.xmin)
        mouseImaginaryPart = self.complex_transform(pos[1], self.height, self.ymax, self.ymin)
        
        # Calculating the interpolation/zoom value
        if zoomtype == 1:
            interpolation = 1.0 / self.zoomfactor
        else:
            interpolation = 1.0 * self.zoomfactor

        # Redefining the values of the initial box drawing Moving the square of calculation around the mouse
        # click coordinates with the interpolate method and "zooming"
        self.xmin = self.interpolate(mouseRealPart, self.xmin, interpolation)
        self.ymin = self.interpolate(mouseImaginaryPart, self.ymin, interpolation)
        self.xmax = self.interpolate(mouseRealPart, self.xmax, interpolation)
        self.ymax = self.interpolate(mouseImaginaryPart, self.ymax, interpolation)

        self.draw()


    # ---------- Util functions -----------------------------------

    def complex_transform(self, grid_position, size, max, min):
        return grid_position / (size / (max - min)) + min

    def interpolate(self, start, end, interpolation):
        return start + ((end - start) * interpolation)

    # --------------------------------------------------------------