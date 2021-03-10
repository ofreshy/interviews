import logging
import math


class InvalidBoard(Exception):
    pass


def check_soduko_board(board):
    """

    :param board: a suduko board
    :return: Raises InvalidBoard if this board is invalid
    """
    # Board must be
    if not board:
        raise InvalidBoard("Empty board is invalid")

    n = len(board)
    sqrt = math.sqrt(n)
    # size must be a perfect square natural number
    if sqrt - int(sqrt) != 0:
        raise InvalidBoard("None natural sqr number")
    sqrt = int(sqrt)

    # a filter function
    def is_in_range(c):
        return 1 <= c <= n

    # Returns all cells in a soduko box, apart from the given cell
    def get_box(ii, jj):
        i_start = (ii / sqrt) * sqrt
        j_start = (jj / sqrt) * sqrt
        box = []
        for ix in range(i_start, i_start+sqrt):
            for jx in range(j_start, j_start+sqrt):
                if (ix, jx) != (i, j):
                    box.append(board[ix][jx])
        return box

    for i in range(n):
        row = board[i]
        if len(row) != n:
            raise InvalidBoard("row %d length is %d but expected %d" % (i, len(row), n))
        for j in range(n):
            cell = board[i][j]

            if not is_in_range(cell):
                raise InvalidBoard("cell value %d is not in allowed range of [1-%d]" % (cell, n))

            row_but_cell = row[0:j] + row[j+1:n]
            if cell in row_but_cell:
                raise InvalidBoard("row %d contains more than one value of %d" % (i, cell))

            col_but_cell = [board[i][x] for x in range(n) if x != j]
            if cell in col_but_cell:
                raise InvalidBoard("col %d contains more than one value of %d" % (j, cell))

            box_but_cell = get_box(i, j)
            if cell in box_but_cell:
                raise InvalidBoard("box for cell in (%d,%d) contains more than value of %d" % (i, j, cell))

    return None


def is_valid_soduko_board(board):
    """

    :param board: a sudoko board
    :return: True if it is valid, False otherwise
    """
    try:
        check_soduko_board(board)
        return True
    except InvalidBoard as e:
        logging.error(e)
        return False


assert is_valid_soduko_board(None) is False
assert is_valid_soduko_board([]) is False
assert is_valid_soduko_board([[]]) is False

assert is_valid_soduko_board([[1, 2], [1, 2], [1, 2]]) is False
assert is_valid_soduko_board([[1, 2], [1, 2, 3], [1, 2], [1, 2]]) is False
assert is_valid_soduko_board([[1, 2], [1, 2], [1, 2], [1, 2]]) is False

assert is_valid_soduko_board([[1, 2, 3, 3], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]) is False

assert is_valid_soduko_board([[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]])
