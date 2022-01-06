import pygame
from mb import Mandelbrot

PARAMS_ = {
    "color": (0, 0, 0), 
    "backgroundColor": (0, 0, 255), 
    "size": (600, 600), 
    "coords": (-2, 0.5, -1.25, 1.25), 
    "zoomfactor": 2
}

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

            if event.button in [1, 3]:
                mandelbrot.zoom(pygame.mouse.get_pos(), event.button)

        pygame.display.flip()