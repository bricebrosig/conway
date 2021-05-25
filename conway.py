""" conway.py

this is an implementation of conways game of life

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

color links : https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

@incomplete - add more of the common presets to the preset list
@incomplete - help menu
@incomplete - preset menu
@incomplete - add run option that advances at given speed for given generations
"""
import presets 
from graphics import *
from typing import Tuple, Generator
from time import sleep

input_buffer: str = ""
state: set = set()
CELL_RES: int = 10  # resolution of a cell in pixels
RUN_DELAY: float = .1 
is_running, keep_running = False, True

# get the neighbors to a cell
#
# @param cell (tuple) - x, y coordinate of the cell
# @return generator of tuples: (x, y) coords
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
    new_state: set = set()
    min_x: int = min([x for x, _ in state])
    max_x: int = max([x for x, _ in state])
    min_y: int = min([y for _, y in state])
    max_y: int = max([y for _, y in state])
    
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            cell: tuple = (x, y)
            live_count: int = 0
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


def handle_left_click(x, y):
    global state, is_running, keep_running
    if is_running:
        keep_running = False
        return

    x, y = int(x / CELL_RES), int(y / CELL_RES) + 1

    state.add((x, y))
    
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_right_click(x, y):
    global state

    x, y = int(x / CELL_RES), int(y / CELL_RES) + 1

    state.remove((x, y))
    draw(state, input_buffer, cell_res=CELL_RES)


def handle_enter():
    global state, input_buffer, is_running, keep_running
    command: str = input_buffer.lower().strip()
    input_buffer = ""
    
    if command in {"exit", "quit", "q"}:
        exit(0)
    if command == "clear":
        state = set()
        draw(state, input_buffer)
    if command == "run":
        is_running = True
        while state and keep_running:
            state = advance(state)
            draw(state, input_buffer)
            sleep(RUN_DELAY)
        is_running = False
        keep_running = True
    elif command == "":
        state = advance(state)
        draw(state, input_buffer)

def handle_backspace():
    global state, input_buffer
    input_buffer = input_buffer[:-1]
    draw(state, input_buffer)

def handle_a():
    global input_buffer
    input_buffer += "a"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_b():
    global input_buffer
    input_buffer += "b"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_c():
    global input_buffer
    input_buffer += "c"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_d():
    global input_buffer
    input_buffer += "d"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_e():
    global input_buffer
    input_buffer += "e"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_f():
    global input_buffer
    input_buffer += "f"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_g():
    global input_buffer
    input_buffer += "g"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_h():
    global input_buffer
    input_buffer += "h"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_i():
    global input_buffer
    input_buffer += "i"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_j():
    global input_buffer
    input_buffer += "j"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_k():
    global input_buffer
    input_buffer += "k"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_l():
    global input_buffer
    input_buffer += "l"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_m():
    global input_buffer
    input_buffer += "m"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_n():
    global input_buffer
    input_buffer += "n"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_o():
    global input_buffer
    input_buffer += "o"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_p():
    global input_buffer
    input_buffer += "p"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_q():
    global input_buffer
    input_buffer += "q"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_r():
    global input_buffer
    input_buffer += "r"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_s():
    global input_buffer
    input_buffer += "s"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_t():
    global input_buffer
    input_buffer += "t"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_u():
    global input_buffer
    input_buffer += "u"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_v():
    global input_buffer
    input_buffer += "v"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_w():
    global input_buffer
    input_buffer += "w"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_x():
    global input_buffer
    input_buffer += "x"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_y():
    global input_buffer
    input_buffer += "y"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_z():
    global input_buffer
    input_buffer += "z"
    draw(state, input_buffer, cell_res=CELL_RES)

def handle_space():
    global input_buffer
    input_buffer += " "
    draw(state, input_buffer, cell_res=CELL_RES)


def register_events():
    onkeypress(handle_a, "a")
    onkeypress(handle_b, "b") 
    onkeypress(handle_c, "c") 
    onkeypress(handle_d, "d") 
    onkeypress(handle_e, "e") 
    onkeypress(handle_f, "f") 
    onkeypress(handle_g, "g") 
    onkeypress(handle_h, "h") 
    onkeypress(handle_i, "i") 
    onkeypress(handle_j, "j") 
    onkeypress(handle_k, "k") 
    onkeypress(handle_l, "l") 
    onkeypress(handle_m, "m") 
    onkeypress(handle_n, "n") 
    onkeypress(handle_o, "o") 
    onkeypress(handle_p, "p") 
    onkeypress(handle_q, "q") 
    onkeypress(handle_r, "r") 
    onkeypress(handle_s, "s") 
    onkeypress(handle_t, "t") 
    onkeypress(handle_u, "u") 
    onkeypress(handle_v, "v") 
    onkeypress(handle_w, "w") 
    onkeypress(handle_x, "x") 
    onkeypress(handle_y, "y") 
    onkeypress(handle_z, "z") 
    onkeypress(handle_enter, "Return")
    onkeypress(handle_backspace, "BackSpace")
    onkeypress(handle_space, "space")

    onscreenclick(handle_left_click)
    onscreenclick(handle_right_click, btn=3)


if __name__ == "__main__":
    state = presets.GLIDER

    init_turtle(800, 600)
    draw(state, "", cell_res=CELL_RES)

    register_events()
    listen()
    mainloop()
