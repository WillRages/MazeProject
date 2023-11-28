from random import choice

from maze import Maze
from player import Player


class Enemy(Player):
    directions = [
        "left",
        "right",
        "up",
        "down",
    ]

    def move_randomly(self, maze: Maze):
        self.move(choice(self.directions), maze)
