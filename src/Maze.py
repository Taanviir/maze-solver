import random
from time import sleep

from Cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window = None,
        seed: int = None,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self) -> None:
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        if self._win is None:
            return

        x1 = self._x1 * i + self._cell_size_x
        y1 = self._y1 * j + self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i: int, j: int) -> None:
        self._cells[i][j].visited = True

        while True:
            cells_to_visit = []

            # left
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                cells_to_visit.append((i + 1, j))
            # right
            if i > 0 and not self._cells[i - 1][j].visited:
                cells_to_visit.append((i - 1, j))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                cells_to_visit.append((i, j + 1))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                cells_to_visit.append((i, j - 1))

            if len(cells_to_visit) == 0:
                self._draw_cell(i, j)
                return

            move = random.randrange(len(cells_to_visit))
            cell_to_visit = cells_to_visit[move]

            # right
            if cell_to_visit[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if cell_to_visit[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # up
            if cell_to_visit[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # down
            if cell_to_visit[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(cell_to_visit[0], cell_to_visit[1])

    def _reset_cells_visited(self) -> None:
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, i, j) -> bool:
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        possible_moves = [
            (i + 1, j, not current_cell.has_right_wall),  # Right
            (i - 1, j, not current_cell.has_left_wall),  # Left
            (i, j + 1, not current_cell.has_bottom_wall),  # Down
            (i, j - 1, not current_cell.has_top_wall),  # Up
        ]

        for next_i, next_j, can_move in possible_moves:
            if (
                0 <= next_i < self._num_cols
                and 0 <= next_j < self._num_rows
                and can_move
                and not self._cells[next_i][next_j].visited
            ):
                next_cell = self._cells[next_i][next_j]
                current_cell.draw_move(next_cell)
                if self._solve_r(next_i, next_j):
                    return True
                current_cell.draw_move(next_cell, True)
        return False
