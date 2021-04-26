"""
This challenge is based on the game Minesweeper.

Create a function that takes a grid of # and -,
where each hash (#) represents a mine and each dash (-) represents a mine-free spot.

Return a list where each dash is replaced by a digit indicating
the number of mines immediately adjacent to the spot (horizontally, vertically, and diagonally).
num_grid([
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) ➞ [
  ["0", "0", "0", "0", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "1", "#", "1", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "0", "0", "0", "0"],
]

num_grid([
  ["-", "-", "-", "-", "#"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["#", "-", "-", "-", "-"]
]) ➞ [
  ["0", "0", "0", "1", "#"],
  ["0", "1", "1", "2", "1"],
  ["0", "1", "#", "1", "0"],
  ["1", "2", "1", "1", "0"],
  ["#", "1", "0", "0", "0"]
]

num_grid([
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) ➞ [
  ["1", "1", "2", "#", "#"],
  ["1", "#", "3", "3", "2"],
  ["2", "4", "#", "2", "0"],
  ["1", "#", "#", "2", "0"],
  ["1", "2", "2", "1", "0"],
]

[
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, '#', 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
] should equal

[
    ['0', '0', '0', '0', '0'],
    ['0', '1', '1', '1', '0'],
    ['0', '1', '#', '1', '0'],
    ['0', '1', '1', '1', '0'],
    ['0', '0', '0', '0', '0']
]
"""
n = 10

def get_neighbours_indices(i, j):
    return [
        (m, k)
        for m in range(i-1, i+2)
        for k in range(j-1, j+2)
        if (0 <= m < n and 0 <= k < n and not (m == i and k == j))
    ]

print(get_neighbours_indices(0, 0))
print(get_neighbours_indices(1, 0))
print(get_neighbours_indices(0, 1))
print(get_neighbours_indices(5, 5))
print(get_neighbours_indices(9, 9))



def num_grid(grid):
    mine = "#"
    n = len(grid)

    def is_mine(c):
        return c == mine

    def count_mines(i , j):
        neighbours = [
            grid[m][k]
            for m in range(i-1, i+2)
            for k in range(j-1, j+2)
            if (0 <= m < n and 0 <= k < n)
        ]
        num_mines = sum([1 for c in neighbours if is_mine(c)])
        return str(num_mines)

    new_cells = [["0" for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_cells[i][j] = mine if is_mine(grid[i][j]) else count_mines(i, j)

    return new_cells


print(
    num_grid(
        [
          ["-", "-", "-", "#", "#"],
          ["-", "#", "-", "-", "-"],
          ["-", "-", "#", "-", "-"],
          ["-", "#", "#", "-", "-"],
          ["-", "-", "-", "-", "-"]
        ]
    )
)
