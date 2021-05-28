""" conway.py

this is an implementation of conways game of life

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

@incomplete - menu screen
@incomplete - help menu
@incomplete - preset menu
@incomplete - have a button that pulls up the command line
"""

from typing import Tuple, Generator
from time import sleep
from functools import partial

import presets 
from graphics import *

# ================= settings =====================

class GameState:
    GAME = 1
    MENU = 2
    COMMAND = 3

input_buffer: str = ""
state: set = set()
CELL_RES: int = 10  # resolution of a cell in pixels
RUN_DELAY: float = .1 
is_running, keep_running = False, True
game_state: int = GameState.GAME
screen = None
turtle = None

# ==================================================

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
    global state, is_running, keep_running, screen, turtle
    if is_running:
        keep_running = False
        return

    x, y = int(x / CELL_RES), int(y / CELL_RES) + 1
    state.add((x, y))
    draw(turtle, screen, state, input_buffer, cell_res=CELL_RES)


def handle_right_click(x, y):
    global state, screen, turtle

    x, y = int(x / CELL_RES), int(y / CELL_RES) + 1
    state.remove((x, y))
    draw(turtle, screen, state, input_buffer, cell_res=CELL_RES)


def handle_enter(*args):
    # global state, input_buffer, is_running, keep_running, CELL_RES, screen, turtle
    global state, input_buffer, CELL_RES, keep_running, is_running

    command: str = input_buffer.lower().strip().split(" ")[0]
    args: list = input_buffer.lower().strip().split(" ")[1:]
    input_buffer = ""

    if command in {"exit", "quit", "q"}:
        exit(0)
    elif command == "clear":
        state = set()
        draw(turtle, screen, state, input_buffer, cell_res=CELL_RES)
    elif command == "size":
        if len(args) == 1:
            CELL_RES = int(args[0])
        draw(turtle, screen, state, input_buffer, cell_res=CELL_RES)
    elif command == "run":
        is_running = True
        while state and keep_running:
            state = advance(state)
            draw(turtle, screen, state, input_buffer, cell_res=CELL_RES)
            sleep(RUN_DELAY)   # TODO: using sleep here is pretty bad
        is_running = False
        keep_running = True
    elif command == "":
        state = advance(state)
        draw(turtle, screen, state, input_buffer, cell_res=CELL_RES)


def handle_backspace(*args):
    global input_buffer
    input_buffer = input_buffer[:-1]
    draw(turtle, screen, state, input_buffer)


def key_handler(key):
    global state, input_buffer, is_running, keep_running, CELL_RES, screen, turtle

    if key in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYS1234567890 ":  # alphanum
        input_buffer += key
        draw(turtle, screen, state, input_buffer, cell_res=CELL_RES)


def _onkeypress(self, fun, key=None):
    if fun is None:
        if key is None:
            self.cv.unbind("<KeyPress>", None)
        else:
            self.cv.unbind("<KeyPress-%s>" % key, None)
    else:
        def eventfun(event):
            fun(event.char)

        if key is None:
            self.cv.bind("<KeyPress>", eventfun)
        else:
            self.cv.bind("<KeyPress-%s>" % key, eventfun)


def main():
    global state, screen, turtle
    state = presets.GLIDER

    screen, turtle = init_turtle(800, 600)
    draw(turtle, screen, state, "", cell_res=CELL_RES)

    screen._onkeypress = partial(_onkeypress, screen)
    screen.onkeypress(handle_enter, "Return")
    screen.onkeypress(handle_backspace, "BackSpace")
    screen.onkeypress(key_handler)
    screen.onscreenclick(handle_left_click)
    screen.onscreenclick(handle_right_click, btn=3)
    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
