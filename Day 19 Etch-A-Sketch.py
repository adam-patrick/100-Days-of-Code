from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("blue")


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(90)


def turn_right():
    tim.right(90)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.textinput(title="Keys", prompt="w = Forward\ns = Backwards\n "
                                      "a = Turn Left\n d = Turn Right\n c = Clear Screen and Return Home")
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
