from graphics import Window, Line, Point


class Cell:
    def __init__(self, window: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = window

    def draw(self, x1: int, y1: int, x2: int, y2: int, fill_color: str = "black"):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), fill_color)
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), fill_color)
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), fill_color)
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), fill_color)

    def draw_move(self, to_cell, undo=False):
        def get_cell_center(cell: Cell) -> Point:
            x = (cell.__x1 + cell.__x2) / 2
            y = (cell.__y1 + cell.__y2) / 2
            return Point(x, y)

        if undo:
            fill_color = "red"
        else:
            fill_color = "gray"

        line = Line(get_cell_center(self), get_cell_center(to_cell))
        self.__win.draw_line(line, fill_color)
