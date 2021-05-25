""" graphics.py

all the functions to draw the state on a screen with turtle / tkinter graphics
"""
from turtle import *

def init_turtle(width: int = 400, height: int = 400):
    title("Conway's Game of Life")
    screensize(width, height, "grey")  # canvas size
    setup(width, height)  # window size (centered)
    setworldcoordinates(0, height, width, 0)
    tracer(0, 0)  # no animation / draw on update() only
    hideturtle()
    up()
    update()


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


def draw_command_line(buff: str) -> None:
    setpos(0, window_height() - 5)
    write(">" + buff, font=("consolas", 18, "normal"))
    

def draw(state: set, buff: str, editor: tuple = (-1, -1), cell_res: int = 10) -> None:
    clear()
    for x, y in state:
        draw_cell(x * cell_res, y * cell_res, "black", cell_res)
    draw_command_line(buff)
    update()



