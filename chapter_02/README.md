# chapter 2

## hello_pygame

Display a font string **"Hello Pygame"**

## draw_circle

Draw a circle and display

```python
position = (
    center_x, # the x of the center of the circle
    center_y  # the y of the center of the circle
)
pygame.draw.circle(
    screen,   # the screen of the game
    color,    # the color of the circle
    position, # the position of the center of the circle
    radius,   # the radius of the circle
    width     # the width of the circle (bold)
)
```

## draw_rectangle

Draw a rectangle and make it move around

## draw_line

Draw a line and display

```python
pygame.draw.line(
    screen,
    color,
    start_point,
    end_point,
    width
)
```

## draw_arcs

Draw a arcs and display

```python
position = (
    screen_x, # the x of the top left corner of the arcs
    screen_y, # the y of the top left corner of the arcs
    width,    # the width of the arcs
    height    # the height of the arcs
)
pygame.draw.arc(
    screen,      # the screen of the game
    color,       # the color of the arcs
    position,    # the position of the arcs
    start_angle, # start angle of the arcs
    end_angle,   # end angle of the arcs
    width        # the width of the arcs (bold)
)
```

## Pie

The game pie