# mandelbrot

Mandelbrot fractal's visualizer with pygame library. 

**Pre-requesite:**
- python (> 3)
- pygame

```
python main.py
```

---------------------------------------------------

## Summary
- [Params](#params)
- [Example](#example)
- [Zoom](#zoom)

---------------------------------------------------

<div id="params">

### Params
In main.py you can change parameters for instance "color" (in RGB) for fractal color, "size" for window size.
```
PARAMS_ = {
    "color": [FRACTAL_COLOR], 
    "backgroundColor": [BACKGROUND_COLOR], 
    "size": [WINDOW_SIZE], 
    "coords": [COORDINATES_COMPLEX_PLANE], 
    "zoomfactor": [ZOOM]
}
```
</div>

---------------------------------------------------


<div id="example">

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
</div>

![example2](/assets/example2.png)

---------------------------------------------------

<div id="zoom">

### Zoom
You can zoom with left click mouse and dezoom with right click mouse.
![example3](/assets/example3.png)
![example4](/assets/example4.png)
</div>