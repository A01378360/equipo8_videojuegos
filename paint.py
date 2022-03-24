"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    '''El circulo es una figura en la que tiene muchas lineas, por lo que se puso un for que
     tuviera un rango de 37 linea, la linea iria derecho luego se moviera a la derecha y repetiria ese movimentio 37 veces'''
    "Aarón García Guerrero"

    
    up()
    goto(start.x, start.y)
    down()
    for count in range(37): 
        forward(end.x - start.x)
        right(10)


def rectangle(start, end):
    """Draw rectangle from start to end."""

    '''Para la def de rectangulo es igual que el cuadrado, la unica diferencia es
        que una de las lineas deberia ser más larga, en este caso es la base que
        sera más larga. Se hicieron dos "for", un for de rango 2 que seran las lineas de la base
        y un for que haga las lineas laterales'''
    "Aarón García Guerrero"

    up()
    goto(start.x, start.y)
    down()
    for count in range(2):
        forward(end.x - start.x)
        right(90)
        for count in range(1):
            forward(40)
            right(90)


def triangle(start, end):
    """Draw triangle from start to end."""
    '''En esta función se dibuja un triángulo isósceles, se usa un "for" de rango 3 para dibujar
        las tres líneas del triángulo con sus respectivas medidas'''
    "Brenda Vega Méndez"
    
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(100)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P') '''Se agrega un color como los anteriores, se define el nombre del color y la letra con la que será identificado y seleccionado''' "Brenda Vega Méndez"
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
