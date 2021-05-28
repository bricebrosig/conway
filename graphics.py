""" graphics.py

all the functions to draw the state on a screen with turtle / tkinter graphics
"""
from turtle import Screen, Turtle  # init a screen and a turtle

FONT: tuple = ("consolas", 18, "normal")


# initialize the turtle graphics settings
#
# @param width (int) - width of the screen / canvas
# @param height (int) - height of the screen / canvas
def init_turtle(width: int = 400, height: int = 400):
    screen = Screen()
    turtle = Turtle()
    
    screen.title("Conway's Game of Life")
    screen.screensize(width, height, "grey")  # canvas size
    screen.setup(width, height)  # window size (centered)
    screen.setworldcoordinates(0, height, width, 0)
    screen.tracer(0, 0)  # no animation / draw on update() only
    turtle.hideturtle()
    turtle.up()
    screen.update()

    return screen, turtle


# draws a single living cell
#
# @param x (int) - x position
# @param y (int) - y position
# @param col (str) - color of a a live cell
# @param res (int) - resolution (in pixels) of a cell
def draw_cell(turtle: Turtle, x: int, y: int, col: str, res: int):
    turtle.setpos(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(col)
    for _ in range(4):
        turtle.forward(res)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()


# draws command line at bottom of screen
#
# @param buff (str) - the input buffer that gets printed
def draw_command_line(turtle: Turtle, screen, buff: str) -> None:
    turtle.color("white")
    turtle.setpos(0, screen.window_height() - 5)
    turtle.write(">" + buff, font=FONT)
    turtle.color("black")
    

# draw and render all the graphics
#
# @param state (set) - set of live cells (state of the game)
# @param buff (str) - current input buffer for the command line 
# @param editor (tuple) - where the editor cell currently is (def to (-1, -1) for inactive)
# @param cell_res (int) - resolution of a cell in pixels
def draw(turtle: Turtle, screen, state: set, buff: str, editor: tuple = (-1, -1), cell_res: int = 10) -> None:
    if turtle is None:
        print("turtle is none. exiting...")
        exit(1)
    if screen is None:
        print("screen is none. exiting...")
        exit(1)

    turtle.clear()
    for x, y in state:
        draw_cell(turtle, x * cell_res, y * cell_res, "black", cell_res)
    draw_command_line(turtle, screen, buff)
    edit_x, edit_y = editor
    draw_cell(turtle, edit_x, edit_y, "blue", cell_res)
    screen.update()
