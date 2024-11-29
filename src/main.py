from graphics import Window
from Maze import Maze


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x + 200, screen_y + 200)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("maze created...")
    if maze.solve():
        print("maze has been solved!")
    else:
        print("maze cannot be solved!")

    win.wait_for_close()


if __name__ == "__main__":
    main()
