# Will & Berri 11/20/23

import turtle
from random import shuffle, randint
from config import *
from time import sleep

from player import *
from maze import Maze
from enemy import Enemy


def print_maze(maze: list[list[bool]]):
    for row in maze:
        # row is a list of bools
        # print row as a binary string again
        print("".join(map(str, map(int, row))))


# convert list of binary strings into 2d array of bools
def cvt_text_repr(text: list[str]) -> list[list[bool]]:
    return [[y == "1" for y in x] for x in text]


def load_level(level_idx: int) -> Maze:
    global player, enemies, maze_obj, moving
    sc.clear()

    # unpack configuration tuple
    (horiz, vert, items, data) = levels[level_idx]

    # read wall strings into 2d wall arrays
    (maze_horiz, maze_vert) = (cvt_text_repr(vert), cvt_text_repr(horiz))

    # create maze object using wall arrays
    maze_obj = Maze(maze_horiz, maze_vert, data["lava"], items, data["exit"])

    # create player using a turtle object and a set of starting coordinates
    player = Player(new_player_turtle(), data["spawnpoint"])

    # create an enemy object
    enemies = [Enemy(new_enemy_turtle(), (x, y)) for (x, y) in data["enemies"]]

    # draw the map using james turtle object
    maze_obj.draw_map(drawing_turtle)

    # lock on moving to prevent multiple move methods
    # from running at the same time, which breaks things
    # while still keeping controls responsive
    moving = False

    def move_both(dir: str):
        def foo():
            global player, enemies, maze_obj, moving
            if moving:
                return
            moving = True
            player.move(dir, maze_obj)
            for enemy in enemies:
                if randint(0, 4) == 0:
                    enemy.move_randomly(maze_obj)
                else:
                    enemy.move(dir, maze_obj)

            danger = maze_obj.lava + [(enemy.x, enemy.y) for enemy in enemies]

            if player.on_any(danger):
                print("you died :<")
                exit()

            if player.on_any([data["exit"]]):
                player, enemies, maze_obj = (None, None, None)
                load_level(level_idx + 1)

            moving = False

        return foo

    # register keybindings
    sc.onkeypress(move_both("right"), "Right")
    sc.onkeypress(move_both("left"), "Left")
    sc.onkeypress(move_both("up"), "Up")
    sc.onkeypress(move_both("down"), "Down")

    sc.onkeypress(move_both("right"), "d")
    sc.onkeypress(move_both("left"), "a")
    sc.onkeypress(move_both("up"), "w")
    sc.onkeypress(move_both("down"), "s")

    sc.listen()

    sc.mainloop()

    # while maze_obj:
    # sleep(0.1)


load_level(0)
