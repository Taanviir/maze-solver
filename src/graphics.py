from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int) -> None:
        self._root = Tk()
        self._root.title = "Maze Solver"
        self._canvas = Canvas(self._root, width=width, height=height, bg="white")
        self._canvas.pack(fill=BOTH, expand=1)
        self._isRunning = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self) -> None:
        self._isRunning = True
        while self._isRunning:
            self.redraw()
        print("window closed...")

    def close(self) -> None:
        self._isRunning = False

    def draw_line(self, line: "Line", fill_color: str = "black") -> None:
        line.draw(self._canvas, fill_color)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
