""" conway.py

this is an implementation of conways game of life

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

@incomplete : better drawing
@incomplete : world borders
@incomplete : test suite
"""

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
    
    # there must be a way to figure out which dead cells should be
    # revived by only iterating over the existing state - then the problem
    # becomes O(N) where N is the max number of live cells given a seed rather than 
    # O(x*y) where x and y are the grid dimensions of the current state.
    # most conway machines are sparse - checking every grid is not efficient at all
    
    for x in range(min_x, max_x + 1):  # @speed @incomplete 
        for y in range(min_y, max_y + 1):
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
    

def show(state):
    print("============")
    for cell in state:
        print(cell)
    print("============")
    
            
def run(seed):
    print("=== seed ===")
    show(seed)
    state = advance(seed)
    
    while True:
        show(state)
        state = advance(state)        
        input("press enter")
    

if __name__ == "__main__":
    seed = [
        (1,1),
        (1,2),
        (2,1),
        (2,2),
        
        (3,3),
        (3,4),
        (4,3),
        (4,4)
    ]
    run(seed)