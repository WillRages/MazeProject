import turtle
from random import shuffle
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

        # shuffle(lines)

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


def print_maze(maze: list[list[bool]]):
    for row in maze:
        print("".join(map(str, map(int, row))))


def cvt_text_repr(text: list[str]) -> list[list[bool]]:
    return [[y == "1" for y in x] for x in text]


def println(text: list):
    for x in text:
        print(x)


def load_level(level_idx: int) -> Maze:
    global player_turtle, james
    (horiz, vert, items, enemy) = levels[level_idx]
    (maze_horiz, maze_vert) = (cvt_text_repr(vert), cvt_text_repr(horiz))

    maze_obj = Maze(maze_horiz, maze_vert, items)

    player = Player(player_turtle, (4, -1))
    maze_obj.draw_map(james)

    sc.onkeypress(lambda: player.move("right", maze_obj), "Right")
    sc.onkeypress(lambda: player.move("left", maze_obj), "Left")
    sc.onkeypress(lambda: player.move("up", maze_obj), "Up")
    sc.onkeypress(lambda: player.move("down", maze_obj), "Down")

    sc.onkeypress(lambda: player.move("right", maze_obj), "d")
    sc.onkeypress(lambda: player.move("left", maze_obj), "a")
    sc.onkeypress(lambda: player.move("up", maze_obj), "w")
    sc.onkeypress(lambda: player.move("down", maze_obj), "s")


load_level(0)


sc.listen()
sc.exitonclick()
