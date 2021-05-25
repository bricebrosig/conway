""" conway.py

this is an implementation of conways game of life

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

color links : https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

@incomplete - command line
@incomplete - gui editor
@incomplete - add more of the common presets to the preset list
@incomplete - refactor to add typing
@incomplete - command line options / parsing
@incomplete - help menu
@incomplete - add run option that advances at given speed for given generations
@incomplete - line counters are fun :)

@research - building an actual executable from python code... is that a thing?
"""
import presets 
from graphics import *

from typing import Tuple, Generator


global_input_buffer: str = ""
global_state: set = set()
CELL_RES: int = 10  # resolution of a cell in pixels


# return a generator of the neighbors to the given cell
def neighbors(cell: Tuple[int, int]) -> Generator:
    x, y = cell
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1 
    yield x, y - 1
    yield x + 1, y + 1
    yield x + 1, y - 1
    yield x - 1, y + 1
    yield x - 1, y - 1 


# advance one step of the game
#
# @param state - set of the "live" cells : (x, y) tuples
# @return new state of the game
def advance(state: set) -> set:
    new_state = set()
    min_x = min([x for x, _ in state])
    max_x = max([x for x, _ in state])
    min_y = min([y for _, y in state])
    max_y = max([y for _, y in state])
    
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            cell = (x, y)
            live_count = 0
            for neighbor in neighbors(cell):
                if neighbor in state:
                    live_count = live_count + 1
            
            if cell in state:  # alive
                if live_count == 2 or live_count == 3:
                    new_state.add(cell)
            else:
                if live_count == 3:
                    new_state.add(cell)
    return new_state


def handle_enter():
    global global_state, global_input_buffer
    command = global_input_buffer.lower().strip()
    
    if command in {"exit", "quit", "q"}:
        exit(0)
    elif command == "":
        global_state = advance(global_state)
        draw(global_state, global_input_buffer)


def handle_backspace():
    global global_state, global_input_buffer
    global_input_buffer = global_input_buffer[:-1]
    draw(global_state, global_input_buffer)


def handle_a():
    global global_input_buffer
    global_input_buffer += "a"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_b():
    global global_input_buffer
    global_input_buffer += "b"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_c():
    global global_input_buffer
    global_input_buffer += "c"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_d():
    global global_input_buffer
    global_input_buffer += "d"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_e():
    global global_input_buffer
    global_input_buffer += "e"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_f():
    global global_input_buffer
    global_input_buffer += "f"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_g():
    global global_input_buffer
    global_input_buffer += "g"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_h():
    global global_input_buffer
    global_input_buffer += "h"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_i():
    global global_input_buffer
    global_input_buffer += "i"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_j():
    global global_input_buffer
    global_input_buffer += "j"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_k():
    global global_input_buffer
    global_input_buffer += "k"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_l():
    global global_input_buffer
    global_input_buffer += "l"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_m():
    global global_input_buffer
    global_input_buffer += "m"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_n():
    global global_input_buffer
    global_input_buffer += "n"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_o():
    global global_input_buffer
    global_input_buffer += "o"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_p():
    global global_input_buffer
    global_input_buffer += "p"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_q():
    global global_input_buffer
    global_input_buffer += "q"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_r():
    global global_input_buffer
    global_input_buffer += "r"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_s():
    global global_input_buffer
    global_input_buffer += "s"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_t():
    global global_input_buffer
    global_input_buffer += "t"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_u():
    global global_input_buffer
    global_input_buffer += "u"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_v():
    global global_input_buffer
    global_input_buffer += "v"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_w():
    global global_input_buffer
    global_input_buffer += "w"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_x():
    global global_input_buffer
    global_input_buffer += "x"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_y():
    global global_input_buffer
    global_input_buffer += "y"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_z():
    global global_input_buffer
    global_input_buffer += "z"
    draw(global_state, global_input_buffer, cell_res=CELL_RES)
def handle_space():
    global global_input_buffer
    global_input_buffer += " "
    draw(global_state, global_input_buffer, cell_res=CELL_RES)


def register_keys():
    onkey(handle_a, "a")
    onkey(handle_b, "b") 
    onkey(handle_c, "c") 
    onkey(handle_d, "d") 
    onkey(handle_e, "e") 
    onkey(handle_f, "f") 
    onkey(handle_g, "g") 
    onkey(handle_h, "h") 
    onkey(handle_i, "i") 
    onkey(handle_j, "j") 
    onkey(handle_k, "k") 
    onkey(handle_l, "l") 
    onkey(handle_m, "m") 
    onkey(handle_n, "n") 
    onkey(handle_o, "o") 
    onkey(handle_p, "p") 
    onkey(handle_q, "q") 
    onkey(handle_r, "r") 
    onkey(handle_s, "s") 
    onkey(handle_t, "t") 
    onkey(handle_u, "u") 
    onkey(handle_v, "v") 
    onkey(handle_w, "w") 
    onkey(handle_x, "x") 
    onkey(handle_y, "y") 
    onkey(handle_z, "z") 
    onkey(handle_enter, "Return")
    onkey(handle_backspace, "BackSpace")
    onkey(handle_space, "space")


if __name__ == "__main__":
    global_state = presets.GLIDER

    init_turtle(800, 600)
    draw(global_state, "", cell_res=CELL_RES)

    register_keys()
    listen()
    mainloop()
