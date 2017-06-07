import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor('blue')

    sb = turtle.Turtle()
    sb.shape("turtle")
    sb.color("white")
    i = 1
    while i <= 4:
        sb.forward(250)
        sb.right(90)
        i = i+1

    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('yellow')
    angie.circle(100)

    helen = turtle.Turtle()
    helen.shape('turtle')
    helen.color('red')
    helen.left(30)
    helen.forward(150)
    helen.left(120)
    helen.forward(150)
    helen.left(120)
    helen.forward(150)
    

    window.exitonclick()

draw_shapes()
