import operator

class Maze(object):
    """Represents a two-dimensional maze, where each cell can hold a
       single marker."""

    def __init__(self, lst):
        self.data = lst

    def find(self, symbol):
        """Find the first instance of the specified symbol in the
           maze, and return the row-index and column-index of the
           matching cell. Return None if no such cell is found."""
        for r, line in enumerate(self.data):
            try:
                return r, line.index(symbol)
            except ValueError:
                pass

    def get(self, where):
        """Return the symbol stored in the specified cell."""
        r, c = where
        return self.data[r][c]

    def set(self, where, symbol):
        """Store the specified symbol in the specified cell."""
        r, c = where
        self.data[r][c] = symbol

    def __str__(self):
        return '\n'.join(''.join(r) for r in self.data)

def solve(maze, where=None, direction=None):
    start_symbol = 'S'
    end_symbol = 'E'
    vacant_symbol = 'O'
    backtrack_symbol = '.'
    directions = (0, 1), (1, 0), (0, -1), (-1, 0)
    direction_marks = '>', 'V', '<', '^'

    where = where or maze.find(start_symbol)
    if not where:
        # no start cell found
        return[]
    if maze.get(where) == end_symbol:
        # standing on the end cell
        return [end_symbol]
    if maze.get(where) not in (vacant_symbol, start_symbol):
        # somebody has been here
        return[]

    for direction in directions:
        next_cell = list(map(operator.add, where, direction))

        # spray-painting direction
        marker = direction_marks[directions.index(direction)]
        if maze.get(where) != start_symbol:
            maze.set(where, marker)

        sub_solve = solve(maze, next_cell, direction)
        if sub_solve:
            # found solution in this direction
            is_first_step = maze.get(where) == start_symbol
            return ([start_symbol] if is_first_step else []) +\
                ([] if is_first_step else [marker])

    # no directions worked from here - have to backtrack
    maze.set(where, backtrack_symbol)
    return []

