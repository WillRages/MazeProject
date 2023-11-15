import turtle

from config import *


def spawn_turtle(loc: tuple[int, int], shape: str) -> turtle.Turtle:
    temp = turtle.Turtle(shape=shape)
    temp.up()
    temp.speed(0)

    temp.goto(
        -board_offset[0] + loc[0] * line_size - line_size // 2,
        board_offset[1] - loc[1] * line_size - line_size // 2,
    )

    return temp


class Maze:
    def __init__(
        self,
        horiz: list[list[bool]],
        vert: list[list[bool]],
        collectibles: dict[tuple[int, int], str],
    ):
        self.horiz = horiz
        self.vert = vert
        self.collectibles = {x: spawn_turtle(x, y) for x, y in collectibles.items()}

    def draw_line(self, loc: tuple[int, int], direction: str, pen: turtle.Turtle):
        pen.up()
        pen.goto(
            -board_offset[0] + loc[0] * line_size,
            board_offset[1] - loc[1] * line_size,
        )
        pen.down()
        pen.seth({"horiz": 0, "vert": -90}[direction])
        pen.forward(line_size)
        pen.up()

    def draw_map(self, pen: turtle.Turtle):
        lines = []

        for i, row in enumerate(self.horiz):
            for j, draw_line in enumerate(row):
                if draw_line:
                    lines.append(((j, i), "horiz"))

        for i, row in enumerate(self.vert):
            for j, draw_line in enumerate(row):
                if draw_line:
                    lines.append(((j, i), "vert"))

        turtles = [pen.clone() for _ in range(10)]
        turtle = 0
        i = 0

        while i < len(lines):
            self.draw_line(lines[i][0], lines[i][1], turtles[turtle])
            turtle += 1
            turtle %= len(turtles)
            i += 1

    dir_lookup = {
        "left": ("vert", 0, 0),
        "right": ("vert", 1, 0),
        "up": ("horiz", 0, 0),
        "down": ("horiz", 0, 1),
    }

    def check_dir(self, loc: tuple[int, int], dir: str) -> tuple[bool, str | None]:
        (arr_key, dx, dy) = self.dir_lookup[dir]

        arr, idx, idy = (
            {"horiz": self.horiz, "vert": self.vert}[arr_key],
            loc[0] + dx,
            loc[1] + dy,
        )

        col: turtle.Turtle = self.collectibles.get((idx, idy), None)
        if not col is None:
            col.hideturtle()
            self.collectibles.pop((idx, idy))

        if 0 <= idy < len(arr) and 0 <= idx < len(arr[0]):
            return not arr[idy][idx], col
        else:
            return False, None
