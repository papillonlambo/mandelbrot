import pygame
import math
from mandelbrot import Mandelbrot

PARAMS_ = {"color": (0,0,0), "size": (600,600), "coords": (-1.5, 2, -1, 2)}

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
            if event.button == 4: 
                p = pygame.mouse.get_pos()
                print(p) 
                
            elif event.button == 5:
                p = pygame.mouse.get_pos()
                print(p)
                
        pygame.display.flip()
