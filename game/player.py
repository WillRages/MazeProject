import turtle

from config import board_offset, line_size
from maze import Maze


class Player:
    dir_map = {
        "left": 180,
        "right": 0,
        "up": 90,
        "down": 270,
    }

    dir_update = {
        "left": (-1, 0),
        "right": (1, 0),
        "up": (0, -1),
        "down": (0, 1),
    }

    dir_dir = {
        "left": "vert",
        "right": "vert",
        "up": "horiz",
        "down": "horiz",
    }

    def __init__(self, turtle: turtle.Turtle, loc: tuple[int, int] = (0, 0)):
        self.turtle = turtle
        turtle.up()
        self.goto(loc)

        self.x, self.y = loc

        self.inventory = []

    def goto(self, loc: tuple[int, int]):
        self.turtle.goto(
            -board_offset[0] + line_size // 2 + line_size * loc[0],
            board_offset[1] - line_size // 2 - line_size * loc[1],
        )

    def on_any(self, spots: list[tuple[int, int]]):
        return any((self.x, self.y) == loc for loc in spots)

    def move(self, direction: str, maze: Maze):
        can_move, pickup = maze.check_dir((self.x, self.y), direction)

        if pickup is not None:
            print(f"Picked up {pickup}!")
            self.inventory.append(pickup)

        self.turtle.seth(self.dir_map[direction])

        if can_move:
            # self.turtle.goto()
            # self.turtle.forward(line_size)
            x, y = self.dir_update[direction]
            self.x += x
            self.y += y
            self.goto((self.x, self.y))
