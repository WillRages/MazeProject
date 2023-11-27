import turtle

sc = turtle.Screen()

orange = "assets/orange.gif"
sc.addshape(orange)
sc.update()


def new_player_turtle():
    player_turtle = turtle.Turtle()
    player_turtle.up()
    player_turtle.turtlesize(2)
    return player_turtle


def new_enemy_turtle():
    enemy_turtle = turtle.Turtle()
    enemy_turtle.up()
    enemy_turtle.speed(0)
    enemy_turtle.turtlesize(2)
    enemy_turtle.pencolor("red")
    return enemy_turtle


drawing_turtle = turtle.Turtle()
drawing_turtle.speed(0)
drawing_turtle.hideturtle()
drawing_turtle.pensize(10)

line_size = 70

board_offset = (300, 300)


levels: list = [
    (
        [
            "10100101011",
            "10010101111",
            "11001010101",
            "10000001001",
            "11000010001",
            "11001010111",
            "11001000011",
            "10000100101",
            "10011101101",
            "10101010001",
        ],
        [
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
            "1111101111",
        ],
        {(2, 4): orange},
        {
            "spawnpoint": (4, -1),
            "enemies": [
                (4, 6),
                (4, 7),
                (4, 8),
            ],
            "lava": [],
            "exit": (5, 10),
        },
    ),
    (
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
            "11010010101",
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
            "1111101111",
        ],
        {},
        {
            "spawnpoint": (4, -1),
            "enemies": [
                (4, 6),
                (4, 7),
                (4, 8),
            ],
            "lava": [
                (6, 6),
                (6, 7),
                (6, 8),
            ],
            "exit": (5, 10),
        },
    ),
]
