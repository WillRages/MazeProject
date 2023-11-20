# Will & ____ 11/20/23

import turtle
from random import shuffle
from config import *

from player import *
from maze import Maze


def print_maze(maze: list[list[bool]]):
    for row in maze:
        # row is a list of bools

        # let's say x is a list, x = [1,5,2,3]
        # f is a function that adds 1 to a number: f(3) = 4
        # map(f, x) = [2,6,3,4]

        print("".join(map(str, map(int, row))))


def cvt_text_repr(text: list[str]) -> list[list[bool]]:
    return [[y == "1" for y in x] for x in text]


def println(text: list):
    for x in text:
        print(x)


def load_level(level_idx: int) -> Maze:
    global player_turtle, james
    # unpack configuration tuple
    (horiz, vert, items, enemy) = levels[level_idx]

    # read wall strings into 2d wall arrays
    (maze_horiz, maze_vert) = (cvt_text_repr(vert), cvt_text_repr(horiz))

    # create maze object using wall arrays
    maze_obj = Maze(maze_horiz, maze_vert, items)

    # create player using a turtle object and a set of starting coordinates
    player = Player(player_turtle, (4, -1))

    # draw the map using james turtle object
    maze_obj.draw_map(james)

    # register keybindings
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
