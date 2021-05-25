""" graphics.py

all the functions to draw the state on a screen with turtle / tkinter graphics
"""
from turtle import *


# initialize the turtle graphics settings
#
# @param width (int) - width of the screen / canvas
# @param height (int) - height of the screen / canvas
def init_turtle(width: int = 400, height: int = 400):
    title("Conway's Game of Life")
    screensize(width, height, "grey")  # canvas size
    setup(width, height)  # window size (centered)
    setworldcoordinates(0, height, width, 0)
    tracer(0, 0)  # no animation / draw on update() only
    hideturtle()
    up()
    update()


# draws a single living cell
#
# @param x (int) - x position
# @param y (int) - y position
# @param col (str) - color of a a live cell
# @param res (int) - resolution (in pixels) of a cell
def draw_cell(x: int, y: int, col: str, res: int):
    setpos(x, y)
    down()
    begin_fill()
    fillcolor(col)
    for _ in range(4):
        forward(res)
        right(90)
    end_fill()
    up()


# draws command line at bottom of screen
#
# @param buff (str) - the input buffer that gets printed
def draw_command_line(buff: str) -> None:
    setpos(0, window_height() - 5)
    write(">" + buff, font=("consolas", 18, "normal"))
    

# draw and render all the graphics
#
# @param state (set) - set of live cells (state of the game)
# @param buff (str) - current input buffer for the command line 
# @param editor (tuple) - where the editor cell currently is (def to (-1, -1) for inactive)
# @param cell_res (int) - resolution of a cell in pixels
def draw(state: set, buff: str, editor: tuple = (-1, -1), cell_res: int = 10) -> None:
    clear()
    for x, y in state:
        draw_cell(x * cell_res, y * cell_res, "black", cell_res)
    draw_command_line(buff)
    edit_x, edit_y = editor
    draw_cell(edit_x, edit_y, "blue", cell_res)
    update()
