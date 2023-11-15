import turtle

from config import *
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
        turtle.goto(
            -board_offset[0] + line_size // 2 + line_size * loc[0],
            board_offset[1] - line_size // 2 - line_size * loc[1],
        )

        self.x, self.y = loc

        self.moving = False

        self.inventory = []

    def move(self, direction: str, maze: Maze):
        # lock on moving to prevent multiple move methods
        # from running at the same time, which breaks things
        # while still keeping controls responsive
        if self.moving:
            return
        self.moving = True
        can_move, pickup = maze.check_dir((self.x, self.y), direction)

        if not pickup is None:
            print(f"Picked up {pickup}!")
            self.inventory.append(pickup)

        self.turtle.seth(self.dir_map[direction])

        if can_move:
            self.turtle.forward(line_size)
            x, y = self.dir_update[direction]
            self.x += x
            self.y += y
        self.moving = False


class Enemy(Player):
    pass
