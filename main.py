import pygame
import math
from mandelbrot import Mandelbrot

PARAMS_ = {"color": (0, 0, 0), "size": (600, 600), "coords": (-2, 0.5, -1.25, 1.25)}

# Zoom factor for each click
zoomfactor = 2


# Util functions---------------------------------------------
def interpolate(start, end, interpolation):
    return start + ((end - start) * interpolation)


def complex_transform(grid_position, height, max, min):
    return grid_position / (height / (max - min)) + min


# -----------------------------------------------------------

pygame.display.init()
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
pygame.display.set_caption("Mandelbrot")

window = pygame.display.set_mode(PARAMS_["size"])
size = pygame.display.get_surface().get_size()

mandelbrot = Mandelbrot(window, PARAMS_["color"], PARAMS_["size"], PARAMS_["coords"])
mandelbrot.draw()

pygame.display.flip()

# Events
isloop = True
while isloop:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            isloop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                p = pygame.mouse.get_pos()
                # Transforming pygame coordinates to complex plan values
                mouseRealPart = complex_transform(p[0], mandelbrot.width, mandelbrot.xmax, mandelbrot.xmin)
                mouseImaginaryPart = complex_transform(p[1], mandelbrot.width, mandelbrot.ymax, mandelbrot.xmin)
                # Calculating the interpolation/zoom value
                interpolation = 1.0 / zoomfactor
                # Redefining the values of the initial box drawing Moving the square of calculation around the mouse
                # click coordinates with the interpolate method and "zooming"
                mandelbrot.xmin = interpolate(mouseRealPart, mandelbrot.xmin, interpolation)
                mandelbrot.ymin = interpolate(mouseImaginaryPart, mandelbrot.ymin, interpolation)
                mandelbrot.xmax = interpolate(mouseRealPart, mandelbrot.xmax, interpolation)
                mandelbrot.ymax = interpolate(mouseImaginaryPart, mandelbrot.ymax, interpolation)
                # Recalling the draw function
                mandelbrot.draw()
            elif event.button == 2:
                p = pygame.mouse.get_pos()
                print(p)
                #TODO Add a "unzoom function" for instance save x and y s in a list and recusively redraw previous zooms.

        pygame.display.flip()
