import turtle

def draw_triangle(a_turtle):
    for i in range(1,4):
        a_turtle.forward(150)
        a_turtle.right(120)

def draw_square(a_turtle):
    for i in range(1,5):
        a_turtle.forward(100)
        a_turtle.right(90)

def draw_hexagon(a_turtle):
    for i in range(1,7):
        a_turtle.forward(100)
        a_turtle.right(60)

def draw_art(mode):
    # create a backend window
    window = turtle.Screen()
    window.bgcolor('red')
    jimmy = turtle.Turtle()
    jimmy.shape('turtle')
    jimmy.color('yellow')
    # create the drawing turtle
    if mode == 1:
        for i in range(1,37):
        # everytime draw a square then turn right 30 degree, repeat for 12 times
            draw_triangle(jimmy)
            jimmy.right(10)

    elif mode == 2:
        for i in range(1,37):
            draw_square(jimmy)
            jimmy.right(10)
        jimmy.right(90)
        jimmy.forward(200)

    else:
        for i in range(1,37):
                draw_hexagon(jimmy)
                jimmy.right(10)
    window.exitonclick()



