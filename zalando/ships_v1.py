# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


class Board(object):
    """
    Board is a mutable object where each coordinate is a key
    and the value is bool representing whether it was hit or not
    """

    @classmethod
    def from_n(cls, n):
        """
        Creates a board from int n
        :param int n: board size
        :return: initial board of size N
        """
        cells = dict()
        for i in range(1, 1+n):
            for j in range(ord("A"), ord("A")+n):
                cells[(i, j)] = False
        return cls(cells)

    def __init__(self, cells):
        self._cells = cells

    def hit(self, coords):
        """

        :param str coords: such as 1A
        :return: mutate board cell in this coordinate to be hit
        """
        int_coords = to_int_coords(coords)
        self._cells[int_coords] = True

    def get_ship_cells(self, two_coord_strings):
        """

        :param two_coord_strings: such as "1A 2B"
        :return: all cells and values associated with the rectangle defined by cells. Essentially, as ship!
        """
        top_left, bottom_right = two_coord_strings.strip().split(" ")
        i_start, j_start = to_int_coords(top_left)
        i_end, j_end = to_int_coords(bottom_right)
        cells = [
            (i, j, self._cells[(i, j)])
            for i in range(i_start, i_end + 1)
            for j in range(j_start, j_end + 1)
        ]
        return cells


def to_int_coords(coord):
    """

    :param str coord: such as 1A
    :return: int tuple such as (1, 65)
    """
    # Work with ints, since we are using dicts, do not care about normalizing letters
    num, letter = coord[0:-1], coord[-1:]
    return int(num), ord(letter)


def is_sunk(ship_cells):
    """
    A sunk ship is a ship that all its cells are hit
    :param ship_cells:
    :return: True if all cells are hit
    """
    return all(v[2] for v in ship_cells)


def is_hit(ship_cells):
    """
    A hit ship it a ship with at least one hit cell
    A sunk ship is always a hit ship!
    Caller should maintain count logic
    :param ship_cells:
    :return:
    """
    return any(v[2] for v in ship_cells)


def solution(N, S, T):
    board = Board.from_n(N)

    for hit in T.split(" "):
        board.hit(hit)

    ships = [board.get_ship_cells(s) for s in S.split(",") if S]
    sunk, hit = 0, 0
    for ship in ships:
        if is_sunk(ship):
            sunk += 1
        elif is_hit(ship):
            hit += 1

    return "%s,%s" % (sunk, hit)


assert solution(4, "1B 2C,2D 4D", "2B 2D 3D 4D 4A") == "1,1"
assert solution(3, "1A 1B,2C 2C", "1B") == "0,1"
assert solution(12, "1A 2A,12A 12A", "12A") == "1,0"
assert solution(12, "1B 2C,2B 4C", "1A 4A 1D 4D") == "0,0"
assert solution(3, "2C 2C", "2C") == "1,0"
assert solution(3, "", "2C") == "0,0"
