"""
Solves Soduko
"""
import math
from collections.abc import Set
from dataclasses import dataclass
from typing import List, ClassVar


@dataclass
class Index:
    row: int
    col: int


@dataclass
class Cell:
    NO_VAL: ClassVar[int] = 0
    possibilities: Set[int]

    @property
    def values(self):
        return list(self.possibilities)

    @property
    def value(self):
        if self.is_fixed():
            return list(self.possibilities)[0]
        return self.NO_VAL

    def is_fixed(self):
        return len(self.values) == 1

    def print_cell(self, pos=False):
        if pos:
            return "(" + ",".join([str(v) for v in self.values]) + ")"
        else:
            return str(self.value)

    @classmethod
    def from_int(cls, value: int, max_val=9):
        if value == cls.NO_VAL:
            return cls(
                possibilities={v for v in range(1, max_val+1)},
            )
        return cls(
                possibilities={value},
            )

    def __repr__(self):
        return self.print_cell(pos=True)


@dataclass
class Grid:
    size: int
    board: List[List[Cell]]

    @classmethod
    def from_board(cls, board: List[List[int]]):
        size = len(board)
        cell_board = []
        for i, row in enumerate(board):
            cell_board.append([])
            for j, col in enumerate(row):
                cell_board[i].append(
                    Cell.from_int(board[i][j])
                )
        return cls(
            size=size,
            board=cell_board,
        )

    def __post_init__(self):
        self._box_size = int(math.sqrt(self.size))

    @property
    def box_size(self):
        return self._box_size

    def _get_row_but(self, r: int, c: int):
        return [
            self.board[r][i]
            for i in range(self.size)
            if i != c
        ]

    def _get_col_but(self, r: int, c: int):
        return [
            self.board[i][c]
            for i in range(self.size)
            if i != r
        ]

    def _get_box_but(self, r: int, c: int):
        i_start = int((r // self.box_size) * self.box_size)
        j_start = int((c // self.box_size) * self.box_size)
        box = []
        for ix in range(i_start, i_start + self.box_size):
            for jx in range(j_start, j_start + self.box_size):
                if (ix, jx) != (r, c):
                    box.append(self.board[ix][jx])
        return box

    def iter_board(self):
        for r in range(self.size):
            for c in range(self.size):
                cell = self.board[r][c]
                row = self._get_row_but(r, c)
                col = self._get_col_but(r, c)
                box = self._get_box_but(r, c)
                yield (r+1, c+1), cell, row, col, box

    def display(self, pos=False):
        def is_sep_row(r: int):
            return r != 0 and r != self.size and r % self.box_size == 0

        def is_sep_col(c):
            return c % self.box_size == 0 and c != self.size

        out = ""

        for row in range(self.size):
            if is_sep_row(row):
                out += "--------+-------+------\n"
            for col in range(self.size):
                if is_sep_col(col):
                    out += "| "
                cell = self.board[row][col]
                out += cell.print_cell(pos) + " "
            out += "\n"
        return out


board=[
    [2,0,0,0,0,0,0,6,0],
    [0,0,0,0,7,5,0,3,0],
    [0,4,8,0,9,0,1,0,0],
    [0,0,0,3,0,0,0,0,0],
    [3,0,0,0,1,0,0,0,9],
    [0,0,0,0,0,8,0,0,0],
    [0,0,1,0,2,0,5,7,0],
    [0,8,0,7,3,0,0,0,0],
    [0,9,0,0,0,0,0,0,4],
]

grid = Grid.from_board(board)
print(grid.display())


def solve_soduko(grid: Grid):
    change = True
    passes = 1

    def iter_grid():
        def eliminate(other_cells):
            fixed = {c.value for c in other_cells if c.is_fixed()}
            cell.possibilities = cell.possibilities - fixed
        def eliminate_all():
            old_values = cell.values
            eliminate(row)
            eliminate(col)
            eliminate(box)
            return len(old_values) > len(cell.values)

        changes = 0
        for index, cell, row, col, box in grid.iter_board():
            if cell.is_fixed():
                continue
            change = eliminate_all()
            changes += int(change)
        print(cell)
        print(row)
        print(col)
        print(box)
        return changes


    while change and passes < 3:
        x = iter_grid()
        print(grid.display(True))
        print(f"has done {x} changes")
        passes += 1






solve_soduko(grid)