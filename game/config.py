import turtle

from level import Level

# create sc variable
sc = turtle.Screen()

# create orange variable to store orange file path
orange = "assets/orange.gif"

# add orange
sc.addshape(orange)

# update to reload changes
sc.update()

# function to create a new turtle for a player
def new_player_turtle():
    player_turtle = turtle.Turtle()
    player_turtle.up()
    player_turtle.turtlesize(2)
    return player_turtle

# function to create a new turtle for an enemy
def new_enemy_turtle():
    enemy_turtle = turtle.Turtle()
    enemy_turtle.up()
    enemy_turtle.speed(0)
    enemy_turtle.turtlesize(2)
    enemy_turtle.pencolor("red")
    return enemy_turtle

# create a new drawing turtle
drawing_turtle = turtle.Turtle()
drawing_turtle.speed(0)
drawing_turtle.hideturtle()
drawing_turtle.pensize(10)

line_size = 40

# board offset is so that the game boards appear in the center of the screen
board_offset = (200, 200)

levels: list[Level] = [
    Level(
        horizontal_walls=[
            "10100101011",
            "10010101111",
            "11001010101",
            "10000001001",
            "11000010001",
            "11001010111",
            "11001000011",
            "10000100101",
            "10011101101",
            "10101010001"
        ],
        vertical_walls=[
            "1111011111",
            "0101101000",
            "0010000000",
            "1111111101",
            "0111110110",
            "0011101100",
            "0110010100",
            "0111111110",
            "0111001001",
            "1000010110",
            "1111101111"
        ],
        # collectibles is a map from coordinates to a turtle shape,
        # which places a collectible at the target location
        collectibles={(2, 4): orange},
        # player spawn coordinates
        spawnpoint=(4, -1),
        # list of enemies
        enemies=[],
        # list of lava squares
        lava=[],
        # maze exit coordinates
        exit=(5, 10),
        # message that gets printed on level load
        instructions="Collect all the oranges to win!"
    ),
    Level(
        [
            "11001010001",
            "10110101001",
            "11010001001",
            "11011001001",
            "10010100111",
            "11001101001",
            "10010011101",
            "10101010001",
            "11010101011",
            "11010010101"
        ],
        [
            "1111011111",
            "0000000110",
            "0101111011",
            "0010110101",
            "1100111110",
            "0010001000",
            "0111010011",
            "0110101010",
            "0101010111",
            "0010110000",
            "1111101111"
        ],
        collectibles={},
        spawnpoint=(4, -1),
        enemies=[
            (4, 6),
            (4, 7),
            (4, 8)
        ],
        lava=[
            (6, 6),
            (6, 7),
            (6, 8)
        ],
        exit=(5, 10),
        instructions="Avoid the enemies and lava in order to win."
    ),
]
