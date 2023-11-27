from config import *
from player import Player
from maze import Maze
import turtle
from random import choice


class Enemy(Player):
    directions = [
        "left",
        "right",
        "up",
        "down",
    ]

    def move_randomly(self, maze: Maze):
        self.move(choice(self.directions), maze)

    def kill_player(self, player_coords: tuple[int, int]):
        if (self.x, self.y) == player_coords:
            print("You died! :<")
            exit()
