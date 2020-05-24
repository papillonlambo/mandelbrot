# mandelbrot

Mandelbrot fractal's visualizer with pygame library. 

![example1](/assets/example1.png)

## Params
In main.py you can change parameters for instance "color" (in RGB) for fractal color, "size" for window size.
```
PARAMS_ = {
    "color": [FRACTAL_COLOR], 
    "backgroundColor": [BACKGROUND_COLOR], 
    "size": [WINDOW_SIZE], 
    "coords": [FRACTAL_COORDONATES], 
    "zoomfactor": [ZOOM]
}
```

### Example
```py
PARAMS_ = {
    "color": (0, 0, 0), 
    "backgroundColor": (0, 0, 255), 
    "size": (600, 600), 
    "coords": (-2, 0.5, -1.25, 1.25), 
    "zoomfactor": 2
}
```

![example2](/assets/example2.png)

### Zoom
You can zoom with left click mouse and dezoom with right click mouse.
![example3](/assets/example3.png)