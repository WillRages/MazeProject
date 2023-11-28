# Will & Berri 11/20/23

from random import randint

from config import drawing_turtle, levels, new_enemy_turtle, new_player_turtle, sc
from enemy import Enemy
from level import Level
from maze import Maze
from player import Player


def print_maze(maze: list[list[bool]]):
    for row in maze:
        # row is a list of bools
        # print row as a binary string again
        print("".join(map(str, map(int, row))))


# convert list of binary strings into 2d array of bools
def cvt_text_repr(text: list[str]) -> list[list[bool]]:
    return [[y == "1" for y in x] for x in text]


def load_level(level_idx: int):
    global player, enemies, maze_obj, moving
    sc.clear()

    # load level out of level array
    level: Level = levels[level_idx]
    print(level.instructions)
    horiz = level.horizontal_walls
    vert = level.vertical_walls
    items = level.collectibles

    # read wall strings into 2d wall arrays
    (maze_horiz, maze_vert) = (cvt_text_repr(vert), cvt_text_repr(horiz))

    # create maze object using wall arrays
    maze_obj = Maze(maze_horiz, maze_vert, level.lava, items, level.exit)

    # create player using a turtle object and a set of starting coordinates
    player = Player(new_player_turtle(), level.spawnpoint)

    # create an enemy object
    enemies = [Enemy(new_enemy_turtle(), loc) for loc in level.enemies]

    # draw the map using turtle object
    maze_obj.draw_map(drawing_turtle)

    # lock on moving to prevent multiple move methods
    # from running at the same time, which breaks things
    # while still keeping controls responsive
    moving = False

    # function that creates a movement callback for the specified direction
    def move_both(dir: str):
        # inner function
        def foo():
            global moving, player, maze_obj, enemies
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

            # if player is on any dangerous spots, die
            if player.on_any(danger):
                print("you died :<")
                exit()

            # if player is on the exit, go to the next one
            if player.on_any([level.exit]):
                # delete current objects
                player, enemies, maze_obj = (None, None, None)
                try:
                    # recursive level loading is probably bad practice
                    load_level(level_idx + 1)
                except IndexError:
                    print("You win!")
                    exit()

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

# start at first level
load_level(0)
