import pygame
import math
from mandelbrot import Mandelbrot

PARAMS_ = {"color": (0, 0, 0), "backgroundColor": (0, 0, 255), "size": (600, 600), "coords": (-2, 0.5, -1.25, 1.25), "zoomfactor":2}

# -----------------------------------------------------------

pygame.display.init()
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
pygame.display.set_caption("Mandelbrot")

window = pygame.display.set_mode(PARAMS_["size"])
size = pygame.display.get_surface().get_size()

mandelbrot = Mandelbrot(window, PARAMS_["color"], PARAMS_["backgroundColor"], PARAMS_["size"], PARAMS_["coords"], PARAMS_["zoomfactor"])
mandelbrot.draw()

pygame.display.flip()

# -----------------------------------------------------------

isloop = True
while isloop:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            isloop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                # -----------------------
                p = pygame.mouse.get_pos()
                # Transforming pygame coordinates to complex plan values
                mouseRealPart = mandelbrot.complex_transform(p[0], mandelbrot.width, mandelbrot.xmax, mandelbrot.xmin)
                mouseImaginaryPart = mandelbrot.complex_transform(p[1], mandelbrot.height, mandelbrot.ymax, mandelbrot.ymin)
                # Calculating the interpolation/zoom value
                interpolation = 1.0 / mandelbrot.zoomfactor
                # Redefining the values of the initial box drawing Moving the square of calculation around the mouse
                # click coordinates with the interpolate method and "zooming"
                mandelbrot.xmin = mandelbrot.interpolate(mouseRealPart, mandelbrot.xmin, interpolation)
                mandelbrot.ymin = mandelbrot.interpolate(mouseImaginaryPart, mandelbrot.ymin, interpolation)
                mandelbrot.xmax = mandelbrot.interpolate(mouseRealPart, mandelbrot.xmax, interpolation)
                mandelbrot.ymax = mandelbrot.interpolate(mouseImaginaryPart, mandelbrot.ymax, interpolation)
                # -----------------------

                mandelbrot.draw()

            elif event.button == 2:
                p = pygame.mouse.get_pos()
            

        pygame.display.flip()