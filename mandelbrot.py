import pygame
from math import *
from cmath import *
import time

class Mandelbrot:

    def __init__(self, window, color, size, coords):
        self.window = window
        self.width, self.height = size
        self.xmin, self.xmax, self.ymin, self.ymax = coords
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
                z = 0
                i = 0
                n+=1
                
                if n % ((self.width*self.height)//100) == 0:
                    progression += 1
                    print(f"Loading... {progression}%")
                
                cx = self.xmin + self.xmax * x / self.width
                cy = self.ymin + self.ymax * y / self.height
                c = complex(cx,cy)

                while abs(z) < 2 and i < self.max_iteration:
                    z = z**2 + c
                    i+=1

                if i == self.max_iteration:
                    self.window.set_at((x,y), self.color)
                else:
                    self.window.set_at((x,y), (i*255/self.max_iteration, i*255/self.max_iteration, i*255/self.max_iteration))
                    
        
        print(f"Mandelbrot fractal successfully generated in {round(time.time() - time_, 2)}s")
