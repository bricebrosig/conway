""" conway.py

this is an implementation of conways game of life

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

@incomplete - add run option that advances at given speed for given generations
@incomplete - detect window resize events
@incomplete - tkinter / turtle gui 

huge
+-------+
|       |
|       |
|       |
+-------+

big
+-----+
|     |
|     |
+-----+

reg
+---+
|   |
+---+

small
%
"""
import os
from msvcrt import getch  # for edit()

import presets 
from keycodes import *


# == codes ==
LIVE_COLOR      = "\u001b[30m"
EDIT_COLOR      = "\u001b[34m"
CHARACTER       = "\u25A0"
RESET_CODE      = "\u001b[0m"
CLEAR_CODE      = "\033c"
BACKGROUND_WHITE = "\u001b[47m"
COLOR_BLACK     = "\u001b[30m"

# == "settings" ==
RESOLUTIONS     = {"small", "regular", "big", "huge"}
RESOLUTION      = "small"


# return a generator of the neighbors to the given cell
def neighbors(cell):
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
def advance(state):
    new_state = set()
    min_x = min([x for x, _ in state])
    max_x = max([x for x, _ in state])
    min_y = min([y for _, y in state])
    max_y = max([y for _, y in state])
    
    # @speed
    # 
    # there must be a way to figure out which dead cells should be revived
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


def draw_board(state, editor=(-1, -1)):
    cols, lines = os.get_terminal_size()

    build_str = ""
    x_pos = 0
    y_pos = 0

    if RESOLUTION == "small":
        height = lines - 1
        width = cols - 1 

        for _ in range(height):
            save_x = x_pos
            for _ in range(width):
                if (x_pos, y_pos) in state:
                    build_str += LIVE_COLOR + CHARACTER
                    build_str += RESET_CODE
                elif (x_pos, y_pos) == editor:
                    build_str += EDIT_COLOR + CHARACTER
                    build_str += RESET_CODE
                else:
                    build_str += CHARACTER
                x_pos = x_pos + 1
            x_pos = save_x
            build_str += "\n"
            y_pos = y_pos + 1

        print(CLEAR_CODE + build_str)
        return

    # TODO: handle other sizes
    # TODO: handle editing for other sizes

    elif RESOLUTION == "regular":
        height = int(lines / 2) 
        width = int(cols / 4)

        for _ in range(height):
            build_str += "+"
            for _ in range(width):
                build_str += "---+"

            save_x = x_pos
            build_str += "\n|"
            for _ in range(width):
                if (x_pos, y_pos) in state:
                    build_str += "%%%|"
                else:
                    build_str += "   |"
                x_pos = x_pos + 1
            x_pos = save_x

            build_str += "\n"
            y_pos = y_pos + 1

        build_str += "+"
        for _ in range(width):
            build_str += "---+"

        print(CLEAR_CODE + build_str)


def edit(state):
    # @incomplete - this currently only supports windows :/
    cols, lines = os.get_terminal_size()
    edit_x = 0
    edit_y = 0

    while True:
        keycode = getch()

        if keycode in [KEY_SPEC, KEY_SPEC_1]:
            double_keycode = getch()  # read the next keycode appropriately

            if double_keycode == KEY_UP:    edit_y = max(edit_y - 1, 0)
            if double_keycode == KEY_DOWN:  edit_y = min(edit_y + 1, lines - 1)
            if double_keycode == KEY_LEFT:  edit_x = max(edit_x - 1, 0)
            if double_keycode == KEY_RIGHT: edit_x = min(edit_x + 1, cols -1)

            draw_board(state, (edit_x, edit_y))
            

        if keycode in [b'\x03', b'q', b'Q']:
            return

        if keycode == KEY_RETURN:
            state.add((edit_x, edit_y))
            draw_board(state)


def presets_menu():
    # TODO: draw the preset

    selected_line = 0
    while True:
        build_str = CLEAR_CODE + "***** PRESETS *****\n"
        for i, pre in enumerate(presets.ALL_STR):
            if i == selected_line:
                build_str += BACKGROUND_WHITE + COLOR_BLACK + pre + "\n" + RESET_CODE
            else:
                build_str += pre + "\n"
        print(build_str)

        keycode = getch()

        if keycode in [KEY_SPEC, KEY_SPEC_1]:
            double_keycode = getch()
            if double_keycode == KEY_UP:    selected_line = max(selected_line - 1, 0)
            if double_keycode == KEY_DOWN:  selected_line = min(selected_line + 1, len(presets.ALL_STR) - 1)

        if keycode in [b'\x03', b'q', b'Q']:
            return None

        if keycode == KEY_RETURN:
            return presets.ALL[selected_line]


if __name__ == "__main__":
    state = presets.GLIDER
    print(CLEAR_CODE)
    draw_board(state)

    while True:
        input_str = input("> ")

        input_str = input_str.split(" ")
        command = input_str[0].lower()
        args = [arg.lower() for arg in input_str[1:]]

        if command == "glider":
            state = presets.GLIDER
            draw_board(state)
            continue
        if command == "blinker":
            state = presets.BLINKER
            draw_board(state)
            continue
        if command == "square":
            state = presets.SQUARE
            draw_board(state)
            continue
        if command == "size" and args:
            RESOLUTION = args[0]
            draw_board(state)
            continue
        if command == "edit":
            edit(state)
        if command == "presets":
            new_state = presets_menu()
            if new_state: state = new_state
            draw_board(state)
            continue
        if command == "help":
            pass  # TODO: implement this
        if command in {"quit", "exit", "stop"}:
            exit(0)

        state = advance(state)
        draw_board(state)
