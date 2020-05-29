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
- [Theory](#theory)

---------------------------------------------------

<div id="params">

### Params
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

---------------------------------------------------

<div id="theory">

### Theory

#### What's Mandelbrot fractal
It's a fractal defined as the set of points of the complex plane for which this sequence is bounded in module, otherwise called 'Mandelbrot Set'.

![formula](/assets/formula.png)

![formula2](/assets/formula2.png)

#### Complex numbers's definition
Complex numbers is real numbers extension but that introduces imaginary number.
![formula3](/assets/formula3.png)

It's a number spelled a+ib.

<img src="/assets/complex_numbers.png" alt="complex_numbers" width="200" />

a is Real part. (abscissa)

b is Imaginary part. (ordinate)

**Vocabulary**

Affix: Complex number that defines point in the complex plane.
Modulus: Distance between origin and complex point. 

![formula4](/assets/formula4.png)


#### Calculation to draw fractal
We set maximum number of iterations (MAX_ITERATION) (Example: 50)
Then , for all cordinated point (x,y) of complex plane.
We define  cordinated point affix noted c. Next we calculate sequence terms with formula:

![formula4](/assets/formula5.png)

While modulus of complex number is less than 2 and iteration (noted 'i') is less than MAX_ITERATION.

If after loop while, 'i' is equal to MAX_ITERATION then the sequence converges so the coordonates is in set Mandelbrot and we can add black pixel. Else we add color pixel (we can vary color degrees using 'i' which different for each release of loop while)

</div>
